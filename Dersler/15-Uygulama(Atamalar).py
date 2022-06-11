x,y,z=2,5,107

numbers=1,5,7,10,6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?

n1 = int(input("Bir sayı giriniz:"))
n2 = int(input("Başka bir sayı giriniz:"))
print((n1*n2)-(x+y+z))
print(30*"-")

# 2- y'nin x'e kalansız bölümünü hesaplayınız.

print(y//x)
print(30*"-")

# 3- (x+y+z) toplamının mod 3'ü nedir ?

print((x+y+z)%3)
print(30*"-")

# 4- y'nin x. kuvvetini hesaplayınız.

print(y**x)
print(30*"-")

# 5- x, *y,z = numbers işlemine göre z'nin küpü nedir ?

x,*y,z = numbers
print(z**3)
print(30*"-")

# 6- x, *y, z = numbers işlemine göre y'nin değerlerinin toplamı nedir ?

temp = 0
for i in y:
    temp += i
print(temp)
print(30*"-")