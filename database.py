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