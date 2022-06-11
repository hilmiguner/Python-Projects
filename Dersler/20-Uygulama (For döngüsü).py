sayilar = [1,3,5,7,9,12,19,21]

# 1- "sayilar" listesindeki hangi sayılar 3'ün katıdır ?

for i in sayilar:
    if i%3==0:
        print(i)
print(100*"-")

# 2- "sayilar" listesindeki sayıların toplamı nedir ?

temp = 0
for i in sayilar:
    temp += i
print("Sayıların toplamı:",temp)
print(100*"-")

# 3- "sayilar" listesindeki tek sayıların karesini alınız.

for i in sayilar:
    if i%2==1:
        print(f"{i}'nin karesi:",i**2)
print(100*"-")

sehirler = ["kocaeli","istanbul","ankara","izmir","rize"]

# 4- "sehirler" adlı listedeki şehirlerden hangileri en fazla 5 karakterlidir ?

for i in sehirler:
    if len(i)<=5:
        print(i)
print(100*"-")

urunler = [
    {"name":"samsung S6","price":"3000"},
    {"name":"samsung S7","price":"4000"},
    {"name":"samsung S8","price":"5000"},
    {"name":"samsung S9","price":"6000"},
    {"name":"samsung S10","price":"7000"},
]

# 5- Ürünlerin fiyatları toplamı nedir ?

temp=0
for i in range(0,len(urunler)):
    for k in urunler[i]:
        if k=="price":
            temp += int(urunler[i][k])
print("Toplam fiyat:",temp)
print(100*"-")

# 6- Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.

for i in urunler:
    if int(i["price"]) <=5000:
        print(i["name"])
print(100*"-")