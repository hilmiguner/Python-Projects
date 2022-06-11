# "is" operatörü

x=y=[1,2,3]
z=[1,2,3]
print(x==y) # "==" kullanırken değişkenlerin değeri karşılaştırılır.
print(x==z)
print(x is z) # "is" kullanırken değişkenlerin adresi karşılaştırılır, değişkenlerin değerinin hiç bir önemi olmaz.
print(x is y)
print(x is not z)

print(100*"-")

# "in" operatörü

a = ["apple","banana"]
print("banana" in a)  #"banana" değeri a adlı listede bulunuyorsa değer "True" olarak döner.
print("grape" in a)
print("grape" not in a)