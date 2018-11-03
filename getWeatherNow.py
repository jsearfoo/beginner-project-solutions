import requests,json
import time,datetime

city=input("enter your city name\n")

app_id=input("Please input valid API key")
app_id=app_id.replace("\"",'')
app_id=app_id.replace(" ",'')

ddict = {}
weather_url="http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city,app_id)
resp=requests.get(weather_url)

data=json.loads(resp.text)

# data={"coord":{"lon":-0.13,"lat":51.51},"weather":[{"id":800,"main":"Clear","description":"clear sky","icon":"01d"}],"base":"stations","main":{"temp":289.69,"pressure":1028,"humidity":63,"temp_min":288.15,"temp_max":291.15},"visibility":10000,"wind":{"speed":3.1,"deg":220},"clouds":{"all":0},"dt":1540387200,"sys":{"type":1,"id":5091,"message":0.0105,"country":"GB","sunrise":1540363245,"sunset":1540399661},"id":2643743,"name":"London","cod":200}

temprature_kelvin=data['main']['temp']                                         #temprature

temprature_celcius=temprature_kelvin-273

pressure=data['main']['pressure']                                       #pressure

humidity=data['main']['humidity']                                       #humidity

min_temp_kelvin=data['main']['temp_min']                                         #temp_min

min_temp_celcius=min_temp_kelvin-273

max_temp_kelvin=data['main']['temp_max']                                         #temp_max

max_temp_celcius=max_temp_kelvin-273


status=data['weather'][0]['main']                                       #Weather's main status

description=data['weather'][0]['description']                                #Weather's description


print('''

Here's is the weather for your city {}

Temprature={} Celcius

Pressure={} Pascals

Humidity={}

Min Temp={}

Max Temp={}


'''.format(city,temprature_celcius,pressure,humidity,min_temp_celcius,max_temp_celcius))


try:
    print("Press Ctrl + C to quit")
    time.sleep(60)



except KeyboardInterrupt:

    print("Good Bye")




