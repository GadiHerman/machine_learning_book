import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.xlim([-1, 11])
plt.ylim([-1, 11])
plt.grid()

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]) 
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10]) 

plt.scatter(x, y, color = "m", marker = "o", s = 40)


plt.show()