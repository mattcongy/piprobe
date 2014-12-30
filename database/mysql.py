# mySQL data persistance of temperature
import pymysql
# -*- coding: utf-8 -*-

# your mysql database should have all tables loaded.

mysql_host   = '192.168.1.151'
mysql_user   = 'ownserve'
mysql_passwd = 'Ownserve1303$'
mysql_db     = 'mysql'


#def initMySQLDatabase():
#  conn = pymysql.connect(host=mysql_host, unix_socket='/tmp/mysql.sock', user=mysql_user, passwd=mysql_passwd, db=mysql_db)
"""Init script
CREATE  TABLE `temperature`.`temperatures` (
  `idtemperatures` DATETIME NOT NULL ,
  `temperaturescol` FLOAT NULL ,
  PRIMARY KEY (`idtemperatures`) );
"""

def saveTempToMySQL(temperature):
    conn = pymysql.connect(host=mysql_host, unix_socket='/tmp/mysql.sock', user=mysql_user, passwd=mysql_passwd, db=mysql_db)

    cur = conn.cursor()
    sql_string = "INSERT INTO temperature.temperatures VALUES ('{date}',{temp})"
    sql_formatted = sql_string.format(date=temperature.date,temp=temperature.temperature)
    print(sql_formatted)
    cur.execute(sql_formatted)

    # print cur.description
    # r = cur.fetchall()
    # print r
    # ...or...
#    for r in cur:
#       print(r)

    cur.close()
    conn.commit()
    conn.close()


