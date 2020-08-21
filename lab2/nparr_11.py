import numpy as np
x1 = np.array([1, 2, 3, 4, 5 ])
x2 = np.array([1, 3, 3, 6, 7 ])
x3 = x1 == x2
x4 = x1 < x2
x5 = x1 > x2
x6 = x1 != x2
print("\n x1 == x2: \n",x3)
print("\n x1 > x2: \n",x4)
print("\n x1 < x2: \n",x5)
print("\n x1 != x2: \n",x6)


