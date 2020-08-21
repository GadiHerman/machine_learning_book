from keras.models import model_from_json
from keras.optimizers import Adam
from keras.preprocessing import image
import matplotlib.pyplot as plt

# Load the Neuron network training from 2 files
model_architecture = "C:/saved_models/CIFAR10model.json"
model_weights = "C:/saved_models/CIFAR10weights.h5"
model = model_from_json(open(model_architecture).read())
model.load_weights(model_weights)

# Lode the image from my computer and do customize
MyPIC = image.load_img('C:/saved_models/dog.jpg', target_size=(32,32))
plt.imshow(MyPIC)
plt.show()
MyPIC = image.img_to_array(MyPIC)
MyPIC = MyPIC.reshape((1,) + MyPIC.shape)
MyPIC = MyPIC/255.

# Compile the neuron network model
model.compile(	loss="categorical_crossentropy", 
				optimizer=Adam(lr=1.0e-4),
				metrics=["accuracy"])

# Predicting the image
predictions = model.predict_classes(MyPIC)
print(predictions)

# 0 : airplane
# 1 : automobile
# 2 : bird
# 3 : cat
# 4 : deer
# 5 : dog
# 6 : frog
# 7 : horse
# 8 : ship
# 9 : truck