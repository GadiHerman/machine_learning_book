from PIL import Image
import numpy as np
#import matplotlib.pyplot as plt

pixels = np.zeros([400,400,3],dtype=np.uint8)
pixels[:,:] = [0, 128, 255]
print(pixels[:,:])

img = Image.fromarray(pixels)
img.show()
#plt.imshow(img)
#plt.show()

