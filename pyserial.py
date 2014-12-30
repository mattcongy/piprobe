# pyserial.py
# --------------------------------
# DESCRIPTION :
#   pyserial module gets information from serial port and return value

from imports.pyTemperature import pyTemperature
import random

class pySerial(object):
    def __init__(self):
        super(pySerial, self).__init__()
        self.temperature = None

    def mock_getTemperature(self):
        self.temperature = pyTemperature(None,12.3)

    def mock_getRandomTemperature(self,dateTemp):
        randomTemp = random.uniform(0, 30)
        self.temperature = pyTemperature(dateTemp,randomTemp)
