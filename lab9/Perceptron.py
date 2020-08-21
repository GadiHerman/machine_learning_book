import numpy as np

class Perceptron(object):
  def __init__(self, numOfInputs, epochs=200, learningRate=0.01):
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
        # self.weights += (labels[i] - prd) * inputs[i] * self.learningRate
        # self.bios += (labels[i] - prd) * self.learningRate

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
labels = np.array([0, 0, 0, 1])
perceptron = Perceptron(2,40,0.01)
perceptron.train(inputs, labels)

t1 = np.array([0, 0])
print(t1 , perceptron.predict(t1))
t2 = np.array([0, 1])
print(t2 , perceptron.predict(t2))
t3 = np.array([1, 0])
print(t3 , perceptron.predict(t3))
t4 = np.array([1, 1])
print(t4 , perceptron.predict(t4))