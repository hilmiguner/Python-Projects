import numpy as np

# 1D Python list
py_list_1D = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 1D Numpy array
np_array_1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
# or
np_array_1D = np.array(py_list_1D)

dim_len = np.ndim(np_array_1D)
shape = np.shape(np_array_1D)

print("1 Dimenional Python List:", py_list_1D)
print(f"{dim_len} Dimensional Numpy Array:", np_array_1D)
print(f"Shape of the Numpy array: {shape}")

print(50*"*")

# 2D Python list
py_list_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 2D Numpy array
np_array_2D = np_array_1D.reshape(3, 3)
# or
np_array_2D = np.array(py_list_2D)

dim_len = np.ndim(np_array_2D)
shape = np.shape(np_array_2D)

print("2 Dimenional Python List:", py_list_2D)
print(f"{dim_len} Dimenional Numpy Array:", np_array_2D)
print(f"Shape of the Numpy array: {shape}")