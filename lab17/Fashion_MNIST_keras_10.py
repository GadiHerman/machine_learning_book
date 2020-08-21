from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
import glob

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
            keras.layers.Dense(10, activation='softmax')])
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])
model.fit(train_data, train_lbl, epochs=50)

# Read all original images
file_list = glob.glob("C:/test_img/*.jpg")
x=[]
for each in file_list:
        img = image.load_img(each, color_mode = "grayscale", target_size=(28, 28))
        img = image.img_to_array(img)
        img = img.reshape(28, 28)
        img = img.astype('float32')
        img = (255-img)/255.0
        x.append(img)
        # plt.figure()
        # plt.imshow(img , cmap='Greys')
        # plt.grid(False)
        # plt.colorbar()
        # plt.show()
x=np.array(x)
result = model.predict_classes(x)
for i in range(len(result)):    
        print(lbls[result[i]], result[i])
print(result)
for i in range(len(result)):
        plt.figure()
        plt.imshow(x[i] , cmap='Greys')
        plt.grid(False)
        plt.axis('off')
        plt.colorbar()
        plt.title(lbls[result[i]])
        plt.show()    


