website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?

print(len(course))

# 2- 'website' içinden www karakterlerini alın.

print(website[7:10])

# 3- 'website' içinden com karakterlerini alın.

print(website[-3:])

# 4- 'course' içinden ilk 15 ve son 15 karakteri alın.

print(course[:15],course[-15:])

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.

print(course[::-1])

# 6- Aşağıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# 'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}.")

# 7- 'Hello world' ifadesindeki w harfini 'W' ile yer değiştirin.

word1 = "Hello world"
print(word1[:5],"W"+word1[7:])

# OR

print(word1.replace("w","W"))

# 8- 'abc' ifadesini yan yana 3 kez yazdırın.

word2 = "abc"
print(3*word2)