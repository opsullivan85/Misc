#Imports
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.animation as animation

#Prep
plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
#ax = fig.gca(projection='3d')
ax = fig.add_subplot(111, projection='3d')

#Constants
FREQ = 10
RES = 100
ANI_RES = 10
AMP = 0.05
LAYER_HEIGHT = 0.1
π = np.pi
R = 1
TUBE_HEIGHT = 2
NUM_LAYERS = int(TUBE_HEIGHT/LAYER_HEIGHT)+1

#Vars
Θ = np.linspace(3*π/2, π/2, RES)
x = R * np.sin(Θ)
y = R * np.cos(Θ)
z = [AMP*np.sin(FREQ*Θ)*np.sin(π*zi/TUBE_HEIGHT)+zi for zi in np.arange(0, TUBE_HEIGHT + LAYER_HEIGHT, LAYER_HEIGHT)]
line3DLayers = [''] * NUM_LAYERS
for i in range(NUM_LAYERS):
    line3DLayers[i] = ax.plot(x,y,z[i],color="black")

#Beautify plot
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)
ax.set_zlim(0, TUBE_HEIGHT)
#ax.zaxis.set_major_locator(LinearLocator(10))
#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_axis_off()

def update(amp):
    z = [amp*np.sin(FREQ*Θ)*np.sin(π*zi/TUBE_HEIGHT)+zi for zi in np.arange(0, TUBE_HEIGHT + LAYER_HEIGHT, LAYER_HEIGHT)]
    for i in range(NUM_LAYERS):
        #print(line3DLayers[i][0][0])
        line3DLayers[i] = ax.plot(x,y,z[i],color="black")
    #return line3DLayers[:][0]

ani = animation.FuncAnimation(fig, update, frames=np.linspace(0,AMP,ANI_RES), interval=25, blit=False)

#Show plot
plt.show()
