import numpy as np

numbers = np.array([0, 5, 10, 15, 20, 25, 50, 75]) # Numpy Array
print(f"Numpy Array -> {numbers}")

print(50*"*")

for index in range(0, len(numbers)):
    print(f"{index}. index -> {numbers[index]}")

print(50*"*")

print(f"From index 3 to index 7 (Index 7 is not included) -> {numbers[3:7]}")
print(f"Last index of the array -> {numbers[-1]}")

print(50*"*")

numbers2 = np.array([[0, 5, 10], [15, 20, 25], [50, 75, 85]]) # Multi-Dimensional Array
print(f"Multi-Dimensional array -> {numbers2}")
print(f"1. index of the array -> {numbers2[1]}")
print(f"0. index from the 1. index of the array -> {numbers2[1, 0]}") # or numbers2[1][0]
print(f"All indexes of the array -> {numbers2[:]}")
print(f"1. indexes from all of the indexes of the array -> {numbers2[:, 1]}")
print(f"From 0 to 2 indexes of the all indexes of the array (2. index is not included)-> {numbers2[:, 0:2]}")

print(50*"*")

# Numpy arrays work as references.
arr1 = np.arange(0, 10)
arr2 = arr1
print("BEFORE".center(50, "*"))
print(arr1)
print(arr2)

# CHANGES
arr2[0] = 20
arr1[4] = 50
# These changes affect the both array at same time (SAME ADDRESSES).

print("AFTER".center(50, "*"))
print(arr1)
print(arr2)

print(50*"*")

# If you want to copy the array without referencing:
arr3 = np.arange(0, 10)
arr4 = arr3.copy()

print("BEFORE".center(50, "*"))
print(arr3)
print(arr4)

# CHANGES
arr3[0] = 20
arr4[4] = 50
# These changes don't affect the both array (DIFFERENT ADDRESSES).

print("AFTER".center(50, "*"))
print(arr3)
print(arr4)
