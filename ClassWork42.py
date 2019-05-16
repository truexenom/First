#!/usr/bin/python
#cmd: pip install pyowm
import pyowm

misto=input()
owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')    # You MUST provide a valid API key
observation = owm.weather_at_place(misto)
w = observation.get_weather()
temperature=w.get_temperature('celsius')['temp']
print("In " + misto + " misto" + " is the temperature of the air" + " " + str(temperature) + " for the Celsius")
print("In this misto "+ w.get_detailed_status())