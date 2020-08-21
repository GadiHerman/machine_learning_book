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

train_data = train_data / 255.0

plt.figure()
for i in range(70):
    plt.subplot(7,10,i+1)
    plt.axis("off")
    plt.imshow(train_data[i], cmap='Greys')
    plt.title(lbls[train_lbl[i]], fontsize=10)
plt.show()

#  plt.figure()
# for i in range(100):
#     plt.subplot(10,10,i+1)
#     plt.axis("off")
#     plt.title(train_lbl[i])
#     plt.imshow(train_data[i].reshape((120,320)),cmap="gray", vmin=0, vmax=255)
# plt.show()


# plt.figure()
# plt.imshow(train_data[0], cmap='Greys')
# plt.title(lbls[train_lbl[0]])
# plt.show()