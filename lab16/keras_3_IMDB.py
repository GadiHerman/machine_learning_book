from keras.datasets import imdb
# from heapq import nlargest 
from heapq import nsmallest

index = imdb.get_word_index()
index = {k:(v+3) for k,v in index.items()}
index["<PAD>"] = 0
index["<START>"] = 1
index["<UNK>"] = 2

MostPopular = nsmallest(100, index, key = index.get) 
for val in MostPopular: 
    print(val, ":", index.get(val)) 