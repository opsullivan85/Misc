from graphics import *
import cmath
import math

class quaternion:
    def __init__(self,r,i,j,k):
        self.r=r
        self.i=i
        self.j=j
        self.k=k
    def __mul__(self,other):
        return quaternion(self.r*other.r-self.i*other.i-self.j*other.j-self.k*other.k,
                          self.i*other.r+self.r*other.i+self.k*other.j-self.j*other.k,
                          self.j*other.r-self.k*other.i+self.r*other.j+self.i*other.k,
                          self.k*other.r+self.j*other.i-self.i*other.j+self.r*other.k)
    def __pow__(self,other):
        product=self
        for _ in range(other-1):
            product*=self
        return product
    def __sub__(self,other):
        return quaternion(self.r-other.r,
                          self.i-other.i,
                          self.j-other.j,
                          self.k-other.k)
    def __abs__(self):
        return (self.r**2+self.i**2+self.j**2+self.k**2)**0.5

s = 5
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

j,k=0.1,0.1

for a in range(winWidth-1):
    for b in range(winHeight-1):
        iteration = 0
        fx = coord = quaternion(xMin+a*aScalar, yMin+b*bScalar,j,k)
        while(iteration < maxIteration and abs(fx) < 2):
                fx = fx**2 - coord
                iteration += 1
        if(abs(fx) > 2):
            c = int(math.log(float(iteration)+1) / math.log(maxIteration+1) * 255)
            win.plot(coord.r, coord.i, color_rgb(c,0,c))
    if(100*a//winWidth > progress + 4):
        progress = 100*a//winWidth
        print(str(progress) + "% Completed")
        #if(not(progress%10)):
        #    update()
print("100% Completed")
print("Pushing to graphics...")
update()
print("Done")

