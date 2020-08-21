import matplotlib.pyplot as plt
x1 = [1,2,3,4,5]
y1 = [5,4,3,3,6]
x2 = [6,7,8,9,10]
y2 = [4,3,4,2,1]
plt.scatter(x1, y1, c='red')
plt.scatter(x2, y2, c='blue')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
