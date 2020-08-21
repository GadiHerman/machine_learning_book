from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
 
fashion_mnist = keras.datasets.fashion_mnist
(train_data, train_lbl), (test_data, test_lbl) = fashion_mnist.load_data()
 
plt.figure()
plt.imshow(train_data[0], cmap='Greys')
plt.colorbar()
plt.grid(False)
plt.show()
 
train_data = train_data / 255.0
 
plt.figure()
plt.imshow(train_data[0], cmap='Greys')
plt.colorbar()
plt.grid(False)
plt.show()