import os
from matplotlib import pyplot as plt
import numpy as np

# x = np.linspace(-10, 9, 20)
# y = x**3
# z = x**2

# figure = plt.figure()

# axes_cube = figure.add_axes([0.1, 0.1, 0.8, 0.8])  # There will be %10 blank from bottom and left and axes will cover %80 of the right and upper side.
# axes_cube.plot(x, y, color="red")
# axes_cube.set_xlabel("X-Axis")
# axes_cube.set_ylabel("Y-Axis")
# axes_cube.set_title("Cube Graph")

# axes_square = figure.add_axes([0.15, 0.6, 0.3, 0.2])
# axes_square.plot(x, z, color="blue")
# axes_square.set_xlabel("X-Axis")
# axes_square.set_ylabel("Y-Axis")
# axes_square.set_title("Quadratic Graph")

# plt.show()

# -----------------------------------------------

# x = np.linspace(-10, 9, 20)
# y = x**3
# z = x**2

# figure = plt.figure()
# axes = figure.add_axes([0.1, 0.1, 0.8, 0.8])
# axes.plot(x, y, label="Cubic")
# axes.plot(x, z, label="Quadratic")

# plt.legend(loc=4)  # 1 is right upper corner, 2 is left upper corner, 3 is left bottom corner and 4 is right bottom corner for the location of the legend.
# plt.show()

# -----------------------------------------------

x = np.linspace(-10, 9, 20)
y = x**3
z = x**2

figure, axes = plt.subplots(nrows=2, ncols=1, figsize=(4,4))  # Or you can use figure, (axes1, axes2) = plt.subplots(nrows=2, ncols=1, figsize=(4,4))
# Figsize manages the size of the figure.

axes[0].plot(x, y)
axes[0].set_title("Cube")

axes[1].plot(x, z)
axes[1].set_title("Square")

plt.tight_layout()
plt.show()

try:
    figure.savefig("Modules/Module Matplotlib/Saves/Figure1.png")
except FileNotFoundError as err:
    os.mkdir("/".join(str(err.filename).split("/")[:-1]))
    figure.savefig(err.filename)