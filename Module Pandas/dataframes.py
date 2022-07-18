from operator import iconcat
import pandas as pd

s1 = pd.Series([3, 2, 0, 1])
s2 = pd.Series([0, 3, 7, 2])

dict1 = dict(apples = s1, oranges = s2)
print(f"Dictionary: \n{dict1}")
dataframe1 = pd.DataFrame(dict1)
print(f"Dataframe: \n{dataframe1}")

print(50*"*")

data1 = [["Ahmet", 50], ["Ali", 60], ["Yağmur", 70], ["Çınar", 80]]
dataframe2 = pd.DataFrame(data= data1)
print(f"Dataframe: \n{dataframe2}")

index1 = [1, 2, 3, 4]
columns1 = ["Name", "Mark"]
dataframe3 = pd.DataFrame(data=data1, index=index1, columns=columns1)
print(f"Dataframe with specific columns and indexes: \n{dataframe3}")

print(50*"*")

# Instead of using the list as a data type, we can use dictionaries.
dict2 = {"Name" : ["Ahmet", "Ali", "Yağmur", "Çınar"], "Mark": [50, 60, 70, 80]}
index2 = ["212", "232", "236", "456"]  # Student numbers.
dataframe4 = pd.DataFrame(data=dict2, index=index2)
print(f"Dataframe: \n{dataframe4}")

print(50*"*")

# Or instead of using the dictionaries as a data type, we can use dictionary list.
dict_list1 = [
    {"Name": "Ahmet", "Mark": 50},
    {"Name": "Ali", "Mark": 60},
    {"Name": "Yağmur", "Mark": 70},
    {"Name": "Çınar", "Mark": 80}
]
dataframe5 = pd.DataFrame(data=dict_list1)
print(f"Dataframe: \n{dataframe5}")