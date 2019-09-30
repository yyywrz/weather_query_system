from requestWeather import *
from formatting import *
from mongoDBhandler import *
import pymongo

def insertWeatherData(city):
    try: 
        weatherJson = weather(city).weather_json()
        #load json file from weatherDataRequest.py

        Instance = weatherInstance(weatherJson)
        instanceToBeInserted = Instance.formattedInstance()
        #obtain stylized form by weatherInstance.py

        weatherByCity = mdb(27017,'weatherDatabase','weatherByCity')
        #port:27017 
        #database name: weatherDatabase
        #collection: weatherByCity

        potentialDuplicate = weatherByCity.getOne('location',instanceToBeInserted['location'])
        # identify if the weather data of the desired city exists

        if (potentialDuplicate is None):
            weatherByCity.addOne(instanceToBeInserted)
            #create new
            return('create')
        else:
            query={'location':instanceToBeInserted['location']}
            for key in instanceToBeInserted:
                value=instanceToBeInserted[key]
                weatherByCity.updateOne(query,key,value)
            # update old data
            return('update')

    except:
        return('illegal')



if __name__=="__main__":
    import sys
    command=sys.argv[1]

    if (command=='test'):
        weatherByCity = mdb(27017,'weatherDatabase','weatherByCity')
        weatherByCity.removeAll()
        print(insertWeatherData('springfield'))
        print(insertWeatherData('123'))
        print(insertWeatherData('springfield'))
        print(insertWeatherData('springfield,canada'))
        print(insertWeatherData('springfield,Pennsylvania'))
        print()
        for x in weatherByCity.all():
            print(x['location'])
        weatherByCity.removeAll()
    else:
        print(insertWeatherData(command))