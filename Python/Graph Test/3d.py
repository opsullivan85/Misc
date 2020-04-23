from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

'''VARS'''
threeD=True
res3D=50
maximized=True
colorBar=False
saveAs="test"
saveType="pdf"
pcolormesh=False
contour=True
fillContour=True
showAxes=True

logScale = False

dpi = 96
winw = 500
winh = 500
supersampling=0.5

depth = 20

zmax = 10
zmin = -zmax

xmin = -30
xmax = 30

ymin = xmin
ymax = xmax

if(threeD):
    xres = (xmax-xmin)/res3D
    yres = (ymax-ymin)/res3D
else:
    xres = (xmax-xmin)/winw/supersampling
    yres = (ymax-ymin)/winh/supersampling

'''X,Y INIT'''

xx = np.arange(xmin,xmax,xres)
yy = np.arange(ymin,ymax,yres)
x, y = np.meshgrid(xx, yy, sparse=True)

'''IMPUT FUNCTION HERE'''
z = 0.5-(np.cos(x)+np.cos(y*np.sin(np.pi/5)+x*np.cos(np.pi/5))+np.cos(y*np.sin(2*np.pi/5)+x*np.cos(2*np.pi/5))+np.cos(y*np.sin(3*np.pi/5)+x*np.cos(3*np.pi/5))+np.cos(y*np.sin(4*np.pi/5)+x*np.cos(4*np.pi/5)))
#z = np.abs(x)**np.sin(y)
#z = np.power(x,np.log(y))-np.power(y,np.log(x))

'''SCALE Z'''
if(logScale):
    z = np.ma.masked_where(z == 0, z) #Mask all 0s
    z = np.sign(z)*np.ma.log(np.abs(z)) #take log|z| and reapply sin
    z = np.array(z) #Remove mask        

'''PLOT INIT'''
if(threeD):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x,y,z,cmap=plt.get_cmap('plasma'),rcount=res3D,ccount=res3D)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(zmin,zmax)
else:
    fig = plt.figure(figsize=(winw/dpi,winh/dpi), dpi=dpi)
    
    if(maximized):
        plt.subplots_adjust(left=0,bottom=0,right=1,top=1)
        
    ax = fig.subplots()

    if(pcolormesh):
        cs = ax.pcolormesh(xx,yy,z,cmap=plt.get_cmap('plasma')) #Make pcolormesh
        
    elif(contour):
        if(fillContour):
            cs = ax.contourf(xx,yy,z,depth,cmap=plt.get_cmap('plasma')) #Make contour
        else:
            cs = ax.contour(xx,yy,z,depth,cmap=plt.get_cmap('plasma'))

    if(colorBar):
        cbar = fig.colorbar(cs) #Show color bar

    if(not(showAxes)):
        ax.set_axis_off()

if(saveAs):
    plt.savefig(saveAs,format=saveType)

plt.show()
print("done")
