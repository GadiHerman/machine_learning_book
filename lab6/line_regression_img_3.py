from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


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
x = np.append(x1,x2)
y = np.append(y1,y2)
#--------Preparing the data for machine learned--------------------

#--------learning--------------------
def LinearRegression(x,y):
    avgx = np.mean(x)
    avgy = np.mean(y)
    m = (np.sum((x-avgx)*(y-avgy)))/(np.sum((x-avgx)*(x-avgx)))
    b = avgy - m*avgx
    return m,b

m,b =LinearRegression(x,y)
#--------learning--------------------

#--------Generate the graph----------------------------------------
x_line = np.linspace(0,255,len(x))
y_line = m*x_line + b 
 
plt.plot(x_line, y_line, color = "r")  
plt.scatter(x1, y1, color = "b", marker = "o", s = 40)
plt.scatter(x2, y2, color = "g", marker = "o", s = 40)
plt.scatter(xtest, ytest, color = "r", marker = "*", s = 200)
plt.title("Logic Regression")
plt.xlim([0, 255])
plt.ylim([0, 255])
plt.show()
#--------end generate the graph-------------------------------------

#--------predict data-------------------------------------
for xi , yi in zip(xtest,ytest):
    yi_line = m*xi + b 
    dist = yi-yi_line
    if dist>0:
        print("SEA Picture !!!")
    else:
        print("LAND Picture !!!")
#--------end predict data----------------------------------