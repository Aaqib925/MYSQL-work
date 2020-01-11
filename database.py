# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password")
#
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
#
# now the database is created
#
# now for checking
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")
#
# # since there is no error it means that database is created...
#
# # now i will run some queries for mydatabase...which is are follows
#
# # table query
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")
#
# mycursor = mydb.cursor()
#
# mycursor.execute("CREATE TABLE mydata (name VARCHAR(255), age VARCHAR(255))")
#
# # this will create a table in mydatabase
#
# now for the insert querry
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")
#
# mycursor = mydb.cursor()
#
# sql = "INSERT INTO mydata (name, age) VALUES (%s, %s)"
#
# val = ("Aaqib", "18")
#
# mycursor.execute(sql, val)
#
# mydb.commit()   # this shit very important
#
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
#
# # select querry
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")
#
# mycursor = mydb.cursor()
#
# sql = "SELECT * from mydata"
#
# # sql = "SELECT name from mydata"
#
# # sql = "SELECT age from mydata"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for i in myresult:
# 	print(i)
#
# # for fetching only one row from the database...we use querry of fetchone()
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")
#
# mycursor = mydb.cursor()
#
# sql = "SELECT * from mydata"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchone()
#
# for i in myresult:
# 	print(i)
#
# # to delete the data from the table we use the query delete from
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")
#
# mycursor = mydb.cursor()
#
# sql = "DELETE FROM mydata where age = '18'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# sql = "SELECT * from mydata where age = '10'"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchone()
#
# for i in myresult:
# 	print(i)
#
# # to update the data from the database we use the query of update
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")
#
# mycursor = mydb.cursor()
#
# sql = "UPDATE mydata SET name = 'BWWLA' WHERE name = 'user1'"
#
# mycursor.execute(sql)
#
# mydb.commit()
#
# to delete a record if any record contain same data two
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="mydatabase")
#
# mycursor = mydb.cursor()
#
# # sql = "SELECT * from mydata where age < '11' OR age = '9'"
#
# sql = "SELECT * from mydata where age = '9' and name = 'BWWLA'"
#
# mycursor.execute(sql)
#
# myresult = mycursor.fetchall()
#
# for i in myresult:
# 	print(i)

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="password", database="labtask")

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE labtask")
except mysql.connector.errors.DatabaseError:
    print("This Database already exist.")
try:
    mycursor.execute("CREATE TABLE numbers (Prime int)")
except mysql.connector.errors.ProgrammingError:
    print("This table already exists.")
