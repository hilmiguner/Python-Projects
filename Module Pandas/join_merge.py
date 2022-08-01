import pandas as pd

customers = {
    'CustomerId': [1, 2, 3, 4],
    'FirstName': ["Ahmet", "Ali", "Hasan", "Canan"],
    'LastName': ["Yılmaz", "Korkmaz", "Çelik", "Toprak"]
}

orders = {
    'OrderId': [10, 11, 12, 13],
    'CustomerId': [1, 2, 5, 7],
    'OrderDate': ['2010-07-04', '2010-08-04', '2010-07-07', '2012-07-04']
}

df_customers = pd.DataFrame(data=customers)
df_orders = pd.DataFrame(data=orders)

result = pd.merge(df_customers, df_orders, how="inner")

print(" CUSTOMERS ".center(100, "*"))
print(df_customers)
print(" ORDERS ".center(100, "*"))
print(df_orders)
print(" INNER JOINT ".center(100, "*"))
print(result)

print(100*"*")

result = pd.merge(df_customers, df_orders, how="left")

print(" CUSTOMERS ".center(100, "*"))
print(df_customers)
print(" ORDERS ".center(100, "*"))
print(df_orders)
print(" LEFT JOINT ".center(100, "*"))
print(result)

print(100*"*")

result = pd.merge(df_customers, df_orders, how="right")

print(" CUSTOMERS ".center(100, "*"))
print(df_customers)
print(" ORDERS ".center(100, "*"))
print(df_orders)
print(" RIGHT JOINT ".center(100, "*"))
print(result)

print(100*"*")

result = pd.merge(df_customers, df_orders, how="outer")

print(" CUSTOMERS ".center(100, "*"))
print(df_customers)
print(" ORDERS ".center(100, "*"))
print(df_orders)
print(" OUTER JOINT ".center(100, "*"))
print(result)

print(100*"*")

customersA = {
    'CustomerId': [1, 2, 3, 4],
    'FirstName': ["Ahmet", "Ali", "Hasan", "Canan"],
    'LastName': ["Yılmaz", "Korkmaz", "Çelik", "Toprak"]
}

customersB = {
    'CustomerId': [4, 5, 6, 7],
    'FirstName': ["Yağmur", "Çınar", "Cengiz", "Can"],
    'LastName': ["Bilge", "Turan", "Yılmaz", "Turan"]
}

df_customersA = pd.DataFrame(data=customersA)
df_customersB = pd.DataFrame(data=customersB)

result = pd.concat([df_customersA, df_customersB])
print(f"According to axis is zero: \n{result}")
result = pd.concat([df_customersA, df_customersB], axis=1)
print(f"According to axis is one: \n{result}")