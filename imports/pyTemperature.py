import time
from datetime import datetime

class pyTemperature(object):
    def __init__(self, date = datetime.now(), temp=None):
        self.date = date
        self.temperature = temp

    def printTemperature(self):
        print(self.date)
        print(self.temperature)
