# import mysql.connector

# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password")

# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")

# now the database is created

# now for checking

# import mysql.connector

# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")

# since there is no error it means that database is created...

# now i will run some queries for mydatabase...which is are follows

# table query

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE mydata (name VARCHAR(255), age VARCHAR(255))")
