from PIL import Image
img = Image.open("All_Data/data/train.jpg") 

img1 = img.convert("L")
img2 = img.convert("1")
img1.show()
img2.show()

data = img.getdata()
for i in range(100):
    print("pixel", i , "=" , data[i])

data = img1.getdata()
for i in range(100):
    print("pixel", i , "=" , data[i])

data = img2.getdata()
for i in range(10000):
    print(data[i] , end=' ')
