import matplotlib.pyplot as plt
import numpy as np
a = np.array([[1,2,3,4,5,6,7,8,9,10],
              [1,3,7,4,8,5,9,7,3,2]])
              
categories = np.array([0,2,1,1,1,2,0,0,2,2])
colormap = np.array(['r', 'g', 'b'])
plt.scatter(a[0], a[1], s=100, c=colormap[categories])
plt.show()