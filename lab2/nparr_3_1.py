import numpy as np

x3 = np.array([[ [1 , 2 ],[3 , 4 ] ],
               [ [11, 12],[13, 14] ],
               [ [21, 22],[23, 24] ] ])
print("\nshape: ", x3.shape)

print("\nall:\n",x3)
print("\nall+10:\n",x3+10)
print("\nall*2:\n",x3*2)

x3[0,0,0] = 500
x3[2,1,1]=100
print("\nprint all:\n",x3)