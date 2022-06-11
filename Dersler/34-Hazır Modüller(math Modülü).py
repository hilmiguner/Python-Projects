import math

# Modüllerin fonksiyonlarına erişmek için dir() komutunu kullanabiliriz.

print(dir(math))
print(50*"-")

# Açıklamalarını istiyorsak help() komutunu kullanabiliriz.

print(help(math))
print(50*"-")

# Spesifik bir fonksiyonun açıklamasını istiyorsak;

print(help(math.factorial))
print(50*"-")

# Örnek;

print(f"5! = {math.factorial(5)}")
print(50*"-")

# Modülü çağırırken ismini istediğimiz gibi belirleyebiliriz.

import math as matematik

print(f"5! = {matematik.factorial(5)} (math yerine matematik kullandık)")
print(50*"-")

# Modülü çağırmak yerine modülden bir fonksiyon çağırabiliriz.

from math import sqrt

print(f"49'un karekökü {int(sqrt(49))}")
print(65*"-")

# Spesifik bir fonksiyon çağırmak yerine tüm fonksiyonları ayrı ayrı çağırabiliriz. Bu olay modülü çağırmak ile aynı
# gözükebilir ancak kullanım açısından daha kolaydır.

from math import *

a = int(sqrt(49))
b = factorial(4)
c = int(pow(5, 3))

print(f"49'un karekökü {a}, 4'ün faktöriyeli {b}, 5'in 3. kuvveti {c}")
print(65*"-")

# Peki biz sqrt() diye bir fonksiyon tanımlarsak ne olur ?

def sqrt(x):
    return f"x: {x}"

print(sqrt(9))
