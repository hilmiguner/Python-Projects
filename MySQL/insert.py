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

list = []
result = "Evet"
while result != "Hayır" and result != "hayır":
    name = input("Ürün adı:")
    price = float(input("Ürün fiyatı:"))
    imageUrl = input("Ürün resim adı:")
    description = input("Ürün açıklaması:")

    list.append((name, price, imageUrl, description))

    result = input("Devam etmek istiyor musunuz (Evet/Hayır):")
    print(50*"*")

insertProducts(list)
