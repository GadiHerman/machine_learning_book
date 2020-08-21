from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

sea_colors = list()
for i in range(10):
    img = Image.open("data/sea" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    t= list()
    for i in range(3):
        t.append(data[:,:,i].sum() / data[:,:,i].size)
    sea_colors.append(t)

land_colors = list()
for i in range(10):
    img = Image.open("data/land" + str(i) + ".jpg")
    img.load()
    data = np.array(img, dtype=np.uint8)
    t= list()
    for i in range(3):
        t.append(data[:,:,i].sum() / data[:,:,i].size)
    land_colors.append(t)

sea_array = np.array(sea_colors)
land_array = np.array(land_colors)

# print(sea_array)
# print(land_array)

# red green
plt.subplot(131)
x1 = sea_array[:,0]
y1 = sea_array[:,1]
x2 = land_array[:,0]
y2 = land_array[:,1]
plt.plot(x1, y1, 'bo', x2, y2, 'r+')
plt.xlabel("red")
plt.ylabel("green")
plt.title("Sea or Land option 1")

# red blue
plt.subplot(132)
x1 = sea_array[:,0]
y1 = sea_array[:,2]
x2 = land_array[:,0]
y2 = land_array[:,2]
plt.plot(x1, y1, 'bo', x2, y2, 'r+')
plt.xlabel("red")
plt.ylabel("blue")
plt.title("Sea or Land option 2")

# green blue
plt.subplot(133)
x1 = sea_array[:,1]
y1 = sea_array[:,2]
x2 = land_array[:,1]
y2 = land_array[:,2]
plt.plot(x1, y1, 'bo', x2, y2, 'r+')
plt.xlabel("green")
plt.ylabel("blue")
plt.title("Sea or Land option 3")
plt.show()