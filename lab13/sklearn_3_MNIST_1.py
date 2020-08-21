import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

print("downloading file...")
x_mnist, y_mnist = fetch_openml("mnist_784", version=1, return_X_y=True, data_home=".")

def image_show(arr):
    p = (np.reshape(arr, (28, 28))).astype(np.uint8)
    plt.axis('off')
    plt.imshow(p)
    plt.show()

image_show(x_mnist[0])
image_show(x_mnist[1])
image_show(x_mnist[59999])

