# 1- 1 ve 100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
# * "random modülü" için "python random" şeklinde arama yapın.
# ** 100 üzerinden puanlama yapın. Her soru 20 puan.
# *** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.

from random import randint
randnum = randint(1,100)  # range(a,b) fonksiyonunu kullanırken fonksiyon a dahil b 'ye kadar alır (b dahil değil) ama randint(a,b) fonksiyonunda b de dahil olur.
hak = int(input("Kaç hak istiyorsunuz:"))
sayac = 0
while sayac != hak:
    sayac += 1
    cvp = int(input("Tahmininizi giriniz:"))
    if cvp == randnum:
        print("Doğru tahmin ettiniz!!")
        break
    elif cvp < randnum:
        if (hak-sayac) != 0:
            print(f"{hak-sayac} hakkınız kaldı.")
            print("Daha yukarıdan tahmin etmeye çalışın.")
            print(50*"*")
            continue
        continue
    elif cvp > randnum:
        if (hak - sayac) != 0:
            print(f"{hak - sayac} hakkınız kaldı.")
            print("Daha aşağıdan tahmin etmeye çalışın.")
            print(50 * "*")
            continue
        continue
sayac += 1
if sayac == hak+1:
    print("Üzgünüm hakkınız bitti ve bilemediniz.")
    print(f"Sayı {randnum} idi.")
    print("Aldığınız puan => 0")
else:
    print(f"Tebrikler, {randnum} sayısını {hak} hakkınızdan {sayac-1} hakkınızı kullanarak bildiniz.")
    print(f"Bu sebeple 100 üzerinden aldığınız puan => {int(100-(100/hak)*(sayac-2))}")