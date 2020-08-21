from PIL import Image
import numpy as np

pixels = np.zeros([100,200,3],dtype=np.uint8)
pixels[:,:100] = [255, 0, 0]
pixels[:,100:] = [0, 0, 255]
pixels[25:75,25:75] = [0, 0, 255]
pixels[25:75,125:175] = [255, 0, 0]
print(pixels.shape,type(pixels))
img = Image.fromarray(pixels)
img.show()


