from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

pixels =[
            [   [255,0,0],[255,255,255],[0,0,0],[0,255,0],[255,0,255]             ],
            [   [255,255,0],[0,255,255],[0,0,255],[100,100,100],[50,50,50]  ]
        ] 

array = np.array(pixels, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save("MyPic.jpg")
plt.imshow(new_image)
plt.show()