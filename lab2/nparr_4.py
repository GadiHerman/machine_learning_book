import numpy as np
a = np.zeros((4,4))
print("np.zero:\n",a)

b = np.ones((1,8))
print("np.ones:\n",b)

c = np.full((2,2), 7)
print("np.full:\n",c)

d = np.eye(5,5)
print("np.eye:\n",d)

e = np.random.uniform(size=[3,5])
print("uniform(size=[3,5]):\n",e)

f = np.random.uniform(-1,1,size=[2,4])
print("uniform(-1,1,size=[2,4]):\n",f)
