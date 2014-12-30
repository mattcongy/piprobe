piprobe
=======

Temperature Probe Python program on a Rapbserry PI.


# About
This python script get temperature from a prob installed on a Raspberry PI, and send information to differnet output (stdout, database, file)

Databases supported :
 . sqlite

**Warning** : you must have Python 3 or superior installed on your local machine in order to launch this program.
To install it on raspberry pi , please run `sudo apt-get install python3-pip`

# How to use it


# Installation

PyMySQL module is required to save data to Mysql interface.
To install it, please follow instructions :
 1. curl -L https://github.com/PyMySQL/PyMySQL/tarball/pymysql-0.6 | tar xz
 2. cd PyMysql folder
 3. python setup.py install
 4. Remove PyMYSQL folder



# Usage
## Test

To test the solution, you can run a load test. This is not taking value from the probe, put insert in into database/sdtout or file like you set in the arguments of the program.

`python3 pyprobe.py --output=database --test`

** Important ** '--output=' parameter must be set at first level.


## Get value from probe and send to stdout
`python3 pyprobe.py --output=stdout --probe`



