import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Baron.951baron",
    database="schooldb"
)

print(mydb)