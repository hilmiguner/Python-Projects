sayilar = [1,3,5,7,9,12,19,21]

# 1- "sayilar" listesini while döngüsü kullanarak ekrana yazdırı.
i = 0
while i != len(sayilar) :
    print(sayilar[i])
    i += 1
print(100*"-")

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

a = int(input("Birinci sayıyı giriniz:"))
b = int(input("İkinci sayıyı giriniz:"))
i = a+1
while i != b:
    if i % 2 ==1:
        print(i)
    i += 1
print(100*"-")

# 3- 1 ve 100 sayıları arasındaki sayıları azalan şeklinde yazınız.

i=99
while i != 1:
    print(i)
    i -= 1
print(100*"-")

# 4- Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.

list = []
i = 1
while i != 6:
    a = int(input(f"{i}. sayıyı giriniz:"))
    list.append(a)
    i += 1
list.sort()
for k in range(0,len(list)):
    print(list[k])
print(100*"-")

# 5- Kullanıcıdan alacağınız sınırsız ürün bilgisini "urunler" listesi içinde saklayın
# * ürün sayısını kullanıcıya sorun.
# ** dictionary listesi yapısı (name,price) şeklinde olsun.
# *** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.

num = int(input("Kaç tane ürün gireceksiniz:"))
list1 = []
x=0
while x < num:
    list1.append({"name":(input(f"{x+1}. ürünün ismini giriniz.")),"price":input(f"{x+1}. ürünün fiyatını giriniz:")})
    x += 1
x = 0
while x != num:
    print(f"{list1[x]['name']} adlı ürünün fiyatı {list1[x]['price']} türk lirasıdır.")
    x += 1
print(100*"-")