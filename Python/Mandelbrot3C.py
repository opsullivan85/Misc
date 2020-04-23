from graphics import *
import cmath
import math
import numpy as np
import matplotlib.pyplot as plt
import quaternion

s = 2
z = 1
h = -1.5
v = 0

maxIteration = 100
winWidth = 100*s
winHeight = 100*s
xMin = -0.5 / z + h
xMax = 2. / z + h
yMin = -1.25 / z + v
yMax = 1.25 / z + v

res=101
colors=np.ones((winWidth,winHeight),dtype='float32')

for j in np.linspace(0,1,res)*np.quaternion(0,0,1,0):
    print(j)
    x=np.linspace(xMin,xMax,winWidth,dtype='quaternion')[:,None]+j
    y=np.linspace(yMin,yMax,winHeight,dtype='quaternion')[None,:]*1j+j
    coords = x+y
    grid = np.zeros_like(coords)
    mask=np.ones_like(grid,dtype='bool')

    for n in range(maxIteration):
        grid[mask]=grid[mask]*grid[mask]+coords[mask]
        mask[mask]=np.absolute(grid[mask])<2

    colors[mask]-=1/res#((maxIteration-n)/maxIteration)

colors = colors**5
colors=np.repeat(colors[:,:,None],3,axis=2)

plt.imshow(colors)
plt.show()

