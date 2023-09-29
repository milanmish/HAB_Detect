import PIL
import cv2
from PIL import Image
import numpy as np


img = PIL.Image.open('testing.jpg')
imSize = (cv2.imread('testing.jpg')).shape
pix = img.load()

for y in range(imSize[1]):
    for x in range(imSize[0]):
        print(x,y)
        r = pix[x,y][0]
        g = pix[x,y][1]
        b = pix[x,y][2]
        pix[x,y] = (r, g, b)
        if g + r - b == 0:
            ADVI = (g - r) / (0.1)
        else:
            ADVI = (g - r) / (g + r - b)
        print(pix[x,y])
        print(ADVI)
        print('----------')