from keras.datasets import imdb

(train_data, train_lbl), (test_data, test_lbl) = imdb.load_data(num_words=1000)
print(len(train_data), 'train data')
print(len(test_data), 'test data')

index = imdb.get_word_index()
index = {k:(v+3) for k,v in index.items()}
index["<PAD>"] = 0
index["<START>"] = 1
index["<UNK>"] = 2

id_to_word = {value:key for key,value in index.items()}
print(" ".join(id_to_word[id] for id in train_data[100] ))
print(train_lbl[100])


# print(type(index))
# print(len(index))


# from heapq import nlargest 
# from heapq import nsmallest
# from operator import itemgetter

# ThreeHighest = nsmallest(100, index, key = index.get) 
  
# print("Dictionary with 3 highest values:") 
# print("Keys: Values") 
  
# for val in ThreeHighest: 
#     print(val, ":", index.get(val)) 