from PIL import Image
import numpy as np

img = Image.open("sea1.jpg")
img.load()
sea0 = np.array(img, dtype=np.uint8)
print(sea0.shape)

print ("sea1 - Green =" , sea0[:,:,1].sum() / sea0[:,:,1].size)
print ("sea1 - blue =" , sea0[:,:,2].sum() / sea0[:,:,2].size)

img = Image.open("land1.jpg")
img.load()
land0 = np.array(img, dtype=np.uint8)

print ("land1 - Green =" , land0[:,:,1].sum() / land0[:,:,1].size)
print ("land1 - blue =" , land0[:,:,2].sum() / land0[:,:,2].size)