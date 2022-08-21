import mysql.connector

def get_products():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql1234",
        database="node-app"
    )
    cursor = conn.cursor()

    # sql = "SELECT * FROM products INNER JOIN categories on categories.id=products.categoryId"
    # sql = "SELECT products.name,products.price,categories.name FROM products INNER JOIN categories ON categories.id=products.categoryId"
    # We can change table names.
    sql = "SELECT p.name,p.price,c.name FROM products as p INNER JOIN categories as c ON p.categoryId=c.id"
    cursor.execute(sql)
    try:
        result = cursor.fetchall()
        for product in result:
            print("Name: {}, Price: {}, Category: {}".format(*product))
    except mysql.connector.Error as err:
        print("Error occured ->", err)
    finally:
        conn.disconnect()
        print("Database connection has been disconnected")

get_products()
