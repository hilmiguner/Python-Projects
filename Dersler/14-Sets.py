fruits = {"apple" , "banana" , "orange"}

# Sets are like lists but you can't use index system. You can print sets by using for loop.

for x in fruits:
    print(x)

fruits.add("cherry")
print(fruits)
fruits.add("cherry")  # You can't use same element in sets.
print(fruits)

myList = [1,2,2,3,3,4,5]
print(myList)
print(set(myList))

print("-"*30)

fruits.update({"mango","grape"})
print(fruits)

fruits.remove("mango")
print(fruits)
fruits.discard("banana")
print(fruits)
fruits.pop()  # That function deletes last index from list but in sets, elements are not in a specific line so .pop() function in sets deletes random element from set.
print(fruits)
fruits.clear()
print(fruits)