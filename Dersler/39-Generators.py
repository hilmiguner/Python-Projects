def cube():
    # With this "temp = []", you located data in ram.
    temp = []
    for i in range(5):
        temp.append(i**3)
    return temp

print(cube())

def cubeYield():
    for i in range(5):
        # With "yield" keyword, you can use it variable for once. You can not acces again after that.
        yield i**3

# Function creates an iterable object.
generator = cubeYield()

print(generator)

# Let's create an iterator object.
iterator = iter(generator)

# Every time you use "next(iterator)", cubeYield function's "i" variable gets the other value, so all i's values does not allocate ram.
print(next(iterator))
print(next(iterator))
print(next(iterator))

# But you don't have to create an iterator object because generator object is already has iterator.
print("Without iterator")
print(next(generator))

# Let's create another variable.
generator1 = cubeYield()

print("Printing with for loop")
# Printing iterator values with for loop.
for i in generator1:
    print(i)

print("Without creating new variable, just using function itself.")

# Or we can use any other variables.
for i in cubeYield():
    print(i)

# Or we can use these syntax.

generator2 = (i**3 for i in range(5))
print(generator2)

print(next(generator2))

