from hashTable import HashTable

hash1 = HashTable(10)

hash1.addItem("apple", 58)
hash1.addItem("green", 87)
hash1.addItem("car", 54)

print(hash1)

print(hash1.getItem("car"))
print(hash1.getKeys())