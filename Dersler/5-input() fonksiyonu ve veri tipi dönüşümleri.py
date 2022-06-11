x = input("First number: ")
y = input("Second number: ")
total1 = x + y                 #When we get a data from input() function, it is always string.
print(type(x))
print(type(y))
print(total1)                  #So total is not going to mathematical result, it is gonna show us x and y just together.

a = int(input("Third number: "))
b = int(input("Fourth number: "))
total2 = a + b
print(type(a))
print(type(b))
print(total2)

#       OR

total3 = int(x) + int(y)
print(total3)