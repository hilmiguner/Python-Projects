import pandas as pd

data = pd.read_csv(filepath_or_buffer="Module Pandas/datasets/nba.csv")
data.dropna(inplace=True)  # DELETING NaN VALUES

print(f"Before the change: \n{data.head()}")
data["Name"] = data["Name"].str.upper()
print(f"After the change: \n{data.head()}")
data["Name"] = data["Name"].str.lower()
print(f"After the change: \n{data.head()}")

print(50*"*")

data["Index"] = data.Name.str.find('a')  # Adds a new column which is "Index" and hold the position of 'a' character at "Name".
print(f"New data: \n{data.head()}")

print(50*"*")

boolean_series1 = data.Name.str.contains("jordan")  # Returns a series which holds booleans according to comparison parameter.
print(f"Boolean series: \n{boolean_series1}")

temp1 = data[boolean_series1]  # It gives the only "jordan" rows.
print(f'"jordan" rows: \n{temp1}')

print(50*"*")

temp2 = data.Team.str.replace(" ", "-")  # It replaces the blank with hyphen.
print(temp2)

print(50*"*")

data[['FirstName', 'LastName']] = data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand=True)
print(data)
