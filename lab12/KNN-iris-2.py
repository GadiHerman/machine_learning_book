import numpy as np
from termcolor import colored

vir_iris_data = np.genfromtxt('iris_for_ML.csv', delimiter=',')
random_iris_data = np.random.permutation(vir_iris_data)
test_data = random_iris_data[0:10,:4]
train_data = random_iris_data[10:,:4]
test_lbl = random_iris_data[0:10,4:]
train_lbl = random_iris_data[10:,4:]
print("\nrandom_iris_data: \n",colored(random_iris_data, 'red'),"\n")
print("\ntrain_data: \n",colored(train_data, 'blue'),"\n")
print("\ntrain_lbl: \n",colored(train_lbl, 'blue'),"\n")
print("\ntest_data: \n",colored(test_data, 'green'),"\n")
print("\ntest_lbl: \n",colored(test_lbl, 'green'),"\n")

def euclidean_distance(p1, p2):
    d = 0.0
    for i in range(len(p1)):
        a = float(p1[i])
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
	NN = []
	for i in range(K):
		NN.append(distances[i])
	return NN

def predict(train, test, lbl, K):
	neighbors = KNN(train, test, lbl, K)
	out = [row[-1] for row in neighbors]
	return max(set(out), key=out.count)

for i in range(len(test_data)):
	p = predict(train_data, test_data[i], train_lbl, 1)
	print("test_lbl:" , colored(test_lbl[i], 'green')  ,"prediction: " , colored(p, 'green') )

