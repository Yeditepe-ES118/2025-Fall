import matplotlib.pyplot as plt
import numpy as np

# Generate data points
x = np.arange(0,105,5)
f = 5*x + 3
g = 3*x**2 + np.sqrt(x)
h = 100*np.sin(x)**2 * np.exp(-x)

# Plot a 2D single plot for x and y
#fig, ax = plt.subplots()
#ax.plot(x,y,"D")

# Plot an overlay 2D plot for f, g, h
fig, ax = plt.subplots()
ax.plot(x, f, "o", label = "f(x) = 5x + 3")
ax.plot(x, g, "^", label = "g(x) = 3x^2 + x^(1/2)")
ax.plot(x, h, "s", label = "h(x) = 100sin(x)^2 * e^(-x)")
ax.legend(loc = "upper right")

# Other stuff
ax.set(title = "Plot for f(x), g(x), and h(x)", xlabel = "x", ylabel = "y")
ax.grid()
ax.set_ylim(-10, 1000)

plt.show()