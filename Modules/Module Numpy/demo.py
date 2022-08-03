from turtle import pos
import numpy as np

# 1- (10, 15, 30, 45, 60) değerlerine sahip numpy dizisi oluşturunuz.
arr1 = np.array([10, 15, 30, 45, 60])
print(arr1)

print(50*"*")

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturunuz.
arr2 = np.arange(5, 15)
print(arr2)

print(50*"*")

# 3- (50-100) arasında 5'er 5'er artarak numpy dizisi oluşturunuz.
arr3 = np.arange(50, 100, 5)
print(arr3)

print(50*"*")

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturunuz.
arr4 = np.zeros(10)
print(arr4)

print(50*"*")

# 5- 10 elemenalı birlerden oluşan bir dizi oluşturunuz.
arr5 = np.ones(10)
print(arr5)

print(50*"*")

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.
arr6 = np.linspace(0, 100, 5)
print(arr6)

print(50*"*")

# 7- (10-30) arasında rastgele 5 tane tam sayı üretin.
arr7 = np.random.randint(10, 30, 5)
print(arr7)

print(50*"*")

# 8- [-1 ile 1] arasında 10 adet sayı üretin.
arr8 = np.random.randn(10)
print(arr8)

print(50*"*")

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturunuz.
arr9 = np.random.randint(10, 50, 15).reshape(3, 5)
print(arr9)

print(50*"*")

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.
sum_row = arr9.sum(axis=1)
sum_column = arr9.sum(axis=0)
print(f"Satır toplamı -> {sum_row}")
print(f"Sütun toplamı -> {sum_column}")

print(50*"*")

# 11- Üretilen matrisin en büyük, en küçük ve ortalaması nedir ?
max = arr9.max()
min = arr9.min()
mean = arr9.mean()
print("Max değer ->", max)
print("Min değer ->", min)
print("Ortalama değer ->", mean)

print(50*"*")

# 12- Üretilen matrisin en büyük değerinin indisi kaçtır ?
index1 = arr9.argmax()
print(f"{max} sayısı, {index1}. indistedir.")

print(50*"*")

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elemanını seçiniz.
arr10 = np.arange(10, 20)
print(arr10[:3])

print(50*"*")

# 14- Üretilen dizinin elemanlarını tersten yazınız.
print(arr10[::-1])

print(50*"*")

# 15- Üretilen çok boyutlu matrisin ilk satırını seçin.
print("Matris ->", arr9)
print("İlk satırı ->", arr9[0])

print(50*"*")

# 16- Üretilen çok boyutlu matrisin 2. satır 3. sütunundaki elemanı hangisidir ?
print("Matris ->", arr9)
print("2. satır 3. sütun ->", arr9[1, 2])

print(50*"*")

# 17- Üretilen çok boyutlu matrisin tüm satırlardaki ilk elemanını seçiniz.
print("Matris ->", arr9)
print("Tüm satırlardaki ilk elemenlar ->", arr9[::, 0])

print(50*"*")

# 18- Üretilen çok boyutlu matrisin her bir elemanının karesini alınız.
print("Matris ->", arr9)
print("Karesi alınmış matris ->", arr9**2)

# 19- (-50 ile 50) arasında bir matris oluşturup pozitif çift sayıları seçiniz.
arr11 = np.arange(-50, 50)
positives = arr11[arr11 > 0]
pos_evens = positives[positives % 2 == 0]

print("Matris ->", arr11)
print("Pozitif çift sayılar ->", pos_evens)