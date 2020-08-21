import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x_split = np.array_split(x,3)
print("print all split:\n",x_split)
print("print array[0]:\n",x_split[0])
print("print array[1]:\n",x_split[1])
print("print array[2]:\n",x_split[2])

