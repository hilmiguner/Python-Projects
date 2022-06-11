# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#    Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise ya da üniversite olmalıdır.

name = input("Please enter your name:")
age = int(input("Please enter your age:"))
education_situation = input("Please enter your education situation:")

if age >= 18 and (education_situation == "highschool" or education_situation == "university"):
    print(f"Person named {name} can get a driver's license.")
else:
    print(f"Person named {name} can't get a driver's license")

print(100*"-")

# 2- Bir öğrencinin 2 yazılı, 1 sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık gelen not bilgisini yazdırınız.
#    0-24    => 0
#    25-44   => 1
#    45-54   => 2
#    55-69   => 3
#    70-84   => 4
#    85-100  => 0

note1 = float(input("Birinci yazılı notunuzu giriniz:"))
note2 = float(input("İkinci yazılı notunuzu giriniz:"))
note3 = float(input("Sözlü notunuzu giriniz:"))

ortalama = (note1+note2+note3)/3

if ortalama >= 0 and ortalama <= 24:
    print(f"Ortalamanız {ortalama} olduğu için aldığınız not bilgisi 0.")
elif ortalama >= 25 and ortalama <= 44:
    print(f"Ortalamanız {ortalama} olduğu için aldığınız not bilgisi 1.")
elif ortalama >= 45 and ortalama <= 54:
    print(f"Ortalamanız {ortalama} olduğu için aldığınız not bilgisi 2.")
elif ortalama >= 55 and ortalama <= 69:
    print(f"Ortalamanız {ortalama} olduğu için aldığınız not bilgisi 3.")
elif ortalama >= 70 and ortalama <= 84:
    print(f"Ortalamanız {ortalama} olduğu için aldığınız not bilgisi 4.")
elif ortalama >= 85 and ortalama <= 100:
    print(f"Ortalamanız {ortalama} olduğu için aldığınız not bilgisi 5.")
else:
    print("Ortalamayı geçersiz kılan notlar girdiniz !!")

print(100*"-")

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. Yıl
#    2. Bakım => 2. Yıl
#    3. Bakım => 3. Yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.
#    *** datetime modülünü kullanmanız gerekiyor.

from datetime import datetime
date = input("Aracın trafiğe çıkış tarihini aralarında boşluk bırakacak şekilde gün ay yıl olarak yazınız.(örnek 15 02 2001):")
day , month , year = date.split()
fark = (datetime.now() - datetime(int(year),int(month),int(day))).days
print(fark)
if fark // 365 == 0:
    print("Trafiğe çıkış süreniz 1 yılı tamamlamadığı için bakım süreniz daha gelmemiştir.")
elif fark // 365 == 1:
    print("Trafiğe çıkış süreniz 1 yılı tamamladığı için 1. bakımınz gelmiştir.")
elif fark // 365 == 2:
    print("Trafiğe çıkış süreniz 2 yılı tamamladığı için 2. bakımınz gelmiştir.")
elif fark // 365 == 3:
    print("Trafiğe çıkış süreniz 3 yılı tamamladığı için 3. bakımınz gelmiştir.")
else:
    print("Trafiğe çıkış süreniz ya 4 yıl ya da 4 yılı geçtiği için daha fazla bakım yapamamaktayız.")
print(100*"-")