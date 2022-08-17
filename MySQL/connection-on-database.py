import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="mydatabase"
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
except mysql.connector.errors.ProgrammingError as err:
    if err.errno == 1050:
        print("Can't create the table which named 'customer' because there is a table already exists by the same name.")