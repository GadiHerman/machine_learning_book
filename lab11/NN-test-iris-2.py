import numpy as np
import matplotlib.pyplot as plt

class NeuralNetwork:
	def __init__(self,inputLayerNeurons,hiddenLayerNeurons,outputLayerNeurons):
		self.hidden_weights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
		self.hidden_bias =np.random.uniform(size=(1,hiddenLayerNeurons))
		self.output_weights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
		self.output_bias = np.random.uniform(size=(1,outputLayerNeurons))
		self.predicted_output=0

	def sigmoid(self,x):
		return 1.0/(1.0 + np.exp(-x))

	def sigmoid_derivative(self,x):
		return x * (1.0 - x)
	
	def train(self, inpt, exp_out, learningRate=0.1, epochs=10000):
		for _ in range(epochs):
			#Forward Propagation
			hidden_layer_activation = np.dot(inpt,self.hidden_weights)
			hidden_layer_activation += self.hidden_bias
			hidden_layer_output = self.sigmoid(hidden_layer_activation)

			output_layer_activation = np.dot(hidden_layer_output,self.output_weights)
			output_layer_activation += self.output_bias
			self.predicted_output = self.sigmoid(output_layer_activation)

			#Backpropagation
			error = exp_out - self.predicted_output
			d_predicted_output = error * self.sigmoid_derivative(self.predicted_output)
			
			error_hidden_layer = d_predicted_output.dot(self.output_weights.T)
			d_hidden_layer = error_hidden_layer * self.sigmoid_derivative(hidden_layer_output)

			#Updating Weights and Biases
			self.output_weights += hidden_layer_output.T.dot(d_predicted_output) * learningRate
			self.output_bias += np.sum(d_predicted_output,axis=0,keepdims=True) * learningRate
			self.hidden_weights += inpt.T.dot(d_hidden_layer) * learningRate
			self.hidden_bias += np.sum(d_hidden_layer,axis=0,keepdims=True) * learningRate

	def predict(self, inpt):
		hidden_layer_activation = np.dot(inpt,self.hidden_weights)
		hidden_layer_activation += self.hidden_bias
		hidden_layer_output = self.sigmoid(hidden_layer_activation)

		output_layer_activation = np.dot(hidden_layer_output,self.output_weights)
		output_layer_activation += self.output_bias
		return self.sigmoid(output_layer_activation)

#------Get the iris data--------------------------
vir_iris_data = np.genfromtxt('data/iris_for_ML.csv', delimiter=',')
random_iris_data = np.random.permutation(vir_iris_data)
test_data = random_iris_data[0:40,:4]
train_data = random_iris_data[40:,:4]

test_lbl = random_iris_data[0:40,4:]
train_lbl = random_iris_data[40:,4:]

tmp=[]
for i in range(len(test_lbl)):
    if test_lbl[i] == 1:
        t = np.array([1,0,0])
    elif test_lbl[i] == 2:
        t = np.array([0,1,0])
    else:
        t = np.array([0,0,1])  
    tmp.append(t)   
new_test_lbl=np.array(tmp)

tmp=[]
for i in range(len(train_lbl)):
    if train_lbl[i] == 1:
        t = np.array([1,0,0])
    elif train_lbl[i] == 2:
        t = np.array([0,1,0])
    else:
        t = np.array([0,0,1])  
    tmp.append(t)   
new_train_lbl=np.array(tmp)

#------Train the Neural Network--------------------
nn = NeuralNetwork(4,5,3)
nn.train(train_data, new_train_lbl,0.01,1000)
#--------TEST the Neural Network-------------------
predict_values = nn.predict(test_data)
print('predict_values:\n',predict_values)
print('true_values:\n',new_test_lbl)
predict_indices = np.argmax(predict_values, axis=1)
print('predict_indices:\n',predict_indices)
true_indices = np.argmax(new_test_lbl, axis=1)
print('true_indices:\n',true_indices)
accuracy = np.mean(predict_indices==true_indices)
print('accuracy:\n',accuracy)
