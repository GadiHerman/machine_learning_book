from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
 
dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")
 
X = dataset[:,0:8]
Y = dataset[:,8]
 
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()
 
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
 
model.fit(X, Y, epochs=100, batch_size=5, verbose=2)
 
#scores = model.evaluate(X, Y, verbose=2)
#print("accuracy:", scores[1])
 
model.save("model.h5")
print("Saved model to in file: model.h5")
