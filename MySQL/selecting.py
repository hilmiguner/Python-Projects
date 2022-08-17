from mysql import connector

def getAllProducts():
    connection = connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")  # Gets all rows from products table.
    result = cursor.fetchall()   
    
    for product in result:
        print(f"Name: {product[1]}")
        print(f"Price: {product[2]}")

def getNameAndPrice():
    connection = connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT name, price FROM products")  # Gets just name and price columns to performance of the processor.
    result = cursor.fetchall()   
    
    for product in result:
        print(f"Name: {product[0]}")
        print(f"Price: {product[1]}")

def getNameAndPriceOneRow():
    connection = connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT name,price FROM products")
    result = cursor.fetchone()   # Difference is fetchone instead of fetchall

    print(f"Name: {result[0]}")
    print(f"Price: {result[1]}")  

# getAllProducts()
# getNameAndPrice()
getNameAndPriceOneRow()