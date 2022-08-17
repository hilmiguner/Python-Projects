import mysql.connector

def insertProduct(name, price, imageUrl, description):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = (name, price, imageUrl, description)

    cursor.execute(sql, values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın ID: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata", err)
    finally:
        connection.close()
        print("Database bağlantısı kesildi.")

def insertProducts(productList):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    sql = "INSERT INTO products(name, price, imageUrl, description) VALUES (%s, %s, %s, %s)"
    values = productList

    cursor.executemany(sql, values)
    try:
        connection.commit()
        print(f"{cursor.rowcount} tane kayıt eklendi.")
        print(f"Son eklenen kaydın ID: {cursor.lastrowid}")
    except mysql.connector.Error as err:
        print("Hata", err)
    finally:
        connection.close()
        print("Database bağlantısı kesildi.")

def getProducts():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM products")  # Get all rows from products table.
    result = cursor.fetchall()   
    print(result)

getProducts()