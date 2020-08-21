import matplotlib.pyplot as plt
import numpy as np

train_data = np.array( [	
		[ 2.0 , 3.0 ],
		[ 3.0 , 7.0 ],
		[ 4.0 , 4.0 ],
		[ 5.0 , 8.0 ],
		[ 6.0 , 5.0 ],
		[ 7.0 , 9.0 ],
		[ 8.0 , 5.0 ],
		[ 8.0 , 2.0 ],
		[10.0 , 2.0 ]	])

train_lbl = np.array( [	
		[ 1 ],
		[ 1 ],
		[ 1 ],
		[ 1 ],
		[ 2 ],
		[ 2 ],
		[ 2 ],
		[ 2 ],
		[ 2 ]	])

test_data = np.array( [	[ 6.0 , 7.0 ]	])
# test_lbl = np.array( [	[ 0 ]	])

def euclidean_distance(p1, p2):
    d = 0.0
    for i in range(len(p1[0])):
        a = float(p1[0,i])
        b = float(p2[i])
        d += np.power((a-b),2)
    d = np.sqrt(d)
    return d

def KNN(train, test, lbl, K):
	distances = []
	for t, l in zip(train,lbl):
		dist = euclidean_distance(test, t)
		distances.append((t, dist, l[0]))
	distances.sort(key=lambda dist: dist[1])
	# distances = np.delete(distances,[0], axis=0)
	NN = []
	for i in range(K):
		NN.append(distances[i])
	return NN

def predict(train, test, lbl, K):
	neighbors = KNN(train, test, lbl, K)
	out = [row[-1] for row in neighbors]
	return max(set(out), key=out.count)

prediction = predict(train_data, test_data, train_lbl, 3)
print("prediction: " , prediction)
