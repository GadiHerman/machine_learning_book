# https://github.com/PacktPublishing/Deep-Learning-with-Keras/blob/master/Chapter03/keras_CIFAR10_simple.py

from keras.datasets import cifar10
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.optimizers import Adam
import matplotlib.pyplot as plt

# Download the photos and Tags to my computer and customize them
(train_data, train_lbl), (test_data, test_lbl) = cifar10.load_data()
print("train_data shape:", train_data.shape)
print(train_data.shape[0], "train samples")
print(test_data.shape[0], "test samples")
Y_train = np_utils.to_categorical(train_lbl, 10)
Y_test = np_utils.to_categorical(test_lbl, 10) 
train_data = train_data.astype("float32")
test_data = test_data.astype("float32")
train_data /= 255
test_data /= 255

# Building the neuron network model
model = Sequential()
model.add(Conv2D(32, (3, 3), activation="relu", padding="same", input_shape=(32,32,3)))    
model.add(Conv2D(32, (3, 3), activation="relu"))    
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), activation="relu", padding="same"))    
model.add(Conv2D(64, (3, 3), activation="relu"))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(10, activation="softmax"))
model.summary()

# Compile the neuron network model
model.compile(	loss="categorical_crossentropy", 
				optimizer=Adam(lr=1.0e-4),
				metrics=["accuracy"])

# Neuron network training
results = model.fit(train_data, Y_train, 
					batch_size=128,
					epochs=1, 
					validation_split=0.2,
					validation_data= (test_data, Y_test), 
					verbose=1)

# Saving the Neuron network training into 2 files
model_json = model.to_json()
open("C:/saved_models/CIFAR10model.json", "w").write(model_json)
model.save_weights("C:/saved_models/CIFAR10weights.h5", overwrite=True)

# Creating the system learning graph
plt.plot(results.history["val_accuracy"])
plt.ylabel("accuracy")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper right")
plt.show()
plt.plot(results.history["loss"])
plt.plot(results.history["val_loss"])
plt.ylabel("loss")
plt.xlabel("epoch")
plt.legend(["train", "test"], loc="upper right")
plt.show()