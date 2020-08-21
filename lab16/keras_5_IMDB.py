import numpy as np
from keras import models
from keras import layers
from keras.datasets import imdb
# from nltk import word_tokenize
# from keras.preprocessing import sequence

TOP_WORDS = 10000

def Convert_to_vectors(data_list, dimension = TOP_WORDS):
    out = np.zeros((len(data_list), dimension))
    for i, sequence in enumerate(data_list):
        out[i, sequence] = 1
    return out

(train_data, train_lbl), (test_data, test_lbl) = imdb.load_data(num_words=TOP_WORDS)
# print(train_data[0])
train_data = Convert_to_vectors(train_data)
test_data = Convert_to_vectors(test_data)
# print(train_data[0])

model = models.Sequential()
model.add(layers.Dense(50, activation = "relu", input_shape=(TOP_WORDS, )))
model.add(layers.Dropout(0.3, noise_shape=None, seed=None))
model.add(layers.Dense(50, activation = "relu"))
model.add(layers.Dropout(0.2, noise_shape=None, seed=None))
model.add(layers.Dense(50, activation = "relu"))
model.add(layers.Dense(1, activation = "sigmoid"))
model.summary()

model.compile(
            optimizer = "adam",
            loss = "binary_crossentropy",
            metrics = ["accuracy"]
            )

results = model.fit(
                    train_data, train_lbl,
                    epochs= 5,
                    batch_size = 10,
                    validation_data = (test_data, test_lbl)
                    )

print("Test-loss:", results.history["loss"])
print("Test-Accuracy:", results.history["accuracy"])