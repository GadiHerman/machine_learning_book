import numpy as np

class point(object):
    def __init__(self,m=1,b=0):
        self.x = np.random.uniform(-1,1)
        self.y = np.random.uniform(-1,1)
        if (self.x)*m+b > self.y:
            self.label = 1
        else:
            self.label = -1
    def __repr__(self):
        return "\tx="+str(self.x)+"\ty="+str(self.y)+"\tlabel=   "+str(self.label)+"\n"

class listOfpoint:
    def __init__(self,numberOfPoints,m=1,b=0):
        self.points = []
        for _ in range(numberOfPoints):
            self.points.append(point(m,b))
        self.allXY=[]
        self.allLBL=[]
        for item in self.points:
            tmpXY = np.array([item.x , item.y])
            tmpLBL = np.array([item.label])
            self.allXY.append(tmpXY)   
            self.allLBL.append(tmpLBL)
        self.allXY=np.array(self.allXY)
        self.allLBL=np.array(self.allLBL)

#------Test The Point Class-----------------
MyPoints = listOfpoint(10,2,0.5)
print(MyPoints.points)
