import matplotlib.pyplot as plt
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

categories = np.array([0,1,1,1,1,2,2,2,2,2])
colormap = np.array(['r', 'g', 'b'])

plt.scatter(data[:,0], data[:,1], s=100, c=colormap[categories])
plt.show()

