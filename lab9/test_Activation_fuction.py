import numpy as np 
import matplotlib.pyplot as plt 

def Activation(s):
    if s > 0:
        activation = 1
    else:
        activation = 0            
    return activation

in_array = np.linspace(-10, 10, 50)
out_array = []
for i in range(len(in_array)):
    out_array.append(Activation(in_array[i]))
out_array = np.array(out_array)
print("in_array : ", in_array) 
print("\nout_array : ", out_array) 
  
plt.plot(in_array, out_array, marker = ".") 
plt.title("Activation Function") 
plt.xlabel("X") 
plt.ylabel("Y") 
plt.show() 


