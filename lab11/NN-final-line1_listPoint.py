import numpy as np

class listOfpoint:
    def __init__(self,numberOfPoints,m=1,b=0):
        self.points=np.random.uniform(-1,1,size=(numberOfPoints,2))
        self.labels=np.sign(self.points[:,1] - (m*self.points[:,0] + b))
        # colormap = np.array(['r', 'g'])
        # plt.scatter(self.points[:,0], self.points[:,1],s=10, c=colormap[1*(self.labels==1)])
        # plt.show()

    def __repr__(self):
        s=''
        for point,label in zip(self.points,self.labels):
            s += "\tx="+str(point[0])+"\ty="+str(point[1])+"\tlabel="+str(label)+"\n"
        return s

#------Test The Point Class-----------------
MyPoints = listOfpoint(10,2,0.5)
#print(MyPoints.points)
print(MyPoints)
