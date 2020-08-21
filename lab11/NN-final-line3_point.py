import numpy as np
import matplotlib.pyplot as plt
#np.random.seed(1000)

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

class point(object):
    def __init__(self,m=1,b=0):
        '''
        y=mx+b
        '''
        self.x = np.random.uniform(-1,1)
        self.y = np.random.uniform(-1,1)
        if (self.x)*m+b > self.y:
            self.label = 1
        else:
            self.label = -1

class listOfpoint:
    def __init__(self,numberOfPoints,m=1,b=0):
        '''
        Get number Of Points
        Get m and b parameter in y=mx+b (linear function line)
        Return list of point class
        '''
        self.points = []
        for _ in range(numberOfPoints):
            self.points.append(point(m,b))

        self.allXY=[]
        self.allLBL=[]
        for item in self.points:
            tmpXY = np.array([item.x , item.y])
            tmpLBL = np.array([item.label])
            self.allXY.append(tmpXY)   
            self.allLBL.append(tmpLBL)
        self.allXY=np.array(self.allXY)
        self.allLBL=np.array(self.allLBL)

    
    def drawTrainingPoints(self):
        '''
        Draw the training inputs and the training label
        '''
        categories = []
        colormap = np.array(['r', 'g'])
        px = []
        py = []
        for i in range(len(self.points)):
            px.append(self.points[i].x)
            py.append(self.points[i].y)
            if self.points[i].label > 0:
                categories.append(0)
            else:
                categories.append(1)      
        plt.scatter(px, py, s=10, c=colormap[categories])
        plt.axis([-1, 1, -1, 1])
        plt.show()

    def drawMistakesPoints(self,predict_values):
        '''
        Draw a comparison of the correct answers to the mistakes
        '''
        colormap1 = np.array(['r', 'g'])
        colormap2 = np.array(['w', 'b'])
        #Draw the correct answers
        categories = []
        for i in range(len(self.allXY)): 
            if self.points[i].label > 0:
                categories.append(0)
            else:
                categories.append(1) 
            
        plt.scatter(self.allXY[:, 0],self.allXY[:, 1], s=40, c=colormap1[categories])
        #-------------------------------------------------
        categories = []
        for i in range(len(predict_values)):
            if predict_values[i] > 0.5:
                categories.append(0)
            else:
                categories.append(1)
        plt.scatter(self.allXY[:, 0],self.allXY[:, 1], s=10, c=colormap2[categories])      
        plt.axis([-1, 1, -1, 1])
        plt.show()



#------Train the Neural Network--------------------
train_points = listOfpoint(200,-1,-0.2)
train_points.drawTrainingPoints()
nn = NeuralNetwork(2,2,1)
nn.train(train_points.allXY, train_points.allLBL)
#--------TEST the Neural Network-----------------------
test_points = listOfpoint(2000,-1,-0.2)
predict_values = nn.predict(test_points.allXY)
test_points.drawMistakesPoints(predict_values)
