import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-20, 20, 0.1)
y1 = 10*x + 6
y2 = 2*x**2+2*x-100
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.show()