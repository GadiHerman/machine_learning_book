import numpy as np

class Perceptron(object):
  def __init__(self, numOfInputs, epochs=1000, learningRate=0.01):
    self.epochs = epochs
    self.learningRate = learningRate
    self.weights = np.zeros(numOfInputs)
    self.bios = 1

  def Activation(self, s):
    if s > 0:
      activation = 1
    else:
      activation = 0            
    return activation

  def predict(self, inputs):
    sum = np.dot(inputs, self.weights) + self.bios
    out = self.Activation(sum)       
    return out

  def train(self, inputs, labels):
    for _ in range(self.epochs):
      for i in range(len(inputs)):
        prd = self.predict(inputs[i])
        self.weights -= (prd - labels[i]) * inputs[i] * self.learningRate
        self.bios -= (prd - labels[i]) * self.learningRate

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([1, 0, 1, 1])
perceptron = Perceptron(2)
perceptron.train(inputs, labels)


test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
for i in test:  
    print (i,"Output Machine Learning Algorithm: ", perceptron.predict(i))      
