class weatherInstance:

    def __init__(self,weatherJson):
        self.weatherJson = weatherJson
        self.n = 7
    
    def location(self):
        return({
            'city': self.weatherJson['location']['name'],
            'region': self.weatherJson['location']['region'],
            'country': self.weatherJson['location']['country']
        })

    def localTime(self):
        return self.weatherJson['location']['localtime']

    def dataCapturedTime(self):
        return self.weatherJson['current']['last_updated']

    def currentTemperature(self):
        return int(self.weatherJson['current']['temp_c'])

    def condition(self):
        return self.weatherJson['current']['condition']['text']

    def currentAstro(self):
        return self.weatherJson['current']['condition']['text']

    def forecastPeriod(self):
        period=[]
        for i in range(0,self.n):
            period.append\
                (self.weatherJson['forecast']['forecastday'][i]['date'])
        return period

    def forecast(self):
        forecast_data=dict()
        for i in range(0,self.n):
            forecast_data[self.forecastPeriod()[i]]={\
                'avgtemp':(int(self.weatherJson['forecast']\
                    ['forecastday'][i]['day']['avgtemp_c'])),
                'condition':(self.weatherJson['forecast']\
                    ['forecastday'][i]['day']['condition']['text']),
                'astro':(self.weatherJson['forecast']\
                    ['forecastday'][i]['astro'])
                }
        return forecast_data
    
    def formattedInstance(self):
        return({
            'location': self.location(),
            'current':{
                'localTime':self.localTime(),
                'condition':self.condition(),
                'astro':self.currentAstro(),
                'dataCapturedTime':self.dataCapturedTime(),
                'currentTemperature':self.currentTemperature()},
            'forecast':self.forecast(),
        })

if __name__=='__main__':
    import requestWeather as wdr
    w1 = wdr.weather('shanghai').weather_json()
    ins = weatherInstance(w1)
    print(ins.location())
    print(ins.localTime())
    print(ins.dataCapturedTime())
    print(ins.currentTemperature())
    print(ins.forecastPeriod())
    ins.forecast()
    print(ins.formattedInstance())

