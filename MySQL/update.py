import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="node-app"
)

cursor = connection.cursor()

sql = "UPDATE products SET name='Samsung S8' WHERE id=3 or id=5"
cursor.execute(sql)
try:
    connection.commit()
    print(f"{cursor.rowcount} registry has been added to table.")
except mysql.connector.errors.Error as err:
    print("Error ->", err)
finally:
    connection.disconnect()
    print("Database connection is disconnected.")