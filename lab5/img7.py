from PIL import Image
img = Image.open("data/train.jpg")
width, height = img.size
data = img.getdata()
BIN = []
for i in data:
    avg = int((i[0]+i[1]+i[2])/3)
    BIN.append((avg, avg, avg))

imgBIN = Image.new(mode = "RGB", size = (width, height))
imgBIN.putdata(BIN)
imgBIN.show()




# img = Image.open("data/train.jpg") 
# width, height = img.size
# img45 = img.rotate(45)
# area = (width/2-200, height/2-200, width/2+200, height/2+200) 
# img_crop = img.crop(area)
# newsize = (width//4, height//4) 
# img_resize = img.resize(newsize) 
# img_transpose = img.transpose(Image.FLIP_LEFT_RIGHT)

# img45.save("data/train45.jpg")
# img_crop.save("data/train_cropped.jpg") 
# img_resize.save("data/train_resized.jpg")
# print("Old image size:", img.size)
# print("New image size:", img_resize.size)
# img45.show()
# img_crop.show()
# img_resize.show()
# img_transpose.show()

