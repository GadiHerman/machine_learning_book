from PIL import Image
img = Image.open("data/train.jpg")
data = img.getdata()
for i in range(100):
    print("pixel", i , "=" , data[i])

