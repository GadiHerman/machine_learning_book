from keras.datasets import cifar10

print("Loading data...")
(train_data, train_lbl), (test_data, test_lbl) = cifar10.load_data()
print(len(train_data), "train data")
print(len(test_data), "test data")

# from keras.utils import np_utils
# # convert class vectors to binary vectors
# Y_train = np_utils.to_categorical(y_train)
# Y_test = np_utils.to_categorical(y_test)

print("train_data shape:", train_data.shape)
print("train_lbl shape:", train_lbl.shape)
print("test_data shape:", test_data.shape)
print("test_lbl shape:", test_lbl.shape)