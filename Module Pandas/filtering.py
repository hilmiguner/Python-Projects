import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 75).reshape(15, 5)
df = pd.DataFrame(data=data, columns=["Column1", "Column2", "Column3", "Column4", "Column5"])
print(f"Dataframe: \n{df}")

print(50*"*")

print(f"Columns -> {df.columns}")
print(f"First 5 rows: \n{df.head()}")  # .head() returns first 5 rows.
print(f"First 10 rows: \n{df.head(10)}")  # .head() also can get parameter.
print(f"Last 5 rows: \n{df.tail()}")  # .tail() returns last 5 rows.
print(f"Last 10 rows: \n{df.tail(10)}")  # .tail() also can get parameter.

print(50*"*")

temp = df["Column1"].head()
print(f"First 5 row of the first column: \n{temp}")

print(50*"*")

print(f"Numbers of bigger than 50: \n{df[df > 50]}")

print(50*"*")

print(f"Numbers of even ones: \n{df[df % 2 == 0]}")

print(50*"*")

bool_series = df["Column1"] > 50
result = df[bool_series]["Column1"]  # df[bool_series] returns all columns so we need to specify which column we need.
print(result)

print(50*"*")

result = df[(df['Column1'] > 50) & (df['Column1'] <= 70)]["Column1"]
print(f"Dataframe: \n{df}")
print(f"Numbers that are bigger than 50 and less than 70 in first column: \n{result}")

print(50*"*")

# For filtering we can use .query(conditions) instead of df[conditions].
result = df.query("Column1 > 50 | Column1 % 2 == 0")["Column1"]
print(f"Numbers that are bigger than 50 or evens in first column: \n{result}")