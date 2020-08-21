import numpy as np
x = np.array([1, 2, 3, 4, 5 ])
x1 = x+10
print("\n x:\n",x)
print("\n x1: \n",x1)

x2 = np.empty([0])
for i in x:
    x2 = np.append(x2, [i+10])
print("\n x1: \n",x2)

