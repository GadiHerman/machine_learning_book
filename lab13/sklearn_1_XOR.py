import numpy as np
import sklearn.neural_network

inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
expected_output = np.array([[0],[1],[1],[0]])

#model = sklearn.neural_network.MLPClassifier(activation='tanh', max_iter=10000, hidden_layer_sizes=(4,2), verbose = True)
model = sklearn.neural_network.MLPClassifier(activation='tanh', max_iter=10000, hidden_layer_sizes=(3,), solver='lbfgs')
model.fit(inputs, expected_output)

#print('score:', model.score(inputs, expected_output))
print('predictions:', model.predict(inputs))

