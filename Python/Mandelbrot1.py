from graphics import *
import cmath
import math

maxIteration = 1000
winWidth = 1250
winHeight = 1000
xMin = -0.5
xMax = 2
yMin = -1
yMax = 1

aScalar = (xMax-xMin)/winWidth
bScalar = (yMax-yMin)/winHeight

win = GraphWin("graphics", winWidth, winHeight)
win.setCoords(xMin, yMin, xMax, yMax)

for a in range(winWidth-1):
    for b in range(winHeight-1):
        iteration = 0
        fx = coord = complex(xMin+a*aScalar, yMin+b*bScalar)
        while(iteration < maxIteration and abs(fx) < 2):
                fx = fx**2 - coord
                iteration += 1
        if(abs(fx) < 2):
                win.plot(coord.real, coord.imag)
