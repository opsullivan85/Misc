from graphics import *
import cmath
import math

s = 1
z = 1
h = 0
v = 0

maxIteration = 100
winWidth = 100*s
winHeight = 100*s
xMin = -0.5 / z + h
xMax = 2. / z + h
yMin = -1.25 / z + v
yMax = 1.25 / z + v

aScalar = (xMax-xMin)/winWidth
bScalar = (yMax-yMin)/winHeight

win = GraphWin("graphics", winWidth, winHeight, autoflush=False)
win.setCoords(xMin, yMin, xMax, yMax)

progress = 0

for a in range(winWidth-1):
    for b in range(winHeight-1):
        iteration = 0
        fx = coord = complex(xMin+a*aScalar, yMin+b*bScalar)
        while(iteration < maxIteration and abs(fx) < 2):
                fx = fx**2- coord
                iteration += 1
        if(abs(fx) > 2):
            c = int(math.log(float(iteration)+1) / math.log(maxIteration+1) * 255)
            win.plot(coord.real, coord.imag, color_rgb(c,0,c))
    if(100*a//winWidth > progress + 4):
        progress = 100*a//winWidth
        print(str(progress) + "% Completed")
        #if(not(progress%10)):
        #    update()
print("100% Completed")
print("Pushing to graphics...")
update()
print("Done")

