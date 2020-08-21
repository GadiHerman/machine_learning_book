def NewDiv(x,y):
    a=x//y
    b=x%y
    return a , b

n1,n2 = NewDiv(14,4)
print(n1,n2)

for x in [[4, 2],[7,3]]:
    print(NewDiv(x[0],x[1]))