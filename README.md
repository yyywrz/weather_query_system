# weather_query_system
This is a tiny python program that gets weather data via api
<br>
This program has been __deprecated__, because the service provider upgrad the api. The address has been changed to https://weatherstack.com. Most importantly, weather forecast api is not for free anymore.
<br><br>
**1. requestWeather.py**<br>
The fisrt step -- to request data via api https://api.apixu.com/v1/, and then return a proper json dict.
<br><br>
**2. mongoDBhandler.py**
<br>
A helper for connect database and insert/update weather data (by pymongo).
<br><br>
**3. formatting.py**<br>
A handler to extract data from raw data (from 1) and reformat.
<br><br> 
**4. putOneInstance.py**
<br>
Inserction formatted data to database. There are three return values:
<br>

| return value        | meanings   | 
| ------------- | ------------- | 
| `create`      | successful insert data into database | 
| `update`     | the data already existed, replace by latest one |
| `illegal`    | failed to insert/obtain data |

<br><br>
**5. refresher.py**
<br>
A refresher that works every 30s to update all existing data.
