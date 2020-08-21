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

class listOfpoint:
    def __init__(self,numberOfPoints,m=1,b=0):
        '''
        y=mx+b
        '''
        self.points=np.random.uniform(-1,1,size=(numberOfPoints,2))
        self.labels=np.sign(self.points[:,1] - (m*self.points[:,0] + b))
        # x2= x.reshape(x.shape[0],1)
        self.labels= self.labels.reshape(self.labels.shape[0],1)

    def __repr__(self):
        s=''
        for point,label in zip(self.points,self.labels):
            s += "\tx="+str(point[0])+"\ty="+str(point[1])+"\tlabel="+str(label)+"\n"
        return s

    def drawTrainingPoints(self):
        '''
        Draw the training inputs and the training label
        '''
        colormap = np.array(['r', 'g'])
        categories = []
        for i in range(len(self.points)): 
            if self.labels[i] > 0:
                categories.append(0)
            else:
                categories.append(1) 
        plt.scatter(self.points[:,0], self.points[:,1], s=40, c=colormap[categories])
        plt.show()

    def drawMistakesPoints(self,predict_values):
        '''
        Draw a comparison of the correct answers to the mistakes
        '''
        colormap1 = np.array(['r', 'g'])
        colormap2 = np.array(['r','g','w'])
        #Draw the correct answers
        categories = []
        accuracy = 0
        for i in range(len(self.points)): 
            if self.labels[i] > 0:
                categories.append(0)
            else:
                categories.append(1) 
        plt.scatter(self.points[:,0], self.points[:,1], s=30, c=colormap1[categories])
        #-------------------------------------------------
        categories = []
        for i in range(len(predict_values)):
            if (predict_values[i] > 0.5) and (self.labels[i] > 0):
                categories.append(0)
                accuracy +=1
            elif (predict_values[i] < 0.5) and (self.labels[i] < 0):
                categories.append(1)
                accuracy +=1
            else:
	            categories.append(2)

        plt.scatter(self.points[:,0], self.points[:,1], s=10, c=colormap2[categories])      
        plt.axis([-1,1,-1,1])
        plt.show()
        return accuracy / len(predict_values)

#------Train the Neural Network--------------------
train_points = listOfpoint(200,-1,-0.2)
train_points.drawTrainingPoints()
nn = NeuralNetwork(2,2,1)
nn.train(train_points.points, train_points.labels)
#--------TEST the Neural Network-----------------------
test_points = listOfpoint(2000,-1,-0.2)
predict_values = nn.predict(test_points.points)
accuracy = test_points.drawMistakesPoints(predict_values)
print ('Accuracy: ',accuracy)
