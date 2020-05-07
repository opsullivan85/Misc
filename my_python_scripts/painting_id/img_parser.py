import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
import cv2

class im_parser:
    def __init__(self, f_name, block_size = 1000):
        self.im = cv2.imread(f_name, 1)
        self.block_size = block_size
        

    def crop_to_centered_square(self):
        short_side = min(self.im.size)
        side_len = short_side - short_side % self.block_size
        center = (im.size[0] / 2, im.size[1] / 2)
        box = (center[0] - side_len / 2,
               center[1] - side_len / 2,
               center[0] + side_len / 2,
               center[1] + side_len / 2)
        
        self.im = self.im.crop(box)

    def crop_to_centered_rectangle(self):
        size = (im.size[0] % self.block_size, im.size[1] % self.block_size)
        center = (im.size[0] / 2, im.size[1] / 2)
        box = (center[0] - size[0] / 2,
               center[1] - size[1] / 2,
               center[0] + size[0] / 2,
               center[1] + size[1] / 2)

        self.im = self.im.crop(box)

    def edge_detect(self):
        self.im = cv2.GaussianBlur(self.im, (3, 3), 0)
        #self.im = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)
        self.im = cv2.Laplacian(self.im,cv2.CV_8U)

    def kernel(self, k):
        cv2.filter2D(self.im, 1, k)

    def to_gray(self):
        self.im = cv2.cvtColor(self.im, cv2.COLOR_BGR2GRAY)

    def show(self, resize = 1):
        #cv2.imshow('image',self.im)
        plt.imshow(cv2.resize(self.im, None, fx=resize, fy=resize)[:5000,:5000], cmap='gray')
        plt.xticks([]), plt.yticks([])
        plt.show()
#im
#i = im_parser('test_img.png', 1000)
i = im_parser('Starry_Night.jpg')
#i.show(1)
i.edge_detect()
#i.to_gray()
i.show(1)








