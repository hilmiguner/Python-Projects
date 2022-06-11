file = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile3.txt", "r", encoding="utf-8")
for i in file:
    print(i, end="")

print("\n"+(50*"-"))

# or

file = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile3.txt", "r", encoding="utf-8")
content = file.read()
print(content)

print(50*"-")

file = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile3.txt", "r", encoding="utf-8")
content = file.read(3)
print(content)
content = file.read(3)
print(content)
content = file.read(3)
print(content)
content = file.read(3)
print(content)
content = file.read(3)
print(content)

print(50*"-")

file = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile3.txt", "r", encoding="utf-8")
content = file.readline()
print(content, end="")
content = file.readline()
print(content, end="")
content = file.readline()
print(content, end="")
content = file.readline()
print(content, end="")

print("\n"+(50*"-"))

file = open("C:\\Users\\Casper\\Desktop\\Python\\Files\\newfile3.txt", "r", encoding="utf-8")
liste = file.readlines()
print(liste)

file.close()
