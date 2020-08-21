import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.datasets import fetch_openml

datapath = Path("mnist_784.npz")
if not(datapath.exists()):
    print("downloading file...")
    x_mnist, y_mnist = fetch_openml("mnist_784", version=1, return_X_y=True, data_home=".")
    x=np.array(x_mnist,dtype="u8")
    y=np.array(y_mnist,dtype="u8")
    np.savez(datapath,x=x,y=y)
    del x_mnist, y_mnist
print("Loading file...")
data = np.load(datapath)
# print("\ntype:\n", type(data))
# print("\nfiles:\n", data.files)
x_mnist = data["x"]
y_mnist = data["y"]
# print("\ntype:\n", type(x_mnist))

plt.figure()
for i in range(200):
    plt.subplot(10,20,i+1)
    plt.axis("off")
    plt.imshow(x_mnist[i].reshape((28,28)),cmap="gray", vmin=0, vmax=255)
plt.show()
