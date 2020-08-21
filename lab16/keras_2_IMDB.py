from keras.datasets import imdb

(train_data, train_lbl), (test_data, test_lbl) = imdb.load_data(num_words=10000)

print("\n",train_data[123])

index = imdb.get_word_index()
index = {k:(v+3) for k,v in index.items()}
index["<PAD>"] = 0
index["<START>"] = 1
index["<UNK>"] = 2

id_to_word = {value:key for key,value in index.items()}
print(" ".join(id_to_word[id] for id in train_data[123] ))
