import numpy as np

arr = np.arange(0, 10) # Makes an array from 0 to 10 (10 is not included).
print(arr)

print(50*"*")

arr = np.arange(10, 100, 3) # 10 to 100 with 3 at a time.
print(arr)

print(50*"*")

arr = np.zeros(10) # Makes an array with 10 zeros.
print(arr)

print(50*"*")

arr = np.ones(10) # Makes an array with 10 ones.
print(arr)

print(50*"*")

arr = np.linspace(0, 100, 5) # Makes an array with capacity of 5.
# Every intervel between pieces are equal and it starts from 0 to 100
print(arr)

print(50*"*")

arr = np.random.randint(0, 100) # Returns a number from 0 to 100 (100 is not included).
print(arr)

arr = np.random.randint(0, 100, 10) # Returns an array with 10 elements which are random integers between 0 and 100.
print(arr)

print(50*"*")

arr = np.random.rand(5) # Returns an array with 5 elements which are random floats between 0 and 1.
print(arr)

arr = np.random.randn(5) # Returns an array with 5 elements which are random floats between -1 and 1.
print(arr)

print(50*"*")

arr = np.arange(0, 50).reshape(5, 10) # Multi-Dimensional Array
print(arr)
print("Sum of the rows:", arr.sum(axis=1))
print("Sum of the columns:", arr.sum(axis=0))

print(50*"*")

arr = np.random.randint(0, 100, 10)
print("Random 10 numbers:", arr)
max_num = arr.max()
index_max = arr.argmax() # Index of the max number.
min_num = arr.min()
index_min = arr.argmin() # Index of the min number.
mean = arr.mean()
print("Max number of the array:", max_num)
print("Index of the max number:", index_max)
print("Min number of the array:", min_num)
print("Index of the min number:", index_min)
print("Mean of the array:", mean)
