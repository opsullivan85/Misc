import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time
import sys

t0 = time.perf_counter_ns()

print("Starting program.")

'''VARS'''
threeD=True
res3D=100
maximized=False
colorBar=False
saveAs=False#'eqn_10000^2_2000^2.png'
pcolormesh=True
contour=False
fillContour=True
showAxes=True
aa=False
toolbar=True

solve=False

logScale = 0

symetric = #True

cmap='plasma' if not(solve) else 'binary'
#cmap='binary'

dpi = 166
winw = 1000
winh = 1000
supersampling=0.5

depth = 20

zmax = 30
zmin = -zmax
if(symetric):
    xmin = -25
    xmax = -xmin
    ymin = xmin
    ymax = -xmin
else:
    xmin = -100
    xmax = 100
    ymin = 1000
    ymax = 1100

print("Solving graph bounds...", end='')
if(threeD):
    xres = (xmax-xmin)/res3D
    yres = (ymax-ymin)/res3D
else:
    xres = (xmax-xmin)/winw/supersampling
    yres = (ymax-ymin)/winh/supersampling
print("Done")

'''X,Y INIT'''

print("Initializing graph variables...", end='')
xx = np.arange(xmin,xmax,xres)
yy = np.arange(ymin,ymax,yres)
x, y = np.meshgrid(xx, yy, sparse=True)
print("Done")

'''IBPUT FUNCTION HERE'''

print("Generating Plot...", end='')
z = 0.5-(np.cos(x)+np.cos(y*np.sin(np.pi/5)+x*np.cos(np.pi/5))+np.cos(y*np.sin(2*np.pi/5)+x*np.cos(2*np.pi/5))+np.cos(y*np.sin(3*np.pi/5)+x*np.cos(3*np.pi/5))+np.cos(y*np.sin(4*np.pi/5)+x*np.cos(4*np.pi/5)))
#z=x**2+y**2-1
#z = x**np.sin(y)
#z = x*y**2-(x-y)
#z = np.power(x,np.log(y))-np.power(y,np.log(x))
#z=x*y**2-x**3*y-6
#z = x**y-y**x
print("Done")

if(solve):
    print("Solving 2D Equation...", end='')
    z=1==np.sign(z)
    b = np.zeros((z.shape[0]-2,z.shape[1]-2))
    for i, val in np.ndenumerate(b):
        b[i]=np.any(z[i[0]+1,i[1]+1] != z[i[0]:3+i[0],i[1]:3+i[1]])
    z=np.pad(b,1,mode='constant')
    print("Done")

'''SCALE Z'''
if(logScale):
    print("Finding absLog() of equation...", end='')
    z = np.ma.masked_where(z == 0, z) #Mask all 0s
    for i in range(logScale):
        z = np.sign(z)*np.ma.log(np.abs(z)) #take log|z| and reapply sign
    z = np.array(z) #Remove mask
    print("Done")

'''PLOT INIT'''
if(not(toolbar)):
    plt.rcParams['toolbar'] = 'None'
    print("Removed Toolbar.")
if(threeD):
    print("Beginning 3D plot generation.")
    fig = plt.figure(figsize=(winw/dpi,winh/dpi), dpi=dpi)
    print("Figure created.")
    if(maximized):
        plt.subplots_adjust(left=0,bottom=0,right=1,top=1)
        print("Maximized Plot.")
    ax = fig.add_subplot(111, projection='3d')
    print("Subplot created.")
    print("Creating plot surface...", end='')
    cs=ax.plot_surface(x,y,z,cmap=plt.get_cmap(cmap),rcount=res3D,ccount=res3D,shade=True,antialiased=aa)
    print("Done")
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(zmin,zmax)
    print("Plot bounds set")

    if(not(showAxes)):
        ax.set_axis_off()
        print("Axes hidden.")
    if(colorBar):
        cbar = fig.colorbar(cs) #Show color bar
        print("Color bar added.")
    ax.set_xbound(-10,10)
    ax.set_ybound(-10,10)
    ax.set_zbound(-10,10)
    ax.view_init(45/2,33.33)
    
else:
    print("Beginning 2D plot generation.")
    fig = plt.figure(figsize=(winw/dpi,winh/dpi), dpi=dpi)
    print("Figure created.")
    if(maximized):
        plt.subplots_adjust(left=0,bottom=0,right=1,top=1)
        print("Maximized Plot.")
    ax = fig.subplots()
    print("Subplot created.")
    if(pcolormesh):
        print("Creating pcolormesh...", end='')
        cs = ax.pcolormesh(xx,yy,z,cmap=plt.get_cmap(cmap), antialiased=aa) #Make pcolormesh
        print("Done")
    elif(contour):
        if(fillContour):
            print("Creating contourf...", end='')
            cs = ax.contourf(xx,yy,z,depth,cmap=plt.get_cmap(cmap), antialiased=aa) #Make contour
            print("Done")
        else:
            print("Creating contour...", end='')
            cs = ax.contour(xx,yy,z,depth,cmap=plt.get_cmap(cmap), antialiased=aa)
            print("Done")

    if(not(showAxes)):
        ax.set_axis_off()
        print("Axes hidden.")
        
    if(colorBar):
        cbar = fig.colorbar(cs) #Show color bar
        print("Color bar added.")

if(saveAs):
    plt.savefig(saveAs)
    print(saveAs + " saved.")
else:
    plt.show(block=False)
    print("Plot shown.")

print("Program done.")

t1 = time.perf_counter_ns()
print(f"Time elapsed: {(t1-t0)/10**9:.3f}s")
