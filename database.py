import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="aaqib",
    passwd="Aaaqib"
)

print(mydb)
