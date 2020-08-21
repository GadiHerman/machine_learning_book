from PIL import Image
import numpy as np

#--------start Perceptron---------------------------------
class Perceptron(object):
  def __init__(self, numOfInputs, epochs=100, learningRate=0.01):
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
#--------end Perceptron----------------------------------

#--------start get data from images---------------------------------- 
sea_colors = list()
for i in range(10):
    img = Image.open("data/sea" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    sea_colors.append([data[:,:,color].sum() / data[:,:,color].size for color in range(3)])
 
land_colors = list()
for i in range(10):
    img = Image.open("data/land" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    land_colors.append([data[:,:,color].sum() / data[:,:,color].size for color in range(3)])

test_colors = list()
for i in range(6):
    img = Image.open("test/test" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    test_colors.append([data[:,:,color].sum() / data[:,:,color].size for color in range(3)])
#--------end get data from images---------------------------------- 

#--------Preparing the data for machine learned-------------------- 
sea_array = np.array(sea_colors)
land_array = np.array(land_colors)
test_array = np.array(test_colors)
 
x1 = sea_array[:,1]
y1 = sea_array[:,2]
x2 = land_array[:,1]
y2 = land_array[:,2]
xtest = test_array[:,1]
ytest = test_array[:,2]
 
x = list()
y = list()

x = np.append(x1,x2)
y = np.append(y1,y2)

data = np.stack((x, y), axis=-1)
test_data = np.stack((xtest, ytest), axis=-1)

lbl=[0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]

#--------Preparing the data for machine learned--------------------
print("\nx1- sea_array_green:\n",x1)
print("\ny1- sea_array_blue:\n",y1)
print("\nx2 - land_array_green:\n",x2)
print("\ny2 - land_array_blue:\n",y2)
print("\nxtest - test_array_green:\n",xtest)
print("\nytest - test_array_blue:\n",ytest)
print("\nx (all training data green):\n",x)
print("\ny (all training data blue):\n",y)
print("\ndata (all training data (green and blue)):\n",data)
print("\ntest_data (all testing data (green and blue)):\n",test_data)
print("\nlbl:\n",lbl)

#--------start run machine learned---------------------------------
perceptron = Perceptron(2)
perceptron.train(data, lbl)

for i in test_data:
    if perceptron.predict(i)==0:
        print(i , "SEA Picture !!!")
    else:
        print(i , "LAND Picture !!!")
       

#--------end run machine learned----------------------------------
