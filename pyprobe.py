#!/usr/bin/env python
# Main file.

import sys, getopt, os, datetime
from database import mysql
from pyserial import pySerial


# Version
# x.y.z where
#   x = Release Version
#   y = Evolution Version
#   z = Minor evolution / defect correction

version = "0.01"

class py_probe(object):

    @staticmethod
    def printHelp():
        print("piprobe.py <options>")
        print("Version : ", version)
        print("https://github.com/mattcongy/piprobe")
        print("Options : ")
        print(" -h, --help     : Print help documentation")
        print(" -t, --test     : Get a mock temperature")





    """docstring for pyprobe"""
    def __init__(self):
        super(py_probe, self).__init__()
        self.serial = None
        self.output = "stdout"

    """ test method is only to simulate a temperature. No signal is sent to serial device"""
    def test(self):
        self.serial = pySerial()
        self.serial.mock_getTemperature()


    def setOutput(self,out):
        self.output = out

    def save(self):
        if self.output == "stdout":
            self.serial.temperature.printTemperature()
        elif self.output == "database":
            mysql.saveTempToMySQL(self.serial.temperature)

def main(argv):
       try:

          probe = py_probe()
          opts, args = getopt.getopt(argv,"hto:",["help","test","output="])

       except getopt.GetoptError as err:
          print("An error has occured :",err)
          py_probe.printHelp()
          sys.exit(2)
       for opt, arg in opts:

            if opt in ('-h',"--help"):
                py_probe.printHelp()
                sys.exit()
            elif opt in ('-o', "--output"):
                if (arg in ("stdout", "database", "file")):
                    print("Output accepted : ", arg)
                    probe.setOutput(arg)

                else:
                    print("Ouptut format not recongnized. Accepted value are 'stdout', 'database' or 'file'")


            elif opt in ('-t',"--test"):
                # Load multiples data on database, simulate one month of data (december 2014)

                for days in range(1,31):
                    for hours in range (0,23):
                        dateSet = datetime.datetime(2014,12,days,hours,00,00,00)
                        probe.serial = pySerial()
                        probe.serial.mock_getRandomTemperature(dateSet)
                        probe.save()


                sys.exit()

if __name__ == "__main__":
       main(sys.argv[1:])





