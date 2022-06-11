file = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile4.txt", "r", encoding="utf-8")
content = file.read()
print(content)
file.close()  # Burada dosyayı manuel olarak kapatıyoruz.


# Burada ise with kelimesi ile açtığımız satır bloğundaki işlemler bittiğinde dosya kendiliğinden kapanır.
with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile4.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)

print(50*"-")

file = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile4.txt", "r", encoding="utf-8")
content = file.read(5)
print(content)
cursor_current_location = file.tell()  # tell() fonksiyonu, cursorun nerede olduğunu söyler.
print(cursor_current_location)

content = file.read(8)
print(content)
cursor_current_location = file.tell()
print(cursor_current_location)

print(50*"-")

file.seek(0)  # seek() fonksiyonu, cursorun konumunu değiştirir.
cursor_current_location = file.tell()
print(cursor_current_location)
content = file.read(13)
print(content)
cursor_current_location = file.tell()
print(cursor_current_location)
