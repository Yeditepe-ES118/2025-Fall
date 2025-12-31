import matplotlib.pyplot as plt
import numpy as np

# DATA GENERATION
# x-axis:
x = np.linspace(0,2*np.pi,100)

# f function (discontinuous):
f = np.zeros((100,))

f0 = np.sin(x[(0 <= x) & (x < np.pi/2)])
f[0:np.size(f0)] = f0

f1 = x[(np.pi/2 <= x) & (x < np.pi)]
f[np.size(f0):np.size(f0) + np.size(f1)] = 0

f2 = np.sin(x[(np.pi <= x) & (x < 3*np.pi/2)])
f[np.size(f0) + np.size(f1):np.size(f0) + np.size(f1) + np.size(f2)] = f2

# no need to evaluate the last section because it also remains 0 in f

# other two functions:
g = -x**2 + 3

h = 3*np.ones((np.size(x),))

# PLOTTING
fig, ax = plt.subplots(1,2)

# first subplot:
ax[0].plot(x,f,"ks-")
ax[0].set_title("f(x) vs x")
ax[0].set_ylabel("f(x)")
ax[0].set_xlabel("x")
ax[0].grid()

# second subplot:
ax[1].plot(x,g,"b-",label="g(x) = -x**2 + 3")
ax[1].plot(x,h,"r-",label="h(x) = 3")
ax[1].set_title("Two functions")
ax[1].set_ylabel("outputs")
ax[1].set_xlabel("x")
ax[1].legend(loc="lower left")
ax[1].grid()

plt.tight_layout()

plt.show()
