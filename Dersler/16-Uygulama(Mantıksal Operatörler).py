# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

a = int(input("Bir sayı giriniz:"))
print(f"{a} sayısının 0-100 arasında olma durumu: {a > 0 and a < 100}")
print(100*"-")

# 2- Girilen bir sayının pozitif çift sayı olma durumunu kontrol ediniz.

b=int(input("Bir sayı giriniz:"))
print(f"{b} sayısının pozitif çift sayı olma durumu: {b>0 and (b%2 == 0)}")
print(100*"-")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.

email = "hilmi.guner@hotmail.com"
password = "1234"
gEmail = input("Email:")
gPassword = input("Şifre:")
print("Girilen emailin doğru olma durumu:",(gEmail==email),"ve girilen şifrenin doğru olma durumu:",(gPassword==password))
print(100*"-")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

n1 = int(input("SAYI 1 :"))
n2 = int(input("SAYI 2 :"))
n3 = int(input("SAYI 3 :"))

print(f"{n1} sayısının en büyük olma durumu: {(n1>n2 and n1>n3)}")
print(f"{n2} sayısının en büyük olma durumu: {(n2>n1 and n2>n3)}")
print(f"{n3} sayısının en büyük olma durumu: {(n3>n1 and n3>n2)}")
print(100*"-")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalamayı hesaplayınız. Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
#    Ortalama 50 olsa bile final notu en az 50 olmalıdır.
#    Finalden 70 alındığında ortalamanın önemi olmasın.

vize1 = float(input("Birinci vize notunu giriniz: "))
vize2 = float(input("İkinci vize notunu giriniz: "))
final = float(input("Final notunu giriniz: "))
ortalama = (((vize1+vize2)/2)*0.6)+(final*0.4)
isPassed = ((ortalama >= 50) and (final >= 50)) or (final >= 70)
if isPassed == True:
    print("Geçtiniz.")
else:
    print("Kaldınız.")
print(100*"-")

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Herhangi birinin hangi gruba girdiğini aşağıdaki tabloya bakarak görebilirsiniz.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

name = input("Adınızı giriniz:")
mass = float(input("Kilonuzu giriniz:"))
height = float(input("Boyunuzu giriniz(metre formatında yazınız.):"))
x = (mass/(height**2))
if x >= 0 and x <= 18.4:
    print(f"{name} adlı kişinin {x} numaralı vücut indeksine göre kendisi ZAYIF sınıfına girmektedir.")
elif x >= 18.5 and x <= 24.9:
    print(f"{name} adlı kişinin {x} numaralı vücut indeksine göre kendisi NORMAL sınıfına girmektedir.")
elif x >= 25.0 and x <= 29.9:
    print(f"{name} adlı kişinin {x} numaralı vücut indeksine göre kendisi FAZLA KİLOLU sınıfına girmektedir.")
elif x >= 30.0 and x <= 34.9:
    print(f"{name} adlı kişinin {x} numaralı vücut indeksine göre kendisi OBEZ sınıfına girmektedir.")
else:
    print("Geçersiz index.")
print(100*"-")