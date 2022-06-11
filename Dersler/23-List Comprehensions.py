for x in range(1,10):
    print(x)

numbers = [x for x in range(1,10)]
print(numbers)

print(100*"-")

for x in range(1,10):
    print(x**2)

numbers = [x**2 for x in range(1,10)]
print(numbers)

print(100*"-")

numbers = [x for x in range(1,10)]
print(numbers)
numbers = [x for x in range(1,10) if x%3==0]
print(numbers)

print(100*"-")

myString = "Hello"
myList = []
for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

print(100*"-")

years = [1983,1999,2008,1956,1986]
print(years)
ages = [(2021-x) for x in years]
print(ages)

print(100*"-")

numbers = [x if x%2 ==0 else "tek" for x in range(1,11)]
print(numbers)