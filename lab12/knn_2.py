#import matplotlib.pyplot as plt
import numpy as np

data = np.array( [	[ 6.0 , 7.0],
					[ 2.0 , 3.0],
					[ 3.0 , 7.0],
					[ 4.0 , 4.0],
					[ 5.0 , 8.0],
					[ 6.0 , 5.0],
					[ 7.0 , 9.0],
					[ 8.0 , 5.0],
					[ 8.0 , 2.0],
					[10.0 , 2.0]	])
              

def euclidean_distance(p1, p2):
    d = 0.0
    for i in range(len(p1)):
        a = float(p1[i])
        b = float(p2[i])
        d += np.power((a-b),2)
    d = np.sqrt(d)
    return d


# print("\n All point: \n",data)
# print(data[:,0])
# print(data[:,1])
print("\nAll Euclidean Distance from point: ",data[0], "\n")
for point in data:
	distance = euclidean_distance(data[0], point)
	print(distance)
# x1 = [1.0, 2.0, 4.0, 5.0, 6.0, 7.0]
# print(np.power(x1, 2))