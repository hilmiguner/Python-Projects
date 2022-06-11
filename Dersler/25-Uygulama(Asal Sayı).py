# Girilen bir sayının asal olup olmadığını bulun.

num = int(input("Lütfen bir sayı giriniz:"))
a = True
for i in range(2,(int(num/2))+1):
    if num % i == 0:
        a = False
        break
    else:
        a = True
if a == False:
    print("Sayı asal değildir.")
else:
    print("Sayı asaldır.")