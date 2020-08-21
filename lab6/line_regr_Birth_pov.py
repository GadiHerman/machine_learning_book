import numpy as np
import matplotlib.pyplot as plt

#--------Preparing the data for machine learned--------
dataset = np.loadtxt("lab6\data.csv", delimiter=',')
x = dataset[:,0]
y = dataset[:,1]
#--------Preparing the data for machine learned-------- 

#--------learning--------------------
def LinearRegression(x,y):
    avgx = np.mean(x)
    avgy = np.mean(y)
    m = (np.sum((x-avgx)*(y-avgy)))/(np.sum((x-avgx)*(x-avgx)))
    b = avgy - m*avgx
    return m,b
m,b =LinearRegression(x,y)
#--------learning--------------------

#--------Generate the graph--------------------
x_line = np.arange(0, 40)
y_line = m*x_line + b  
plt.plot(x_line, y_line, color = "b")  
plt.scatter(x, y, color = "g", marker = "o", s = 20)
plt.title('Teen Birth Rate and Poverty Level Data')
plt.xlabel('Poverty Rate')
plt.ylabel('Birth Rate for 15 to 17 year old')
plt.xlim([5, 40])
plt.ylim([0, 120])
plt.grid()
plt.show()
#--------Generate the graph--------------------

#--------predict data--------------------
pov=float(input('Enter poverty rate: '))
brth15to17 = m*pov + b
print('Birth Rate for 15 to 17 year old is:', int(brth15to17))
#--------predict data--------------------
