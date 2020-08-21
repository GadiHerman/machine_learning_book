from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

fashion_mnist = keras.datasets.fashion_mnist
(train_data, train_lbl), (test_data, test_lbl) = fashion_mnist.load_data()
lbls = ['T-shirt/top',
        'Trouser',
        'Pullover',
        'Dress',
        'Coat',
        'Sandal',
        'Shirt',
        'Sneaker',
        'Bag',
        'Ankle boot']

print("\ntrain images shape: ",train_data.shape)
print("\ntrain labels shape: ",train_lbl.shape)
print("\ntest images shape: ",test_data.shape)
print("\ntest labels shape: ",test_lbl.shape)

print("\n",np.where(train_data[0] > 128, 8, 1))
print("\n",lbls[train_lbl[0]])
print("\n train_lbl: ",train_lbl)

plt.figure()
plt.imshow(train_data[0], cmap='Greys')
plt.title(lbls[train_lbl[0]])
plt.show()

print(train_data[0].shape)