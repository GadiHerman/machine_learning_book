from PIL import Image
import numpy as np
#import matplotlib.pyplot as plt

pixels = np.zeros([100,200,3],dtype=np.uint8)
pixels[:,:100] = [255, 0, 0]
pixels[:,100:] = [0, 0, 255]
print(pixels.shape,type(pixels))
img = Image.fromarray(pixels)
img.show()
#plt.imshow(img)
#plt.show()

