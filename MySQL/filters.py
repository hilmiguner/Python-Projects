import mysql.connector

def getAllProducts(sql: str):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    cursor.execute(sql)
    result = cursor.fetchall()   
    
    for product in result:
        print(f"ID: {product[0]}")
        print(f"Name: {product[1]}")
        print(f"Price: {product[2]}")

def getProductByID(sql: str, id:int):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    cursor.execute(sql, tuple([id]))
    result = cursor.fetchone()   
    
    print(f"ID: {result[0]}")
    print(f"Name: {result[1]}")
    print(f"Price: {result[2]}")

# sql1 = "SELECT * FROM products WHERE id=1"
# getAllProducts(sql1)

# sql2 = "SELECT * FROM products WHERE name='Samsung S7'"
# getAllProducts(sql2)

# sql3 = "SELECT * FROM products WHERE name='Samsung S8'"
# getAllProducts(sql3)  # There are 2 rows so we can specify the which row we want.

# sql4 = "SELECT * FROM products WHERE name='Samsung S8' and price=5000"
# getAllProducts(sql4)  # There are 2 rows so we can specify the which row we want.

# sql5 = "SELECT * FROM products WHERE name='Samsung S6' or price>=3000"
# getAllProducts(sql5)  # We can use also the or operator.

# sql6 = "SELECT * FROM products WHERE name LIKE '%Samsung%'"  # Starts with str -> str%, ends with str %str and middle of it %str%.
# getAllProducts(sql6)

sql7 = "SELECT * FROM products WHERE id=%s"
getProductByID(sql7, 3)
