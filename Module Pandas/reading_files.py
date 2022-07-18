import pandas as pd

# Reading .csv
df1 = pd.read_csv("Module Pandas/datasets/nba.csv")
print(df1)

print(50*"*")

# Reading .json
df2 = pd.read_json("Module Pandas/datasets/grades.json")
print(df2)