from PIL import Image
import numpy as np
from sklearn.neural_network import MLPClassifier

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

mlp = MLPClassifier(hidden_layer_sizes=(5,),max_iter=1000,
                    solver='sgd', verbose=10, random_state=1)
 
mlp.fit(data, lbl)
print("Training set score: %f" % mlp.score(data, lbl))
print("Test set score: %f" % mlp.score(data, lbl))

newp = mlp.predict(test_data)
print (newp)