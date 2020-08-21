import numpy as np
from termcolor import colored
import sklearn.neural_network

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

mlp = sklearn.neural_network.MLPClassifier(hidden_layer_sizes=(10), solver='sgd', learning_rate_init=0.01,
                    max_iter=500)

mlp.fit(train_data, train_lbl)

for i in range(len(test_data)):
    tt=test_data[i].reshape( 1,(test_data[i].shape[0]))
    p = mlp.predict(tt)
    print("test_lbl:" , colored(test_lbl[i], 'green')  ,"prediction: " , colored(p, 'green') )

	