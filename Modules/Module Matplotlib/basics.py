from matplotlib import pyplot as plt
import numpy as np

# x = [1, 2, 3, 4]
# y = [1, 4, 9, 16]

# plt.plot(x, y, color="red", linewidth=5)
# plt.axis([0, 6, 0, 20])  # x-axis is 0 to 6 and y-axis 0 to 20.
# plt.title("Graph")
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.show()

# -------------------------------------
# Or you can use plot style.
# -------------------------------------

# plt.plot(x, y, "--g")  # "g--" means line is green and dashed. [marker][line][color]
# plt.show()

# plt.plot(x, y, "H-r")  # [Hexagon][Straight Line][Red] = [H][-][r]
# plt.show()

# -------------------------------------

# data = np.linspace(0, 2, 100)
# plt.plot(data, data, label="Linear")
# plt.plot(data, data**2, label="Quadratic")
# plt.plot(data, data**3, label="Cubic")

# plt.legend()  # Shows info of the all lines on the graph.
# plt.show()

# -------------------------------------
# Adding multiple graphs on a same window.
# -------------------------------------

# figure, axes = plt.subplots(3)  # 3 means there will be 3 graphs total.
# # axes is a array which holds the every graph.

# x = np.linspace(0, 2, 100)

# axes[0].plot(x, x, color="red")
# axes[0].set_title("Linear")

# axes[1].plot(x, x**2, color="green")
# axes[1].set_title("Quadratic")

# axes[2].plot(x, x**2, color="yellow")
# axes[2].set_title("Cubic")

# plt.show()  # As you can see graph titles are blocked by other graph values so we need to change the layout.

# -------------------------------------

# x = np.linspace(0, 2, 100)
# figure, axes = plt.subplots(3)

# axes[0].plot(x, x, color="red")
# axes[0].set_title("Linear")

# axes[1].plot(x, x**2, color="green")
# axes[1].set_title("Quadratic")

# axes[2].plot(x, x**2, color="yellow")
# axes[2].set_title("Cubic")

# plt.tight_layout()
# plt.show()

# -------------------------------------
# We can use rows and columns as a layout.
# -------------------------------------

# x = np.linspace(0, 2, 100)

# figure, axes = plt.subplots(2, 2)
# figure.suptitle("Graphs")

# axes[0, 0].plot(x, x, color="red")
# axes[0, 1].plot(x, x**2, color="green")
# axes[1, 0].plot(x, x**3, color="blue")
# axes[1, 1].plot(x, x**4, color="yellow")

# plt.show()

# -------------------------------------
# Now let's use a real data.
# -------------------------------------

import pandas as pd

df = pd.read_csv("Modules/Module Pandas/datasets/nba.csv")
df.drop(["Number"], axis=1, inplace=True)
df = df.groupby("Team").mean()

df.plot(subplots=True)
plt.legend()
plt.show()
