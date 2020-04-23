from graphics import *
#from frange import *
import cmath
import math

maxIteration = 10
winWidth = 100
winHeight = 100
xMin = -1.
xMax = 1.
yMin = -1.
yMax = 1.

aScalar = (xMax-xMin)/winWidth
bScalar = (yMax-yMin)/winHeight

win = GraphWin("graphics", winWidth, winHeight)
win.setCoords(xMin, yMin, xMax, yMax)

computed = [[False] * winWidth ] * winHeight

tmp = []

for a in range(winWidth-1):
    for b in range(winHeight-1):
        if(not(computed[b][a])):
            tmp=[]
            iteration = 0
            fx = coord = complex(xMin+a*aScalar, yMin+b*bScalar)
            while(iteration < maxIteration and abs(fx) < 2):
                fx = fx**2 - coord
                iteration += 1
                if(not((fx.real-xMin)/aScalar%1) and not((fx.imag-yMin)/bScalar%1) and xMin <= fx.real < xMax and yMin <= fx.imag < yMax):
                    computed[int((fx.real-xMin)/aScalar)][int((fx.imag-yMin)/bScalar)] = True
                    tmp = [fx.real, fx.imag]
            if(abs(fx) < 2):
                win.plot(coord.real, coord.imag)
                win.plot(tmp[0], tmp[1])
                #for i in range(len(tmp)-1):
                    #win.plot(tmp[i][0], tmp[i][1])
                    #print(tmp[i][0], tmp[i][1])

##for i in range(len(tmp)-1):
##    win.plot(tmp[i][0], tmp[i][1])

print("done")
