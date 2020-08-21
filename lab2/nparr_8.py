import numpy as np
x1 = np.array([1, 2, 3])
x2 = np.array([6, 7, 8])
x = np.vstack((x1,x2))
print("\nprint all:\n",x)
y = np.hstack((x1,x2))
print("\nprint all:\n",y)

