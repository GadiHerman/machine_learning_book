import numpy as np
x3 = np.array([[[1  , 2 , 3 , 4 ],[5 , 6 , 7 , 8 ]],
                [[10, 20, 30, 40],[50, 60, 70, 80]]])
print("print all:\n",x3[0,0])
print("print all:\n",x3)
print("type: ", type(x3))
print("shape: ", x3.shape)
print("[0,0,0]: ",x3[0,0,0])
print("[1,1,3]: ",x3[1,1,3])
print("[0,0]: ",x3[0,0])
print("[1,1]: ",x3[1,1])
print("[0,:,0]",x3[0,:,0])
print("[0,:,3]",x3[1,:,3])
x3[0,0,0] = 500
x3[1,1,3]=100
print("print all:\n",x3)