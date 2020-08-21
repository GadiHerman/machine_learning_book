from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

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
 
model.fit(train_data, train_lbl, epochs=3)

predictions = model.predict(test_data)
np.set_printoptions(precision=4, suppress=True)
print("\n   Show all network outlets: ",predictions[22])
predic = np.argmax(predictions[22])
print("\n   Show prediction: ", lbls[predic])
 
plt.figure()
plt.imshow(test_data[22],cmap='Greys')
plt.title(lbls[predic])
plt.grid(False)
plt.show()