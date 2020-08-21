import numpy as np 
from termcolor import colored

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

inputs = np.array([	[0,0,0],
					[0,0,1],
					[0,1,0],
					[0,1,1],
					[1,0,0],
					[1,0,1],
					[1,1,0],
					[1,1,1]])
expected_output = np.array([[0,0],
							[1,1],
							[1,1],
							[1,0],
							[1,1],
							[1,0],
							[1,0],
							[1,1]])

nn = NeuralNetwork(3,3,2)
nn.train(inputs, expected_output)

A = int(input("Entar A (1 or 0):"))
B = int(input("Entar B (1 or 0):"))
C = int(input("Entar C (1 or 0):"))
while (A==1 or A==0) and (B==1 or B==0) and (C==1 or C==0):
	tests = np.array([ [A,B,C] ])
	print(colored(nn.predict(tests), 'blue'))
	A = int(input("Entar A (1 or 0):"))
	B = int(input("Entar B (1 or 0):"))
	C = int(input("Entar C (1 or 0):"))
