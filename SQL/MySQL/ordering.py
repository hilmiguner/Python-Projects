import mysql.connector

def getAllProductsByOrder(column: str):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM products ORDER BY {column}")  # Gets all rows from products table ordering by the name column.
    result = cursor.fetchall()   
    
    for product in result:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")

def getAllProductsByReverseOrder(column: str):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM products ORDER BY {column} DESC")  # Only difference is the DESC keyword.
    result = cursor.fetchall()
    
    for product in result:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")

def getAllProductsByOrders(*columns):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    txt = ",".join(columns)

    cursor.execute(f"SELECT * FROM products ORDER BY {txt}")  # Only difference is the DESC keyword.
    result = cursor.fetchall()
    
    for product in result:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")

def func():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    cursor.execute(f"SELECT * FROM products ORDER BY name DESC, id DESC")  # Only difference is the DESC keyword.
    result = cursor.fetchall()
    
    for product in result:
        print(f"ID: {product[0]}, Name: {product[1]}, Price: {product[2]}")

# getAllProductsByOrder("name")
# getAllProductsByOrder("price")
# getAllProductsByOrder("id")

# getAllProductsByReverseOrder("name")
# getAllProductsByReverseOrder("price")
# getAllProductsByReverseOrder("id")

# getAllProductsByOrders("name", "id")
func()