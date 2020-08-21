import numpy as np
import matplotlib.pyplot as plt

def LineRegression(x,y):
    avgx = np.mean(x)
    avgy = np.mean(y)
    lin_m = (np.sum((x-avgx)*(y-avgy)))/(np.sum((x-avgx)*(x-avgx)))
    lin_b = avgy - lin_m*avgx
    return lin_m,lin_b

def GradientDescent(x,y,learning_rate=0.01, epochs=200):
    m=0
    b=0
    err_m = np.array([0])
    err_b = np.array([0])
    lin_m,lin_b=LineRegression(x,y)
    for _ in range(epochs):
        for i in range(len(x)): 
            xi = x[i]
            yi = y[i]
            guess = m * xi + b
            error = guess - yi
            m = m - (error * xi) * learning_rate
            b = b - error * learning_rate
        err_m = np.append(err_m,m-lin_m)
        err_b = np.append(err_b,b-lin_b)
    return m,b,err_m,err_b

ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
plt.xlim([-1, 11])
plt.ylim([-1, 11])
plt.grid()

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8]) 
y = np.array([1, 4, 2, 5, 7, 8, 8, 9, 10]) 

m,b,err_m,err_b=GradientDescent(x,y)

print("\nm = ",m," b = ",b) 
x_line = x
y_line = m*x + b  
plt.plot(x_line, y_line, color = "b")  
plt.scatter(x, y, color = "g", marker = "o", s = 40)
plt.show()

plt.plot(err_m, '-r', label='m' )
plt.plot(err_b, '-g', label='b')
plt.legend(loc='upper right')

plt.show()