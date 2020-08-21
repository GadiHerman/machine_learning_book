from PIL import Image
import numpy as np
img = Image.open("All_Data/data/train.jpg")
pix = np.array(img)
print(pix[0:10])
pixbg = 1.0 * (pix > 60)
img1 = Image.fromarray(pixbg, 'RGB')
# img1.save('my.png')
img1.show()




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

