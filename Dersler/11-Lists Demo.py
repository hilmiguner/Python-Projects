# 1- "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.

list1 = ["Bmw","Mercedes","Opel","Mazda"]

# 2- Liste kaç elemanlıdır ?

print(len(list1))

# 3- Listenin ilk ve son elemanı nedir ?

print(list1[0],list1[-1])

# 4- 'Mazda' değerini 'Toyota' ile değiştirin.

list1[-1]="Toyota"
print(list1)

# 5- 'Mercedes' listenin bir elemanı mıdır ?

print("Mercedes" in list1)

# 6- Listenin -2. indexindeki değer nedir ?

print(list1[-2])

# 7- Listenin ilk 3 elemanını alınız.

print(list1[:3])

# 8- Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.

list1[-1],list1[-2] = "Toyota","Renault"
print(list1)

# 9- Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.

list1 += ["Audi","Nissan"]
print(list1)

# 10- Listenin son elemanını silin.

del list1[-1]
print(list1)

# 11- Liste elemanlarını tersten yazdırın.

print(list1[::-1])