from PIL import Image
import numpy as np

sea_list = list()
land_list = list()

for i in range(10):
    img = Image.open("data/sea" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    sea_list.append(data[:,:,1].sum() / data[:,:,1].size)
    
    img = Image.open("data/land" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    land_list.append(data[:,:,1].sum() / data[:,:,1].size)

print("\nsea_list:\n",sea_list)
print("\nland_list:\n",land_list,"\n")
