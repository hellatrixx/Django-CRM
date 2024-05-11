#install MySQL on machin
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123',
    auth_plugin='mysql_native_password'  # or 'caching_sha2_password' if supported
)

#cursor object
cursorObject = dataBase.cursor()

#create database
cursorObject.execute("CREATE DATABASE db")

print("All done!")