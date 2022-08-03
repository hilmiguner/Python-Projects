import pandas as pd

df = pd.read_csv(filepath_or_buffer="Module Pandas/datasets/nba.csv")

# 1- İlk 10 kaydı getiriniz.
print(f"1- İlk 10 kaydı getiriniz. \n{df.head(10)}")

print(100*"*")

# 2- Toplam kaç kayıt vardır ?
print(f"2- Toplam kaç kayıt vardır -> {df.index.size}")

print(100*"*")

# 3- Tüm oyuncuların toplam maaş ortalaması nedir ?
result = df["Salary"].mean()
print(f"3- Tüm oyuncuların toplam maaş ortalaması nedir -> {result}")

print(100*"*")

# 4- En yüksek maaşı ne kadardır ?
result = df["Salary"].max()
print(f"4- En yüksek maaşı ne kadardır -> {result}")

print(100*"*")

# 5- En yüksek maaşı alan oyuncu kimdir ?
result = df[df["Salary"] == df["Salary"].max()]["Name"].iloc[0]
print(f"5- En yüksek maaşı alan oyuncu kimdir -> {result}")

print(100*"*")

# 6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz.
result = df[(df["Age"] < 25) & (df["Age"] > 20)][["Name", "Team", "Age"]].sort_values(by="Age", ascending=False)
print(f"6- Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı getiriniz. \n{result}")

print(100*"*")

# 7- "John Holland" isimli oyuncunun oynadığı takım hangisidir ?
result = df[df["Name"] == "John Holland"]["Team"].iloc[0]
print(f"7- 'John Holland' isimli oyuncunun oynadığı takım hangisidir -> {result}")

print(100*"*")

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
result = df.groupby("Team")["Salary"].mean()
print(f"- Takımlara göre oyuncuların ortalama maaş bilgisi nedir: \n{result}")

print(100*"*")

# 9- Kaç farklı takım mevcut ?
result = len(df.groupby("Team").groups)
result = df["Team"].nunique()
print(f"9- Kaç farklı takım mevcut -> {result}")

print(100*"*")

# 10- Her takımda kaç oyuncu oynamaktadır ?
result = df["Team"].value_counts()
print(result)

print(100*"*")

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df.dropna(inplace=True)
result = df[df["Name"].str.contains("and")]
print(result)