import numpy as np
from keras.utils import to_categorical
from keras import models
from keras import layers
from keras.datasets import imdb
from nltk import word_tokenize
import string
import nltk
nltk.download('punkt')

TOP_WORDS = 10000

def Preparing_string(text_string, dimension = TOP_WORDS):
    text_string = text_string.lower()
    table = str.maketrans(dict.fromkeys(string.punctuation))
    text_string = text_string.translate(table)

    word2index = imdb.get_word_index()
    test=[]
    for word in word_tokenize(text_string):
        test.append(word2index[word])

    results = np.zeros(dimension)
    for _ , sequence in enumerate(test):
        if sequence < dimension:
            results[sequence] = 1

    # print("\nOriginal string:", text_string,"\n")
    # print("\nIndex conversion:", test,"\n")
    results = np.reshape(results,(1, TOP_WORDS))
    # print("\nConvert to vectors:", results,"\n")
    return results

def Convert_to_vectors(sequences, dimension = TOP_WORDS):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results

(training_data, training_targets), (testing_data, testing_targets) = imdb.load_data(num_words=TOP_WORDS)
data = np.concatenate((training_data, testing_data), axis=0)
targets = np.concatenate((training_targets, testing_targets), axis=0)

data = Convert_to_vectors(data)
# targets = np.array(targets).astype("float32")
test_x = data[:5000]
test_y = targets[:5000]
train_x = data[5000:]
train_y = targets[5000:]

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
                    train_x, train_y,
                    epochs= 10,
                    batch_size = 500,
                    validation_data = (test_x, test_y)
                    )

print("Test-val_loss:", results.history["val_loss"])
print("Test-val_accuracy:", results.history["val_accuracy"])
print("Test-loss:", results.history["loss"])
print("Test-Accuracy:", results.history["accuracy"])


data_string = Preparing_string("First off, this is NOT a war film. It is a movie about the bond of men in war. It is by far the best movie I've seen in a very, very long time. I had high expectations and was not disappointed. At first I was eager to see the one shot idea Sam Mendes went into this with but, after awhile, I stopped paying attention to that. While everything about the movie was well done I was so caught up in the two central characters that nothing else mattered. I will watch this again and again.")
print("predict:",model.predict(data_string))
print("predict_classes:",model.predict_classes(data_string))
print("------1 is Good-------\n")
data_string = Preparing_string("One of the best films I've seen in a long while. Worth seeing on a big screen. Cinematography is outstanding, the one shot process really makes you feel as though you are there. The two leading actors really grasped the concept that human contact can be so strong, especially in such awful situations as war. Insightful, moving and an overall amazing watch.")
print("predict:",model.predict(data_string))
print("predict_classes:",model.predict_classes(data_string))
print("------1 is Good-------\n")
data_string = Preparing_string("I felt dirty, I felt tired, I felt hungry, I felt a will to succeed and I felt sadness when I was watching the movie. It felt like I was also fighting to reach Colonel MacKenzie for two hours. Several hours later after my emotions are still outside my body. Fantastic photo and music. Good casting of staff. The movie is just perfect!")
print("predict:",model.predict(data_string))
print("predict_classes:",model.predict_classes(data_string))
print("------1 is Good-------\n")
data_string = Preparing_string("I don't feel like I know the characters at all. I have no idea why the two soldiers were friends or what they had been through together. The cinematography tried so hard to make this an emotional shocking movie that it had the opposite effect. War scenes with gratuitous up close views of corpses and body parts that don't add anything to the story got old quick.")
print("predict:",model.predict(data_string))
print("predict_classes:",model.predict_classes(data_string))
print("------0 is Bad-------\n")
data_string = Preparing_string("Predictable and horrendous. The acting was terrible and the story was common and nonsense. The only exciting part about the movie was the very end when finally people were dying and it represented WW1. I highly doubt he met a strange woman with an abandoned child and I highly doubt any of this even happened. This movie was Saving Private Ryan, but boring and predictable.")
print("predict:",model.predict(data_string))
print("predict_classes:",model.predict_classes(data_string))
print("------0 is Bad-------\n")