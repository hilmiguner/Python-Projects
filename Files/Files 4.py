content = "Güncelleme almadan önceki hali\n01234"
with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "w", encoding="utf-8") as file:
    file.write(content)
# "r+" hem okuma hem de yazma demektir.
with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "r+", encoding="utf-8") as file:
    print(file.read())

print(50*"-")

with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "r+", encoding="utf-8") as file:
    file.write("Deneme")
with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "r", encoding="utf-8") as file:
    print(file.read())

print(50*"-")

with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "a", encoding="utf-8") as file:
    file.write("56789")
with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "r", encoding="utf-8") as file:
    print(file.read())

print(50*"-")

with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "r+", encoding="utf-8") as file:
    liste = file.readlines()
    print(liste)
    liste.insert(1, "abcde\n")
    print(liste)
    file.seek(0)
    for i in liste:
        file.write(i)
with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "r", encoding="utf-8") as file:
    print(file.read())

# or
print(50*"-")

with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "r+", encoding="utf-8") as file:
    liste = file.readlines()
    print(liste)
    liste.insert(1, "A1B2C3D4\n")
    print(liste)
    file.seek(0)
    file.writelines(liste)
with open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile5.txt", "r", encoding="utf-8") as file:
    print(file.read())

