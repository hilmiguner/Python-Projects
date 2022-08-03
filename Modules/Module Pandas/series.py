import pandas as pd

# Data
numbers = [20, 30, 40, 50]
letters = ['a', 'b', 'c', 'd']

pandas_series1 = pd.Series(numbers)
pandas_series2 = pd.Series(letters)

print(f"Integer series: \n{pandas_series1}")
print(f"Letter series: \n{pandas_series2}")

print(50*"*")

# In Numpy, arrays must be homojens but in Pandas series can have different type of elements.
mixed_list = ['a', 'b', 10, 50,45]
mixed_series = pd.Series(mixed_list)
print(f"Mixed series: \n{mixed_series}")

print(50*"*")

# If we give a scalar data to the .Series() function, it returns a series with just 1 element that is the scalar value.
scalar = 5
pandas_series3 = pd.Series(scalar)
print(f"Series: \n{pandas_series3}")

print(50*"*")

# We can give specific keys to the elements.
pandas_series4 = pd.Series(numbers, letters)  # Keys are letters and values are numbers.
print(f"Series: \n{pandas_series4}")

print(50*"*")

# We can use dictionaries.
dict1 = {'a': 20, 'b': 30, 'c': 40, 'd':50}
pandas_series5 = pd.Series(dict1)
print(f"Dictionary Series: \n{pandas_series5}")

print(50*"*")

# We can use Numpy and Pandas together.
import numpy as np
random_numbers = np.random.randint(10, 100, 6)
pandas_series6 = pd.Series(random_numbers)
print(f"Pandas series from Numpy array: \n{pandas_series6}")

print(50*"*")

pandas_series7 = pd.Series(numbers, letters)  # We gave specific keys/indexes to the series 
# but we can access elements by default index rules.

print(f"Using key 'a' -> {pandas_series7['a']}")
print(f"Using key 0 -> {pandas_series7[0]}")
print("They are the same value.")

print(50*"*")

print(f"Series: \n{pandas_series7}")
print(f"Dimension of the series -> {pandas_series7.ndim}")
print(f"Data Type of the series -> {pandas_series7.dtype}")
print(f"Shape of the series -> {pandas_series7.shape}")
print(f"Sum of the elements -> {pandas_series7.sum()}")
print(f"Maximum element -> {pandas_series7.max()}")
print(f"Minimum element -> {pandas_series7.min()}")

print(50*"*")

sum_series1 = pandas_series7 + pandas_series7
print(f"First series: \n{pandas_series7}")
print(f"Sum series: \n{sum_series1}")

print(50*"*")

sum_series2 = pandas_series7 + 50
print(f"First series: \n{pandas_series7}")
print(f"First series after adding 50: \n{sum_series2}")

print(50*"*")

# Boolean series in Numpy module, is also here.
bool_series1 = pandas_series7 <= 30
print(f"The series: \n{pandas_series7}")
print(f"Boolean series of equality or less than 30: \n{bool_series1}")
print(f"Elements that less than or equal to 30: \n {pandas_series7[bool_series1]}")

print(50*"*")

opel2018 = pd.Series([20, 30, 40, 10], ["astra", "corsa", "mokka", "insignia"])
opel2019 = pd.Series([40, 30, 20, 10], ["astra", "corsa", "grandland", "insignia"])

total_opel_series = opel2018 + opel2019
print(f"Total series: \n{total_opel_series}")
