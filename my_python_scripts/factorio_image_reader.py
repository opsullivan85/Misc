from PIL import Image
import numpy as np

img = np.array(Image.open("img.png"))
num = 0
print(img.shape)

for col in range(img.shape[0]):
    num = -0
    for row in range(img.shape[1]):
        num += np.array_equal(img[col, row], [255, 255, 255, 255])
        num = num << 1
    num = num << 31 - img.shape[1]
    print(num)
    
