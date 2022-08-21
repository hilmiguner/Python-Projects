import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql1234",
    database="node-app"
)

cursor = connection.cursor()

sql = "DELETE FROM products WHERE id=6"
cursor.execute(sql)
try:
    connection.commit()
    print(f"{cursor.rowcount} registry has been deleted from table.")
except mysql.connector.errors.Error as err:
    print("Error ->", err)
finally:
    connection.disconnect()
    print("Database connection is disconnected.")