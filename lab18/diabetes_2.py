from numpy import loadtxt
import numpy as np
from keras.models import load_model
 

model = load_model('model.h5')
# model.summary()

dataset = loadtxt("pima-indians-diabetes.csv", delimiter=",")
X = dataset[:,0:8]
Y = dataset[:,8]
for i in range(20,23):
    print ("data=",X[i],"------",Y[i]) 


Pregnancies = float(input("Pregnancies: "))
Glucose = float(input("Glucose: "))
BloodPressure = float(input("BloodPressure: "))
SkinThickness = float(input("SkinThickness: "))
Insulin = float(input("Insulin: "))
BMI = float(input("BMI: "))
DiabetesPadigreeFunction = float(input("Diabetes Padigree Function: "))
Age = float(input("Age: "))
t = np.array([  Pregnancies,Glucose,
                BloodPressure,SkinThickness,
                Insulin,BMI,
                DiabetesPadigreeFunction,Age
            ],ndmin=2)
prediction = model.predict(t)
print ("You have", str(prediction[0]*100) ,"percent chance of getting diabetes")