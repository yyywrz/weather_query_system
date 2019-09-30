import time
import putOneInstance as di
import mongoDBhandler as db

def refresh():
    weatherByCity = db.handler(27017,'weatherDatabase','weatherByCity')
    while 1:
        for x in weatherByCity.all():
            di.insertWeatherData(x['location'])           
        time.sleep(60)
#renew all instances in every 30s

if __name__=="__main__":
    weatherByCity = db.handler(27017,'weatherDatabase','weatherByCity')
    weatherByCity.removeAll()
    citys = ['beijing','Shanghai,Shanghai,China'\
        ,'beijing','123','kunming','Fairfax',\
         'washington DC','san jose','springfield,ca'\
             ,'springfield,v','springfield,Pennsylvania']
    #put in some initial data

    for city in citys:
        print(city,di.insertWeatherData(city))
    #insert the instance citys
    refresh()