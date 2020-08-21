from PIL import Image
img = Image.open("data/train.jpg")
width, height = img.size
data = img.getdata()
R = []
G = []
B = []
for i in data:
    R.append((i[0], 0, 0))
    G.append((0, i[1], 0))
    B.append((0, 0, i[2]))
# data_jpg = list(img.getdata())
# print(data_jpg[:10])
# print(R[:10])
# print(G[:10])
# print(B[:10])
imgR = Image.new(mode = "RGB", size = (width, height))
imgG = Image.new(mode = "RGB", size = (width, height))
imgB = Image.new(mode = "RGB", size = (width, height))
imgR.putdata(R)
imgG.putdata(G)
imgB.putdata(B)
imgR.show()
imgG.show()
imgB.show()