import numpy as np
import matplotlib.pyplot as plt

def GradientDescent(x,y,learning_rate=0.01, epochs=1000):
    m=0
    b=0
    for _ in range(epochs):
        for i in range(len(x)): 
            xi = x[i]
            yi = y[i]
            guess = m * xi + b
            error = guess - yi
            m = m - (error * xi) * learning_rate
            b = b - error * learning_rate

    return m,b

ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.xlim([-1, 11])
plt.ylim([-1, 11])
plt.grid()

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]) 
y = np.array([1, 4, 2, 5, 7, 8, 8, 9, 10]) 

m,b=GradientDescent(x,y)

print("\nm = ",m," b = ",b) 
x_line = x
y_line = m*x + b  
plt.plot(x_line, y_line, color = "b")  
plt.scatter(x, y, color = "g", marker = "o", s = 40)
plt.title("Gradient Descent")
plt.show()