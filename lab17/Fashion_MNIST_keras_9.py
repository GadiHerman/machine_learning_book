import numpy as np
import matplotlib.pyplot as plt
from keras.preprocessing import image
import glob

file_list = glob.glob("C:/test_img/*.jpg")
x=[]
for each in file_list:
        img = image.load_img(each, color_mode = "grayscale", target_size=(28, 28))
        img = image.img_to_array(img)
        img = img.reshape(28, 28)
        img = img.astype('float32')
        img = (255-img)/255.0
        x.append(img)
        plt.figure()
        plt.imshow(img , cmap='Greys')
        plt.grid(False)
        plt.colorbar()
        plt.show()
x=np.array(x)