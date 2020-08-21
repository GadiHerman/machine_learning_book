from keras.datasets import imdb

print('Loading data...')
(train_data, train_lbl), (test_data, test_lbl) = imdb.load_data(num_words=10000)
print(len(train_data), 'train data')
print(len(test_data), 'test data')