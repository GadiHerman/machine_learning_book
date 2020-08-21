import numpy as np
from termcolor import colored

vir_iris_data = np.genfromtxt('data/iris_for_ML.csv', delimiter=',')

random_iris_data = np.random.permutation(vir_iris_data)


test_data = random_iris_data[0:10,:4]
train_data = random_iris_data[10:,:4]

test_lbl = random_iris_data[0:10,4:]
train_lbl = random_iris_data[10:,4:]

tmp=[]
for i in range(len(test_lbl)):
    if test_lbl[i] == 1:
        t = np.array([1,0,0])
    elif test_lbl[i] == 2:
        t = np.array([0,1,0])
    else:
        t = np.array([0,0,1])  
    tmp.append(t)   
new_test_lbl=np.array(tmp)

tmp=[]
for i in range(len(train_lbl)):
    if train_lbl[i] == 1:
        t = np.array([1,0,0])
    elif train_lbl[i] == 2:
        t = np.array([0,1,0])
    else:
        t = np.array([0,0,1])  
    tmp.append(t)   
new_train_lbl=np.array(tmp)




print("\nrandom_iris_data: \n",colored(random_iris_data, 'red'),"\n")
print("\ntest_data: \n",colored(test_data, 'green'),"\n")
print("\ntrain_data: \n",colored(train_data, 'blue'),"\n")
print("\ntest_lbl: \n",colored(test_lbl, 'green'),"\n")
print("\nnew_test_lbl: \n",colored(new_test_lbl, 'green'),"\n")
print("\ntrain_lbl: \n",colored(train_lbl, 'blue'),"\n")
print("\nnew_train_lbl: \n",colored(new_train_lbl, 'blue'),"\n")


# A = np.random.randint(100, size=(10,3))
# print("\nA: ",A,"\n")
# idx = np.random.permutation(A)
# print("\nidx: ",idx,"\n")