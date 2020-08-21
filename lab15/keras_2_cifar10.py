import _pickle as pickle

f = open("Data/CIFAR10dataset/batches.meta", 'rb')
meta = pickle.load(f, encoding='bytes')

print("category:", meta[b'label_names'])
