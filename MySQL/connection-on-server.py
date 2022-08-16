import errno
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Baron.951baron",
)

mycursor = mydb.cursor()

try: 
    mycursor.execute("CREATE DATABASE mydatabase")  # Creating new database.
except mysql.connector.errors.DatabaseError as err:
    if err.errno == 1007:
        print("Can't create a new database, database already exists.")

mycursor.execute("SHOW DATABASES")  # Cursor is on the databases now.

for db in mycursor:
    print(db)