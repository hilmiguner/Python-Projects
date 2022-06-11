# 1- Gönderilen bir kelimeyi belirtilen kez ekranda yazdırmak.
def func1(kelime,tekrar):
    print(f"{kelime}\n"*tekrar)
func1("Hilmi",6)

print("-"*100)

# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çevirir.
def func2(*a):
    list1 = []
    for i in a:
        list1.append(i)
    print(list1)
func2(1,2,4,"hilmi")

print("-"*100)

# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyon yazınız.
def func3(a,b):
    list2 = []
    for k in range(a,b+1):
        a = False
        for i in range(2, (int(k / 2)) + 1):
            if k % i == 0:
                a = False
                break
            else:
                a = True
        if a == True:
            list2.append(k)
    return list2
print(func3(5,17))

print("-"*100)

# 4- Kendisine gönderilen sayının tam bölenlerini gösteren listeyi ekrana yazdıran fonksiyon yazınız.
def func4(a):
    list3 = []
    for i in range(1,int((a/2))+1):
        if a % i == 0:
            list3.append(i)
    return list3
print(func4(256))