import numpy as np 
class point(object):
    def __init__(self):
        self.x = np.random.uniform(-1,1)
        self.y = np.random.uniform(-1,1)
        if self.x > self.y:
            self.label = 1
        else:
            self.label = -1
    def __repr__(self):
        return "x="+str(self.x)+" y="+str(self.y)+" label="+str(self.label)+"\n"

p= point()
print(p)

Points_list = []
for i in range(10):
    Points_list.append(point())
print(Points_list)


