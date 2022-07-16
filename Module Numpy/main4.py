import numpy as np

arr1 = np.random.randint(10, 100, 6)
arr2 = np.random.randint(10, 100, 6)

print("First array ->", arr1)
print("Second array ->", arr2)

sum_arr1 = arr1 + arr2

print("Type of the array ->", type(sum_arr1))
print("Array ->", sum_arr1)

print(50*"*")

sum_arr2 = arr1 + 10
print("Array before addition ->", arr1)
print("Array after adding 10 to every element ->", sum_arr2)

print(50*"*")

diff_arr1 = arr1 - arr2
print("First array ->", arr1)
print("Second array ->", arr2)
print("Difference array ->", diff_arr1)

print(50*"*")

diff_arr2 = arr1 - 10
print("Array before substraction ->", arr1)
print("Array after substracting 10 from every element ->", diff_arr2)

print(50*"*")

multi_arr1 = arr1 * arr2
print("First array ->", arr1)
print("Second array ->", arr2)
print("Multiplication array ->", multi_arr1)

print(50*"*")

multi_arr2 = arr1 * 10
print("Array before multiplication ->", arr1)
print("Array after multiplying every element with 10 ->", multi_arr2)

print(50*"*")

div_arr1 = arr1 / arr2
print("First array ->", arr1)
print("Second array ->", arr2)
print("Division array ->", div_arr1)

print(50*"*")

div_arr2 = arr1 / 10
print("Array before division ->", arr1)
print("Array after dividing every element with 10 ->", div_arr2)

print(50*"*")

sin_arr = np.sin(arr1)
cos_arr = np.cos(arr1)

print("Array ->", arr1)
print("Sinus of the array ->", sin_arr)
print("Cosinus of the array ->", cos_arr)

print(50*"*")

multi_dim_arr1 = arr1.reshape(2, 3)
multi_dim_arr2 = arr2.reshape(2, 3)

vertically_stacked_arr = np.vstack((multi_dim_arr1, multi_dim_arr2))
horizontally_stacked_arr = np.hstack((multi_dim_arr1, multi_dim_arr2))

print(" First multi-dimensional array ".center(50, "*"))
print(multi_dim_arr1)
print(" Second multi-dimensional array ".center(50, "*"))
print(multi_dim_arr2)
print(" Vertically stacked array ".center(50, "*"))
print(vertically_stacked_arr)
print(" Horizontally stacked array ".center(50, "*"))
print(horizontally_stacked_arr)

print(50*"*")

bool_arr1 = arr1 >= 50
bool_arr2 = arr1 % 2 == 0
print("The array ->", arr1)

print()

print("Boolean array created by checking the elements are bigger or equal to 50 ->", bool_arr1)
print("The elements which are bigger or equal to 50 ->", arr1[bool_arr1])

print()

print("Boolean array created by checking the mod 2 of the elements equal to 0 (Even or Odd) ->", bool_arr2)
print("The elements which are even ->", arr1[bool_arr2])
print("Inverse of the last boolean array ->", bool_arr2.__invert__())
print("The elements which are odd ->", arr1[bool_arr2.__invert__()])