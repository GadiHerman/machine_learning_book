import numpy as np

x = np.array([2, 4, 6, 8, 10])
print(type(x))
print(x.shape)
print(x[0], x[1], x[4])
x[0] = 5
print(x)



#not in the book, gadi add it זה קשור לתוספת בפרק 7
for i in range(len(x)): 
    xi = x[i]
    print("x[",i,"]=",xi)

#not in the book, gadi add it זה קשור לתוספת בפרק 7
x = np.append(x,12)
print(x)
x = np.append(x,np.array([13, 14]))
print(x)

