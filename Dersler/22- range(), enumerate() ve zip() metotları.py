# range()
print(list(range(3,11)))
print(100*"-")

# enumerate()

greeting = "Hello"
for item in enumerate(greeting):
    print(item)
for a,b in enumerate(greeting):
    print(f"{a}. index from greeting is {b}")
print(100*"-")

# zip()

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]
print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)
for a,b,c in zip(list1,list2,list3):
    print(a,b,c)