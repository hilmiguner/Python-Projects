import pandas as pd

data = {
    "Column1" : [1, 2, 3, 4, 5],
    "Column2" : [10, 20, 13, 20, 25],
    "Column3" : ["abc", "bcaa", "addre", "cb", "dea"]
}

df = pd.DataFrame(data=data)
print(df)

result = df["Column2"].unique()  # Returns a list of column2 with non-repeated values.
temp = df["Column2"].nunique()  # Returns a number of non-repeated values.
print(f"List of non-repeated values at 'Column2' -> {result} and length of the list -> {temp}")

print(100*"*")

column = df["Column2"]
count = df["Column2"].value_counts()  # Returns a series that holds the number of each value.
print(f"Column: \n{column}\nand number of values: \n{count}")

print(100*"*")

column = df["Column1"]
new_column = df["Column1"] * 2
print(f"Before multiplication: \n{column}\nAfter multiplication with 2: \n{new_column}")

print(100*"*")

def square(x):
    return x * x

column = df["Column1"]
new_column = df["Column1"].apply(square)  # .apply() takes a function and applies it on the selected row or column.

print(f"Before function: \n{column}\nAfter function: \n{new_column}")

print(100*"*")

# Or we can use "lambda" functions.
column = df["Column1"]
new_column = df["Column1"].apply(lambda x: x * x)

print(f"Before lambda function: \n{column}\nAfter lambda function: \n{new_column}")

print(100*"*")

# We can use the .apply() for also string values.
column = df["Column3"]
new_column = df["Column3"].apply(len)

print(f"Before function: \n{column}\nAfter function: \n{new_column}")

print(100*"*")

result = df.sort_values("Column2")  # Sorts the values.
print(f"Dataframe: \n{df}\nDataframe with sorted column: \n{result}")


print(100*"*")

result = df.sort_values("Column2", ascending=False)  # If we change the ascending value to False, 
# it will sort the values from the biggest to the lowest.
print(f"Dataframe: \n{df}\nDataframe with sorted column: \n{result}")

print(100*"*")

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data=data)
print(df)

pivot_table1 = df.pivot_table(index="Ay", columns="Kategori", values="Gelir")
print(pivot_table1)
