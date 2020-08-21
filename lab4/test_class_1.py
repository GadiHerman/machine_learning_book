class MyPoint(object):
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def addX(self, x):
        self.x += x

    def addY(self, y):
        self.y += y

p=MyPoint(0,0)
p.x=100
p.y=100
p.addX(-10)
p.addY(10)
print("obj p:  x=",p.x,"y=",p.y)

Points_list = []

for i in range(10):
    p=MyPoint(i,i)
    p.addX(-10)
    p.addY(10)
    p.x=100
    Points_list.append(p)

for obj in Points_list:
    print("x=",obj.x,"y=",obj.y)
