import numpy as np
 
x2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print("print all:\n",x2)
print("type: ", type(x2))
print("shape: ", x2.shape)
print("data from row0: ",x2[0,0], x2[0,1], x2[0,4])
print("data from row1: ",x2[1,0], x2[1,1], x2[1,4])
print("all row0: ",x2[0])
print("all row1: ",x2[1])
print("Column 0:",x2[0,:])
print ("Column 1:",x2[1,:])
 
x2[0,0] = 500
x2[1,4] = 100
print("all new array:\n",x2)


