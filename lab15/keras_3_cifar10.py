import _pickle as pickle
import numpy as np
import matplotlib.pyplot as plt

imageid = int(input("Enter index image in cifar10 [0 - 49999]: "))
batch = (imageid // 10000) + 1
idx = imageid - (batch-1)*10000

f1 = open("Data/CIFAR10dataset/data_batch_" + str(batch), 'rb')
data = pickle.load(f1, encoding='bytes')
f2 = open("Data/CIFAR10dataset/batches.meta", 'rb')
meta = pickle.load(f2, encoding='bytes')

im = data[b'data'][idx, :]

im_r = im[0:1024].reshape(32, 32)
im_g = im[1024:2048].reshape(32, 32)
im_b = im[2048:].reshape(32, 32)
img = np.dstack((im_r, im_g, im_b))

print("label: ", data[b'labels'][idx])
print("category:", meta[b'label_names'][data[b'labels'][idx]])         

plt.imshow(img) 
plt.show()