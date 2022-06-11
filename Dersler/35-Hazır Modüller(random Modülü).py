import random

number = random.random()  # 0.0 ile 1.0 arasında bir değer seçecek ve bu değeri "number" adlı değişkene atayacak.
print(f"Rastgele ondalık sayı = {number}")
print(50*"-")

# Değer aralığını değiştirmek istersek uniform() fonksiyonunu kullanabiliriz.
number = random.uniform(1, 100)  # 1.0 - 100.0 (1.0 ve 100.0 dahil)
print(f"1.0 ile 100.0 değer aralığından rastgele bir ondalık sayı = {number}")
print(50*"-")

# Çıktıya verilen sayıların ondalık sayılar olduğunu farketmişsinizdir. Ondalık sayı yerine tam sayı istiyorsak
# randint() fonksiyonunu kullanacağız.
number = random.randint(1, 100)  # 1 - 100 (1 ve 100 dahil)
print(f"1 ile 100 değer aralığından rastgele bir tam sayı = {number}")
print(50*"-")

# Bir listenin elemanlarından birini rastgele seçmek istersek;
list1 = ["Hilmi", "Ahmet", "Mehmet", "Batu"]
randVar = list1[random.randint(0, len(list1)-1)]
print(randVar)
print(50*"-")

# Bunları yapmak yerine;
randVar = random.choice(list1)
print(randVar)
print(50*"-")

# Sadece listelerde değil, string ifadelerdede kullanabiliyoruz.
selam = "Selamın aleyküm"
randVar = random.choice(selam)
print(randVar)
print(50*"-")

# Bir listeyi rastgele karıştırmak istersek shuffle() fonksiyonunu kullanabiliriz.
print(f"Karıştırmadan önce;\n{list1}")
random.shuffle(list1)
print(f"Karıştırdıktan sonra;\n{list1}")
print(50*"-")

# Peki seçeceğimiz değerlerin adet sayısını arttırmak istersek ne yapacağız ?
randVar = random.sample(list1, 2)  # list1 adlı listeden 2 tane rastgele eleman seç ve
# onları başka bir liste haline getir.
print(randVar)
print(50*"-")

randVar = random.sample(selam, 5)
print(randVar)
print(50*"-")
