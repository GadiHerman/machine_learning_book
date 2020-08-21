import numpy as np
x = np.array([2, 4, 6, 8, 10])
x2 = np.array([[2, 4, 6, 8, 10]])
a = x.T
b = x2.T
print("x.shape=",x.shape)
print("x2.shape=",x2.shape)
print("x:\n",x)
print("x2:\n",x2)
print("x.T:\n",a) 
print("x2.T:\n",b)
