import json
import requests

class weather:    

    def __init__(self,inputCityName):
        self.inputCityName = inputCityName.replace(',',' ').replace(' ','+')

    def weather_json(self):
        my_key = 'fc940f1393ff4ebbae665613192208'
        url = 'https://api.apixu.com/v1/'
        category = 'forecast'
        predictPeriod = '7'
        weather_api = url + (category+'.json') \
            + ('?key='+my_key) + ('&q='+self.inputCityName)\
                +('&days=' + predictPeriod)
        try:
            return requests.get(weather_api).json()
        except Exception as err:
            return(err)

if __name__=="__main__":
    print(weather('Springfield, Massachusetts, United States of America').weather_json())
