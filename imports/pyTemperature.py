import time
from datetime import datetime

class pyTemperature(object):
    def __init__(self, date = datetime.now(), temp=None,pressure=None,humidity=None):
        self.date = date
        self.temperature = temp
        self.pressure = pressure
        self.humidity = humidity


    def printTemperature(self):
        print(self.date)
        print("Temp: ")
        print(self.temperature)
        print("Press: ")
        print(self.pressure)
        print("Humidity: ")
        print(self.humidity)
