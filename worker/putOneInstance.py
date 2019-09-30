import requestWeather as wdr
import formatting as wi
import mongoDBhandler as db
import pymongo

def insertWeatherData(city):
    try: 
        weatherJson = wdr.weather(city).weather_json()
        #load json file from weatherDataRequest.py

        weatherInstance = wi.weatherInstance(weatherJson)
        instanceToBeInserted = weatherInstance.formattedInstance()
        #obtain stylized form by weatherInstance.py

        weatherByCity = db.handler(27017,'weatherDatabase','weatherByCity')
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
    #import sys
    command='test'#sys.argv[1]

    if (command=='test'):
        weatherByCity = db.handler(27017,'weatherDatabase','weatherByCity')
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