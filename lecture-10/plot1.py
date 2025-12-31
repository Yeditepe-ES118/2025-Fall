import matplotlib.pyplot as plt
import numpy as np

# Generate data points
x1 = np.linspace(0, 100, 50)
x2 = np.linspace(0, 100, 1000)

f = 20*x1 + 3
g = 3*x1**2 + np.sqrt(x1)
h = 3e3*np.sin(5*x2) * np.exp(-0.5*x2)

# Plot an overlay 2D plot for f, g, h
fig, ax = plt.subplots()
ax.plot(x1, f, "o", label = "f(x) = 20x + 3")
ax.plot(x1, g, "^-", label = "g(x) = 3x^2 + x^(1/2)")
ax.plot(x2, h, "-", label = "h(x) = 3*10^3*sin(5x) * exp(-0.5x)")
ax.legend(loc="lower right")

# Other stuff
ax.set(title = "Plot for f(x), g(x), and h(x)", xlabel = "x", ylabel = "y")
ax.grid()
ax.set_xlim(left=-0.5, right=40)
ax.set_ylim(top=5000)

plt.show()