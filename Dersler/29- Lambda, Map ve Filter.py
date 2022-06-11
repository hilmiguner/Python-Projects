def square(a): return a**2
print(square(5))

#Peki ya bir listedeki elemanları fonksiyona sokmak istersek.

list1 = [1,5,9,12]
for i in list1:
    print(square(i))

print("-"*50)

#Bunları yapmamak için bir metodumuz var. map()

print(map(square,list1)) #Bu ifade bize adres verir.
print(list(map(square,list1))) #Biz bu adresi listeye çevirirsek, elemanları görebiliriz.
for i in map(square,list1): #Ya da böylede yapabiliriz.
    print(i)

print("-"*50)

#Fonksiyon tanımladan satır için geçerli fonkisyon yazabiliriz.
result1 = map(lambda a : a ** 2,list1)
print(list(result1))

#Ya da lambdayı bir fonksiyon gibi tanımlayabiliriz.
func1 = lambda a : a ** 2
result2 = map(func1,list1)
print(list(result2))

print("-"*50)

#filter() metodu aynı map() metodu gibi bir liste elemanlarını bir fonksiyon içinde gezdirir ancak filter() metodu,
#bir koşul ile çalışır ve o koşulu True yapan liste elemanlarını return değeri olarak atar.

list2 = [1,5,9,10,6]

func2 = lambda a : a % 2 == 0
print(func2(list2[2])) #Fonksiyonumuz tek değerler içi False değerini alıyor bu sebeple ekrana False değeri çıkar.
print(filter(lambda a : a % 2 == 0 , list2))
print(list(filter(lambda a : a % 2 == 0 , list2))) #Filter metodu iste True değerleri ekrana yazdıran parametreleri bir liste yapar ancak map metodunda olduğu gibi burdada adresi listeye çevirmeliyiz.