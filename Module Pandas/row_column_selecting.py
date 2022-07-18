import pandas as pd
from numpy.random import randn

df1 = pd.DataFrame(data=randn(3, 3), index=["A", "B", "C"], columns=["Column1", "Column2", "Column3"])

print(f'Dataframe: \n{df1}')

print(50*"*")

print(f'First column: \n{df1["Column1"]}')

print(50*"*")

print(f'First and second column: \n{df1[["Column1", "Column2"]]}')  # If we want to select more than one column,
# We send a list of column names.

print(50*"*")

# If we want to select a row, we use df1.loc["row", "column"] function.
# For selecting row              -> df1.loc["row"]
# For selecting column           -> df1.loc[:, "column"]
# For selecting specific element -> df1.loc["row", "column"] 

print(f'First row: \n{df1.loc["A"]}')

print(50*"*")

print(f'First column: \n{df1.loc[:, "Column1"]}')

print(50*"*")

print(f'Element at 2. row, 3. column -> {df1.loc["B", "Column3"]}')

print(50*"*")

# Also you can use interval logic in Pandas.
# Unlike the lists, intervals of Pandas series include to endpoints.
print(f'First and third column interval: \n{df1.loc[:, "Column1":"Column3"]}')  

print(50*"*")

# ADDING NEW COLUMN
new_column1 = pd.Series(data=randn(3), index=['A', 'B', 'C'])
df1["Column4"] = new_column1
print(f'New series: \n{df1}')

print(50*"")

new_column2 = pd.Series(data=randn(3), index=['A', 'B', 'C'])
df1.loc[:, "Column5"] = new_column2
print(f'New series: \n{df1}')

print(50*"*")

df1["Column6"] = df1["Column2"] + df1["Column4"]
print(f'New series: \n{df1}')

print(50*"*")

# DELETING A COLUMN
#.drop() returns the series without a specific column.
print(f'Before deleting a column: \n{df1}')
df1 = df1.drop("Column6", axis=1)  # If we don't use redefinition, original series never changes.
print(f'After deleting a column: \n{df1}')
df1.drop("Column5", axis=1, inplace=True)  # But if we change the inplace value to True, 
# changes automatically be apply on original series.
print(f'After deleting a column: \n{df1}')