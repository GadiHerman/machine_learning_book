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
y = np.array([1, 4, 2, 5, 7, 8, 8, 9, 10]) 

avgx = np.mean(x)
avgy = np.mean(y)
m = (np.sum((x-avgx)*(y-avgy)))/(np.sum((x-avgx)*(x-avgx)))
b = avgy - m*avgx

print("\nm = ",m," b = ",b) 
x_line = x
y_line = m*x + b  
plt.plot(x_line, y_line, color = "b")  
plt.scatter(x, y, color = "g", marker = "o", s = 40)
plt.title("Line Regression")
plt.show()