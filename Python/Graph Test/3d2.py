from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
import matplotlib.pyplot as plt
from matplotlib import ticker
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

'''VARS'''
threeD=False
res3D=100
maximized=True
colorBar=False
saveAs=False#'eqn.png'
pcolormesh=True
contour=False
fillContour=True
showAxes=False
aa=True
toolbar=True

solve=True

logScale = False

cmap='plasma'
#cmap='binary'

dpi = 96
winw = 1000
winh = 1000
supersampling=1

depth = 20

zmax = 30
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
#z = x**np.sin(y)
#z = np.power(x,np.log(y))-np.power(y,np.log(x))
#z = x**y-y**x

if(solve):
    z=1==np.sign(z)
    b = np.zeros((z.shape[0]-2,z.shape[1]-2))
    with np.nditer(b,flags=['multi_index'], op_flags=['readwrite']) as it:
        for val in it:
            val[...]=np.any(z[it.multi_index] != z[it.multi_index[0]:3+it.multi_index[0],it.multi_index[1]:3+it.multi_index[1]])
    z=np.pad(b,1,mode='constant')

'''SCALE Z'''
if(logScale):
    z = np.ma.masked_where(z == 0, z) #Mask all 0s
    z = np.sign(z)*np.ma.log(np.abs(z)) #take log|z| and reapply sin
    z = np.array(z) #Remove mask        

'''PLOT INIT'''
if(not(toolbar)):
    plt.rcParams['toolbar'] = 'None'
if(threeD):
    fig = plt.figure(figsize=(winw/dpi,winh/dpi), dpi=dpi)
    if(maximized):
        plt.subplots_adjust(left=0,bottom=0,right=1,top=1)
    ax = fig.add_subplot(111, projection='3d')
    cs=ax.plot_surface(x,y,z,cmap=plt.get_cmap(cmap),rcount=res3D,ccount=res3D,shade=True,antialiased=aa)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_zlim(zmin,zmax)

    if(not(showAxes)):
        ax.set_axis_off()
    if(colorBar):
        cbar = fig.colorbar(cs) #Show color bar
    ax.set_xbound(-10,10)
    ax.set_ybound(-10,10)
    ax.set_zbound(-10,10)
    #ax.view_init(45/2,45/2)
    
else:
    fig = plt.figure(figsize=(winw/dpi,winh/dpi), dpi=dpi)
    
    if(maximized):
        plt.subplots_adjust(left=0,bottom=0,right=1,top=1)
        
    ax = fig.subplots()

    if(pcolormesh):
        cs = ax.pcolormesh(xx,yy,z,cmap=plt.get_cmap(cmap), antialiased=aa) #Make pcolormesh
        
    elif(contour):
        if(fillContour):
            cs = ax.contourf(xx,yy,z,depth,cmap=plt.get_cmap(cmap), antialiased=aa) #Make contour
        else:
            cs = ax.contour(xx,yy,z,depth,cmap=plt.get_cmap(cmap), antialiased=aa)

    if(colorBar):
        cbar = fig.colorbar(cs) #Show color bar

    if(not(showAxes)):
        ax.set_axis_off()

if(saveAs):
    plt.savefig(saveAs)
else:
    plt.show()

print("done")
