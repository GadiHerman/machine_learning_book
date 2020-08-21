from PIL import Image
import numpy as np

img = Image.open("data/train.jpg")
img.load()
data = np.array(img, dtype=np.uint8)
#print(data.shape,type(data))

data[0:100,0:100]=[255, 0, 0]
data[100:200,100:200]=[0, 255, 0]
data[200:300,200:300]=[0, 0, 255]
data[300:400,300:400]=[255, 0, 255]
data[400:500,400:500]=[0, 255, 255]
data[500:600,500:600]=[255, 255, 255]

# data[0:100,0:100,0]=255
# data[0:100,0:100,1]=0
# data[0:100,0:100,2]=0


img = Image.fromarray(data)
img.show()