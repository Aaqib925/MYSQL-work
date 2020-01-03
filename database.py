# dor this i will first import the mysql connector my which i will connect my database by using python

import mysql.connector

# defining a variable which will carry the username and password 

mydb = mysql.connector.connect(
    host="localhost",
    user="aaqib",
    passwd="Aaaqib"
)

# this will show me the address where the user is located in memory

print(mydb)

# in mysql...we need a cursor for our work to be done and queries for the commands

mycursor = mydb.cursor()

# to create a database we execute a querry of CREATE DATABASE inside a cursor exceute function

mycursor.exceute("CREATE DATABASE Firstdatabase")



