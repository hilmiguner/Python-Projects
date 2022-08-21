import sqlite3

connection = sqlite3.connect("SQL/SQLite/node-app.db")
cursor = connection.cursor()

sql = "SELECT * FROM products"
cursor.execute(sql)
try:
    products = cursor.fetchall()
    for product in products:
        print("ID: {}, Name: {}, Price: {}".format(*product))
except sqlite3.Error as err:
    print("Error has been occured ->", err)
finally:
    connection.close()
    print("Connection with database has succesfully disconnected.")