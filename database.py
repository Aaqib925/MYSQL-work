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

# import mysql.connector

# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")

# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE mydata (name VARCHAR(255), age VARCHAR(255))")

# this will create a table in mydatabase

# now for the insert querry

# import mysql.connector

# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")

# mycursor = mydb.cursor()

# sql = "INSERT INTO mydata (name, age) VALUES (%s, %s)"

# val = ("Aaqib", "18")

# mycursor.execute(sql, val)

# mydb.commit()   # this shit very important

# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO mydata (name, age) VALUES (%s, %s)"
#
# val = []
#
# for i in range(3):
#     tup = ()
#     tup_list = list(tup)
#     x = input("Enter the name: ")
#     y = input("Enter the age: ")
#     tup_list.append(x)
#     tup_list.append(y)
#     tup = tuple(tup_list)
#     val.append(tup)
#
# mycursor.executemany(sql, val)
#
# mydb.commit()

# select querry

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")

mycursor = mydb.cursor()

sql = "SELECT * from mydata"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for i in myresult:
	print(i)