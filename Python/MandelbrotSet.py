import math
import cmath
from graphics import *

height = 500
width = 500



win = GraphWin("Graphics Window", width, height)
win.setCoords(-width/2,-height/2,width/2,height/2)

#Line(Point(0,width/2),Point(0,-width/2)).draw(win)
#Line(Point(-height/2,0),Point(height/2,0)).draw(win)

coord = 0

for a in range(-width//2, width//2):
    for b in range(-height//2, height//2):
        coord = complex(4.0*a/height, 4.0*b/width)
        #print(coord)
        fx = coord
        iteration = 0
        while(iteration < 10000 and abs(fx) < 2):
            #print(fx)
            fx = fx**2 - coord
            iteration += 1
        #print("\n\n")
        if(abs(fx) < 2):
            Point(a, b).draw(win)
