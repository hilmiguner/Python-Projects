import mysql.connector

def get_product_info():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    # sql = "SELECT COUNT(*) FROM products"  # Tells how many rows in the database.
    # sql = "SELECT AVG(price) FROM products"  # Tells the average value of the selected column.
    # sql = "SELECT SUM(price) FROM products"  # Tells the sum of the selected column.
    # sql = "SELECT MAX(price) FROM products"  # Tells the maximum value of the selected column.
    # sql = "SELECT MIN(price) FROM products"  # Tells the minimum value of the selected column.
    
    # If you want to get the name of the most expensive product, you can use more than one sql syntaxes.
    sql = "SELECT name FROM products WHERE price = (SELECT MAX(price) FROM products)"  

    cursor.execute(sql)
    result = cursor.fetchone()   
    
    print(f"Result: {result[0]}")

get_product_info()