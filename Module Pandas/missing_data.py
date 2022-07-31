import re
import pandas as pd
import numpy as np

data = np.random.randint(10, 100, 15).reshape(5, 3)
df = pd.DataFrame(data=data, index=['a', 'c', 'e', 'f', 'h'], columns=["Column1", "Column2", "Column3"])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
result = df

print(f"Dataframe: \n{result}")

print(50*"*")

# DELETING ROWS AND COLUMNS
result = df.drop("Column1", axis=1)
print(f"New dataframe: \n{result}")

print(50*"*")

result = df.drop(["Column1", "Column2"], axis=1)
print(f"New dataframe: \n{result}")

print(50*"*")

result = df.drop('a', axis=0)
print(f"New dataframe: \n{result}")

print(50*"*")

result = df.drop(['a', 'b', 'h'], axis=0)
print(f"New dataframe: \n{result}")

print(50*"*")

# FINDING NaN (Not a Number) VALUES
bool_series1 = df.isnull()  # NaN values will be changed to True, others will be changed to False.
print(f"Boolean series that NaN values are True: \n{bool_series1}")

print(50*"*")

bool_series2 = df.notnull()  # NaN values will be changed to False, others will be changed to True.
print(f"Boolean series that NaN values are False: \n{bool_series2}")

print(50*"*")

# Getting how many NaN values at the columns, we use df.isnull().sum()
result = df.isnull().sum()
print(f"How many NaN values at the columns: \n{result}")

print(50*"*")

result = df["Column1"].isnull().sum()
print(f"Total NaN values number at Column1 -> {result}")

print(50*"*")

# If we look at the series we can see the all 3 NaN values are at the same row.
# So we are going to add another column to not fit that system.

new_column = [np.nan, 30, np.nan, 51, np.nan, 30, np.nan, 10]
df["Column4"] = new_column  # ADDING NEW COLUMN
result = df

print(f"New dataframe: \n{result}")

print(50*"*")

# Getting NaN values at Column1.
result = df[df["Column1"].isnull()]["Column1"]
print(f"NaN values at Column1: \n{result}")

print(50*"*")

# Getting valid values at Column1.
result = df[df["Column1"].notnull()]["Column1"]
print(f"Valid values at Column1: \n{result}")

print(50*"*")

print(f"Dataframe: \n{df}")
# df.dropna() deletes a row or a column which has at least one NaN value. 
result = df.dropna()  # Default axis value is 0 which means it deletes rows by default.
print(f"New dataframe: \n{result}")

result = df.dropna(axis=1)  # There is no column without NaN value so new dataframe is going to be empty.
print(f"New dataframe: \n{result}")

print(50*"*")

result = df.dropna(how="any")  # how="any" is the default value so it deletes every row with at least one NaN value.
result = df.dropna(how="all")  # If we put "all" to how parameter, it just deletes the rows with all of the elements are NaN.
# But as you can see there is no row that fits that rule.
print(result)

print(50*"*")

result = df.dropna(subset=["Column1", "Column2"], how="all")  # If we just interest with specific columns,
# we use subset parameter.
print(result)

print(50*"*")

result = df.dropna(thresh=3)  # If there are 3 or more than 3 valid values, .dropna() does not deletes the rows or columns.
print(result)

print(50*"*")

result = df.dropna(thresh=4)
print(result)

print(50*"*")

# FILLING THE NAN VALUES
result = df.fillna(value="No Input")
print(f"Dataframe that filled by specific value: \n{result}")

print(50*"*")

result = df.fillna(value=1)
print(f"Dataframe that filled by specific value: \n{result}")

print(50*"*")

result = df.sum()  # Gets the sum of the every column.
print(f"Sum of the every column: \n{result}")

result = df.sum().sum()  # Gets the sum of the whole series.
print(f"Sum of the whole series -> {result}")

result = df.notnull().sum().sum()  # Gets how many valid values inside of the series.
print(result)

print(50*"*")

def avg(df:pd.DataFrame):
    size = df.notnull().sum().sum()
    sum = df.sum().sum()
    return sum/size

result = df.fillna(value=avg(df))
print(f"Before filling: \n{df}")
print(f"After filling: \n{result}")
