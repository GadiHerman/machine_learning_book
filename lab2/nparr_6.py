import numpy as np
# x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# a = np.reshape(x,(5, 2))
# print("reshape(x,(5, 2)):\n",a)
# b = np.reshape(x,(10, 1))
# print("reshape(x,(10, 1)):\n",b)
# c = np.reshape(x,(2, 5))
# print("reshape(x,(2, 5)):\n",c)

x2 = np.array([[1,2,3,4], [5,6,7,8]])
d = np.reshape(x2,8)
print("reshape(x2,8):\n",d)
e = np.reshape(x2,(8,1))
print("reshape(x2,(8,1)):\n",e)
f = np.reshape(x2,(x2.shape[0]*x2.shape[1], 1))
print("reshape(x2,(x2.shape[0]*x2.shape[1], 1)):\n",f)


# x2 = np.array([ [1,2,3,4,5],
#                 [6,7,8,9,10],
#                 [11,12,13,14,15],
#                 [16,17,18,19,20],
#                 [21,22,23,24,25] ])
# print("\nprint all:\n",x2)
# print("FROM:start=1:stop=4:step=no TO:start=1:stop=4:step=no\n",x2[1:4,1:4])
# print("FROM:start=2:stop=no:step=no TO:start=2:stop=no:step=no\n",x2[2:,2:])
# print("FROM:start=no:stop=no:step=2 TO:start=no:stop=no:step=2\n",x2[::2,::2])
# print("FROM:start=no:stop=no:step=-1 TO:start=no:stop=no:step=-1\n",x2[::-1,::-1])
# print("FROM:start=-2:stop=no:step=-1 TO:start=-2:stop=no:step=-1\n",x2[-2::-1,-2::-1])
