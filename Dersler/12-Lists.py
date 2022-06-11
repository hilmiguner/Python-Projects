numbers = [1,10,5,16,4,9,10]
letters = ["a","g","s","b","y","a","s"]

print(min(numbers))
print(max(numbers))
print(min(letters))
print(max(letters))

print("------------------------")

numbers.append(49)
print(numbers)
numbers.insert(3,78)  # Takes index 3 to one index right and puts integer 3 into the empty index.
print(numbers)

print("------------------------")

numbers.pop()  # Removes the last element of the list.
print(numbers)
numbers.pop(3)  # Removes index 3 from the list.
print(numbers)

print("------------------------")

numbers.remove(4)  # .pop() deletes an index, .remove() deletes a specific element from the list.
print(numbers)

print("------------------------")

numbers.sort()
print(numbers)
letters.sort()
print(letters)

print("------------------------")

numbers.reverse()
print(numbers)
letters.reverse()
print(letters)

print("------------------------")

print(numbers.count(10))
print(letters.count("a"))

print("------------------------")

numbers.clear()
letters.clear()
print(numbers)
print(letters)