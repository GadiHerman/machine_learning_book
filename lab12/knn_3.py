import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

data = np.array( [	[ 6.0 , 7.0, 5.0],
					[ 2.0 , 3.0, 7.0],
					[ 3.0 , 7.0, 2.0],
					[ 4.0 , 4.0, 8.0],
					[ 5.0 , 8.0, 9.0],
					[ 6.0 , 5.0, 7.0],
					[ 7.0 , 9.0, 4.0],
					[ 8.0 , 5.0, 1.0],
					[ 8.0 , 2.0, 3.0],
					[10.0 , 2.0, 5.0]	])
              
categories = np.array([0,1,1,1,1,2,2,2,2,2])
colormap = np.array(['r', 'g', 'b'])

fig = plt.figure()
ax = Axes3D(fig)

ax.scatter(data[:,0], data[:,1],data[:,2], s=150, c=colormap[categories])
plt.show()