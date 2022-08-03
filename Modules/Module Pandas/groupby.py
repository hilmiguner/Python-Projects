import pandas as pd

personeller = {
    'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
    'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
    'Yaş': [30,25,45,50,23,34,42],
    'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
    'Maaş': [5000,3000,4000,3500,2750,6500,4500]
}

df = pd.DataFrame(data=personeller)
print(df)
result = df["Maaş"].sum()
print(f"Sum of the salaries -> {result}")

print(50*"*")

# For grouping we use .groupby().
print(f"Columns -> {df.columns}")
groupby_obj1 = df.groupby("Departman")
print(f"Groupby object -> {groupby_obj1}")
print(f"Groups -> {groupby_obj1.groups}")

print(50*"*")

groupby_obj2 = df.groupby(["Departman", "Semt"])
print(f"Another groupby object -> {groupby_obj2}")
print(f"Groups -> {groupby_obj2.groups}")

print(50*"*")

groupby_obj3 = df.groupby("Semt")
print(f"Another groupby object -> {groupby_obj3}")
for name, group in groupby_obj3:
    print(f"Group name -> {name}")
    print(f"Group: \n{group}")

print(50*"*")

for name, group in df.groupby("Departman"):
    print(f"Group name -> {name}")
    print(f"Group: \n{group}")

print(50*"*")

result = df.groupby("Semt").get_group("Kadıköy")
print(f"Group that it's 'Semt' is 'Kadıköy': \n{result}")

print(50*"*")

result = df.groupby("Departman").get_group("Muhasebe")
print(f"Group that it's 'Departman' is 'Muhasebe': \n{result}")

print(50*"*")

result = df.groupby("Departman").mean()
print(f"Mean of the group by 'Departman': \n{result}")

print(50*"*")

result = df.groupby("Departman")["Maaş"].mean()
print(f"Salary mean of the group by 'Departman': \n{result}")

print(50*"*")

result = df.groupby("Semt")["Yaş"].mean()
print(f"Age mean of the group by 'Semt': \n{result}")

print(50*"*")

result = df.groupby("Semt")["Maaş"].mean()
print(f"Salary mean of the group by 'Semt': \n{result}")

print(50*"*")

result = df.groupby("Semt")["Çalışan"].count()
print(f"Employee number of the group by 'Semt': \n{result}")

print(50*"*")

result = df.groupby("Departman")["Yaş"].max()
print(f"Maximum age of the group by 'Departman': \n{result}")

print(50*"*")

result = df.groupby("Departman")["Maaş"].min()
print(f"Minimum salary of the group by 'Departman': \n{result}")

print(50*"*")

result = df.groupby("Departman")["Maaş"].max()
print(f"Maximum salary of the group by 'Departman': \n{result}")

print(50*"*")

result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]
print(f"Maximum salary of 'Muhasebe' in the group by 'Departman': \n{result}")

print(50*"*")

import numpy as np
result = df.groupby("Departman").agg(np.mean)  # .agg() can take numpy methods.
print(f"Mean by Numpy: \n{result}")

print(50*"*")

result = df.groupby("Departman")["Maaş"].agg([np.sum, np.mean, np.max, np.min])
print(f"Salary data by Numpy: \n{result}")
