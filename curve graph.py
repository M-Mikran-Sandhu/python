# importing the required modules
import matplotlib.pyplot as plt
import numpy as np

# setting the x — coordinates
x = np.arange(0, 2 * np.pi, 0.1)

# setting the corresponding y — coordinates
y = np.sin(x)

# plotting the points
plt.plot(x, y)

# function to show the plot
plt.title("Sine Wave")
plt.xlabel("x values (radians)")
plt.ylabel("sin(x)")
plt.grid(True)
plt.show()
