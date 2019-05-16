#!/usr/bin/python
#cmd: pip install pyowm
import pyowm
city=input("What city you are interested:")
owm = pyowm.OWM(' your-API-key ef2206ff5da67de63306d0b143e20872')    # You MUST provide a valid API key
# Have a pro subscription? Then use:
# owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
# Search for current weather in the city

observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
print("In " + city + " city" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
print("In this city "+ w.get_detailed_status())