import numpy as np
import matplotlib.pyplot as plt

class point(object):
    def __init__(self,m=1,b=0):
        self.x = np.random.uniform(-1,1)
        self.y = np.random.uniform(-1,1)
        if (self.x)*m+b > self.y:
            self.label = 1
        else:
            self.label = -1

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

    
    def drawTrainingPoints(self):
        '''
        Draw the training inputs and the training label
        '''
        categories = []
        colormap = np.array(['r', 'g'])
        px = []
        py = []
        for i in range(len(self.points)):
            px.append(self.points[i].x)
            py.append(self.points[i].y)
            if self.points[i].label > 0:
                categories.append(0)
            else:
                categories.append(1)      
        plt.scatter(px, py, s=10, c=colormap[categories])
        plt.axis([-1, 1, -1, 1])
        plt.show()

    def drawMistakesPoints(self,predict_values):
        '''
        Draw a comparison of the correct answers to the mistakes
        '''
        colormap1 = np.array(['r', 'g'])
        colormap2 = np.array(['w', 'b'])
        #Draw the correct answers
        categories = []
        for i in range(len(self.allXY)): 
            if self.points[i].label > 0:
                categories.append(0)
            else:
                categories.append(1) 
            
        plt.scatter(self.allXY[:, 0],self.allXY[:, 1], s=40, c=colormap1[categories])
        #-------------------------------------------------
        categories = []
        for i in range(len(predict_values)):
            if predict_values[i] > 0.5:
                categories.append(0)
            else:
                categories.append(1)
        plt.scatter(self.allXY[:, 0],self.allXY[:, 1], s=10, c=colormap2[categories])      
        plt.axis([-1, 1, -1, 1])
        plt.show()



#------Test The Point Class-----------------
MyPoints = listOfpoint(2000,-1,0)
MyPoints.drawTrainingPoints()

