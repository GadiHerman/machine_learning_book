import _pickle as pickle
import numpy as np
import os
import matplotlib.pyplot as plt

imageid = int(input("Enter index image in cifar10 test data [0 - 9999]: "))

f1 = open("CIFAR10dataset/test_batch", 'rb')
data = pickle.load(f1, encoding='bytes')
f2 = open("CIFAR10dataset/batches.meta", 'rb')
meta = pickle.load(f2, encoding='bytes')

im = data[b'data'][imageid, :]

im_r = im[0:1024].reshape(32, 32)
im_g = im[1024:2048].reshape(32, 32)
im_b = im[2048:].reshape(32, 32)
img = np.dstack((im_r, im_g, im_b))

print("label: ", data[b'labels'][imageid])
print("category:", meta[b'label_names'][data[b'labels'][imageid]])         

plt.imshow(img) 
plt.show()