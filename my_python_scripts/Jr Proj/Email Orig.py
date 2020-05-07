#Imports
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#Prep
plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')

#Constants
FREQ = 10
RES = 100
AMP = 0.5
LAYER_HEIGHT = 0.1
π = np.pi
R = 3
H = 6

#Vars
layers = np.arange(0, H + LAYER_HEIGHT, LAYER_HEIGHT)
Θ = np.linspace(3*π/2, π/2, RES)
#Θ = np.linspace(0, π*2, RES)
z = [AMP * np.sin(FREQ*Θ) * np.sin(π*layer/H) + layer for layer in layers]
x = R * np.sin(Θ)
y = R * np.cos(Θ)

#Plot each layer
for layerNum in range(len(layers)):
    ax.plot(x, y, z[layerNum], color='black', alpha=0.5)

#Beautify plot
ax.set_xlim(-R, R)
ax.set_ylim(-R, R)
ax.set_zlim(0, H)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.set_axis_off()

#Show plot
plt.show()
