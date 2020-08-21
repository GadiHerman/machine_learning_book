import numpy as np
from keras.datasets import imdb
from nltk import word_tokenize
# from keras.preprocessing import sequence
import string

# for i, sequence in enumerate("i love this movie"):
#     print(i,sequence)

def Preparing_string(text_string, dimension = 40):

    text_string = text_string.lower()
    table = str.maketrans(dict.fromkeys(string.punctuation))
    text_string = text_string.translate(table)

    word2index = imdb.get_word_index()
    test=[]
    for word in word_tokenize(text_string):
        test.append(word2index[word])
    print(text_string)
    print(test)

    out = np.zeros(dimension)
    for _ , sequence in enumerate(test):
        if sequence < dimension:
            out[sequence] = 1
    print ("\nOutput:",out)

Preparing_string("First off, this is NOT a war film. It is a movie about the bond of men in war. It is by far the best movie I've seen in a very, very long time. I had high expectations and was not disappointed. At first I was eager to see the one shot idea Sam Mendes went into this with but, after awhile, I stopped paying attention to that. While everything about the movie was well done I was so caught up in the two central characters that nothing else mattered. I will watch this again and again.")
