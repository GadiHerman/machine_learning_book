from PIL import Image
 
img = Image.open("All_Data/data/train.jpg") 
width, height = img.size
print(width, height)
img.show()
