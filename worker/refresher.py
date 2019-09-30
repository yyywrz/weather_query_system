import time
from putOneInstance import *
from mongoDBhandler import *

def refresh():
    weatherByCity = mdb(27017,'weatherDatabase','weatherByCity')
    while 1:
        for x in weatherByCity.all():
            insertWeatherData(x['location'])           
        time.sleep(60)
#renew all instances in every 30s

if __name__=="__main__":
    weatherByCity = mdb(27017,'weatherDatabase','weatherByCity')
    weatherByCity.removeAll()
    citys = ['beijing','Shanghai,Shanghai,China'\
        ,'beijing','123','kunming','Fairfax',\
         'washington DC','san jose','springfield,ca'\
             ,'springfield,v','springfield,Pennsylvania']
    #put in some initial data

    for city in citys:
        print(city,insertWeatherData(city))
    #insert the instance citys
    refresh()