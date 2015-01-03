#!/usr/bin/env python
# Get External Temperature from OpenWeatherMap
# External informations are :
# - temperature
# - humidity
# - pressure
# - precipitation volume (each 3h)

import urllib.request
import json
import pyowm
from datetime import datetime

from pyserial import pySerial
from imports.pyTemperature import pyTemperature
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q="
DEFAULT_CITY = "Meyreuil, France"
API_KEY = "4ca5e2bebb63f72d4cc5564300cf68d5"


class py_external(object):
    def __init__(self):
        super(py_external, self).__init__()
        self.pyTemperature = None


    def getDataAPI(self):
        owm = pyowm.OWM(API_KEY)
        #observation = owm.weather_at_place(DEFAULT_CITY,'accurate')
        observation = owm.weather_at_id(2994068)
        print(observation)
        if observation is not None:

            w = observation.get_weather()

            w_temp = w.get_temperature(unit='celsius')
            w_hum  = w.get_humidity()
            w_pres = w.get_pressure()
            w_prec = w.get_rain()
            #print(w_prec)
            l = observation.get_location()
            #print(l.get_ID())
            #print(l.get_name())
            #print(l.get_lat())
            #print(l.get_lon())

            #pyTemperature Constructor (self, date = datetime.now(), temp=None,pressure=None,humidity=None,precicipationVol=None):
            dateNow = datetime.now()
            self.pyTemperature = pyTemperature(dateNow,w_temp['temp'],w_pres['press'],w_hum)
            #print("Temperature at pyExternal")
            #self.pyTemperature.printTemperature()



    def getPyTemperature(self):
        return self.pyTemperature

    def setDate(self,newDate):
        self.date = newDate

    def setPressure(self,newPressure):
        self.pressure = newPressure

    def setHumidity(self,newHumidity):
        self.humidity = newHumidity



