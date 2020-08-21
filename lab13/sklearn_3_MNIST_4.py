import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier

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
print("\ntype: ", type(data))
print("\ntype: ", data.files)
x_mnist = data["x"]
x_mnist = x_mnist / 255
y_mnist = data["y"]

train_data, train_lbl = x_mnist[:60000], y_mnist[:60000]
test_data, test_lbl = x_mnist[60000:70000], y_mnist[60000:70000]

plt.figure()
for i in range(200):
    plt.subplot(10,20,i+1)
    plt.axis("off")
    plt.imshow(train_data[i].reshape((28,28))*255,cmap="gray", vmin=0, vmax=255)
plt.show()

def image_show(arr):
    two_d = (np.reshape(arr, (28, 28)) * 255).astype(np.uint8)
    plt.axis('off')
    plt.imshow(two_d, interpolation="nearest")
    plt.show()

image_show(test_data[0])
image_show(test_data[1])

mlp = MLPClassifier(hidden_layer_sizes=(50,), max_iter=20, alpha=1e-4,
                    solver='sgd', verbose=10, tol=1e-4, random_state=1,
                    learning_rate_init=.1)

mlp.fit(train_data, train_lbl)
print("Training set score: %f" % mlp.score(train_data, train_lbl))
print("Test set score: %f" % mlp.score(test_data, test_lbl))

print("\nTest data: ",test_lbl[:30])
newp = mlp.predict(test_data[:30])
print ("\nPredict data: ",newp)