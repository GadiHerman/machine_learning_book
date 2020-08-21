import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.xlim([-4, 4])
plt.ylim([-1, 10])
plt.grid()

x = np.arange(-4.0, 3.0, 0.1)
y= 2*x**2 + 4*x + 3
y2 = 4*x+4
plt.plot(x, y, color = "b")  
plt.plot(x, y2, color = "r")  
#plt.scatter(x, x**2, color = "g", marker = "o", s = 40)
plt.show()