import numpy as np
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("\nprint all:\n",x)
print("start=1:stop=7:step=no ",x[1:7])
print("start=5:stop=no:step=no ",x[5:])
print("start=no:stop=5:step=no ",x[:5])
print("start=1:stop=7:step=2 ",x[1:7:2])
print("start=no:stop=no:step=-1 ",x[::-1])
print("start=-3:stop=-6:step=-1 ",x[-3:-6:-1])

x2 = np.array([ [1,2,3,4,5],
                [6,7,8,9,10],
                [11,12,13,14,15],
                [16,17,18,19,20],
                [21,22,23,24,25] ])
print("\nprint all:\n",x2)
print("FROM:start=1:stop=4:step=no TO:start=1:stop=4:step=no\n",x2[1:4,1:4])
print("FROM:start=2:stop=no:step=no TO:start=2:stop=no:step=no\n",x2[2:,2:])
print("FROM:start=no:stop=no:step=2 TO:start=no:stop=no:step=2\n",x2[::2,::2])
print("FROM:start=no:stop=no:step=-1 TO:start=no:stop=no:step=-1\n",x2[::-1,::-1])
print("FROM:start=-2:stop=no:step=-1 TO:start=-2:stop=no:step=-1\n",x2[-2::-1,-2::-1])
