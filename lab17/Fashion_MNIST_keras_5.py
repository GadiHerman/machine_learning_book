from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
 
fashion_mnist = keras.datasets.fashion_mnist
(train_data, train_lbl), (test_data, test_lbl) = fashion_mnist.load_data()
 
train_data = train_data / 255.0
test_data = test_data / 255.0
 
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
 
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
 
model.fit(train_data, train_lbl, epochs=10)