def SignCheck(x):
    if x > 0:
        print(x,"is positive") 
    elif x < 0:
        print(x,"is negative") 
    else:
        print(x,"is zero") 

SignCheck(-10)

for i in [-2,0,10,-10,0,3]:
    SignCheck(i)