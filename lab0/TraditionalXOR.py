import numpy as np

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

for i in inputs:
    out_arr = np.bitwise_and(i[0], i[1])  
    print (i,"Output bitwise AND: ", out_arr)      
