from PIL import Image
img = Image.open("data/train.jpg")
width, height = img.size
area = (500, 580, 640, 650) 
img_crop = img.crop(area)

data = img_crop.getdata()
BIN = []
for i in data:
    avg = (i[0]+i[1]+i[2])/3
    if avg<60:
        BIN.append((255, 255, 255))
    else:
        BIN.append((0, 0, 0))
width, height = img_crop.size
imgBIN = Image.new(mode = "RGB", size = (width, height))
imgBIN.putdata(BIN)
newsize = (width*3, height*3) 
imgBIN = imgBIN.resize(newsize) 
imgBIN.show()