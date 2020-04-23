import math
import cmath
from graphics import *

height = 500
width = 500

win = GraphWin("Graphics Window", width, height)
win.setCoords(-width/2,-height/2,width/2,height/2)

#Line(Point(0,width/2),Point(0,-width/2)).draw(win)
#Line(Point(-height/2,0),Point(height/2,0)).draw(win)

coords = [[0] * width] * height

for a in range(-width//2, width//2):
    for b in range(-height//2, height//2):
        coords[a][b] = complex(4.0*a/height, 4.0*b/width)

toDraw = []

for a in range(width-1):
    for b in range(height-1):
        coord = coords[a][b]
        iteration = 0
        fx = coord
        toDraw = []
        while(iteration < 10 and abs(fx) < 2):
            #print(fx.real*height/4%1)
            if(not(fx.real*width/4%1) and not(fx.imag*height/4%1)):
                toDraw.append(fx)
            fx = fx**2 - coord
            iteration += 1
        if(abs(fx) < 2):
            print(toDraw)
            for imgNum in toDraw:
                Point(imgNum.real*width/4, imgNum.imag*height/4).draw(win)
        
