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
              
def euclidean_distance(p1, p2):
    d = 0.0
    for i in range(len(p1)):
        a = float(p1[i])
        b = float(p2[i])
        d += np.power((a-b),2)
    d = np.sqrt(d)
    return d

def KNN(train, test, K):
	distances = []
	for p in train:
		dist = euclidean_distance(test, p)
		distances.append((p, dist))
	distances.sort(key=lambda dist: dist[1])
	distances = np.delete(distances,[0], axis=0)
	NN = []
	for i in range(K):
		NN.append(distances[i][0])
	return NN
 
neighbors = KNN(data, data[0], 3)
for neighbor in neighbors:
	print(neighbor)