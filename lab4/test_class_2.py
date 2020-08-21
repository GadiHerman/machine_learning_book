class MyPoint(object):
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

    def addX(self, x):
        self.x += x

    def addY(self, y):
        self.y += y

p1=MyPoint(5,5)
p1.x=100
p1.y=100
p1.addX(-10)
p1.addY(10)
print("obj p1:  x=",p1.x,"y=",p1.y)

p2=MyPoint()
p2.addX(-10)
p2.addY(10)
print("obj p2:  x=",p2.x,"y=",p2.y)
 
Points_list = []

for i in range(5):
    p=MyPoint(i,i)
    p.addX(-10)
    p.addY(10)
    p.x=100
    Points_list.append(p)

for obj in Points_list:
    print("x=",obj.x,"y=",obj.y)
