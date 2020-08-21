import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')
plt.xlim([-10, 10])
plt.ylim([-10, 10])
plt.grid()

x = np.arange(-10,10,0.1)    #x = np.linspace(-10,10,10)
y1 = 0.5*x+2.5
y2 = x+2.5
y3 = 2*x+2.5
plt.plot(x, y1, '-r', label='y=0.5x+2.5')
plt.plot(x, y2, '-g', label='y=x+2.5')
plt.plot(x, y3, '-b', label='y=2x+2.5')
plt.legend(loc='upper left')

plt.show()