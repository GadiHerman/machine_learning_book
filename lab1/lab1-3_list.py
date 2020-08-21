import matplotlib.pyplot as plt
x=[]
y1=[]
y2=[]
for i in range(0,30):
    x.append(i/10)
    y1.append(pow(i/10,2))
    y2.append(pow(i/10,3))
print(x,y1,y1)
plt.plot(x, y1, 'r--')
plt.plot(x, y2, 'g^')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
