liste = ["1", "2", "5a", "10b", "abc", "10", "50"]

# 1- Liste elemanları içindeki sayısal değerleri bulunuz.

import re

for i in liste:
    if re.search("[0-9]", i) and not re.search("[a-z]", i):
        print(f"Sayısal değer: {i}")

print(50*"-")

# 2- Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz. Aksi halde hata mesajı yazın.

while True:
    girdi = input("Bir değer giriniz: ")
    if girdi == "q":
        break
    try:
        result = int(girdi)
    except ValueError:
        print("Geçersiz sayı.")

print(50*"-")

# 3- Girilen parola içerisinde türkçe karakter hatası veriniz.

turkce_karakterler = "şçğüöıİ"
parola = input("Bir parola giriniz: ")
for i in parola:
    if i in turkce_karakterler:
        raise TypeError("Türkçe karakter girmeyiniz.")
print("Geçerli Parola")

print(50*"-")

# 4- Faktöriyel fonksiyonu oluşturup, gelen değer için hata mesajları verin.

def faktoriyel(x):
    x = int(x)
    if x < 0:
        raise ValueError("Negatif değer girilemez.")
    result1 = 1
    for k in range(1, x+1):
        result1 *= k
    return result1
print(faktoriyel(5))
