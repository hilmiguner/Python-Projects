import pandas as pd
df = pd.read_csv(filepath_or_buffer="Module Pandas/datasets/imdb.csv")

# 1- Dosya hakkındaki bilgiler.
print(f"1- Dosya hakkındaki bilgiler: \n{df}")

print(50*"*")

# 2- İlk 5 kaydı gösterin.
print(f"2- İlk 5 kaydı gösterin: \n{df.head()}")

print(50*"*")

# 3- İlk 10 kaydı gösterin.
print(f"3- İlk 10 kaydı gösterin: \n{df.head(10)}")

print(50*"*")

# 4- Son 5 kaydı gösterin.
print(f"4- Son 5 kaydı gösterin: \n{df.tail()}")

print(50*"*")

# 5- Son 10 kaydı gösterin.
print(f"5- Son 10 kaydı gösterin: \n{df.tail(10)}")

print(50*"*")

# 6- Sadece Movie_Title kolonunu alın.
result = df["Movie_Title"]
print(f"6- Sadece Movie_Title kolonunu alın: \n{result}")

print(50*"*")

# 7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın.
result = df["Movie_Title"].head()
print(f"7- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın: \n{result}")

print(50*"*")

# 8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın.
result = df[["Movie_Title", "Rating"]].head()
print(f"8- Sadece Movie_Title ve Rating kolonunu içeren ilk 5 kaydı alın: \n{result}")

print(50*"*")

# 9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın.
result = df[["Movie_Title", "Rating"]].tail(7)
print(f"9- Sadece Movie_Title ve Rating kolonunu içeren son 7 kaydı alın: \n{result}")

print(50*"*")

# 10- Sadece Movie_Title ve Rating kolonunu içeren ikinci ilk 5 kaydı alın.
result = df[5:][["Movie_Title", "Rating"]].head()
print(f"10- Sadece Movie_Title ve Rating kolonunu içeren ikinci ilk 5 kaydı alın: \n{result}")

print(50*"*")

# 11- Sadece Movie_Title ve Rating kolonlarını içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesini alın.
result = df[df["Rating"] >= 8].head(50)[["Movie_Title", "Rating"]]
print(f"11- Sadece Movie_Title ve Rating kolonlarını içeren ve imdb puanı 8.0 ve üstünde olan kayıtlardan ilk 50 tanesini alın: \n{result}")

print(50*"*")

# 12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz.
result = df[(df["YR_Released"] == 2014) | (df["YR_Released"] == 2015)]["Movie_Title"]
print(f"12- Yayın tarihi 2014 ile 2015 arasında olan filmlerin isimlerini getiriniz: \n{result}")

print(50*"*")

# 13- Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı 8 ile 9 arasında olan filmleri listeleyiniz.
result = df[(df["Num_Reviews"] > 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))]
print(f"13- Değerlendirme sayısı (Num_Reviews) 100.000 den büyük ya da imdb puanı 8 ile 9 arasında olan filmleri listeleyiniz: \n{result}")