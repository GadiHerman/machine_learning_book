def SignCheck(x):
    if x > 0:
        return "positive"
    elif x < 0:
        return "negative"
    else:
        return "zero"

for i in [-2,0,10,-10,0,3]:
    print(i, "is", SignCheck(i))