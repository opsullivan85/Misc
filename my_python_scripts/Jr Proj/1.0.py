#Imports
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import re
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#Prep
plt.rcParams['legend.fontsize'] = 10
fig = plt.figure()
ax = fig.gca(projection='3d')

π = np.pi
#Θ

class gcode:
    
    def __init__(this, fname = "gcode.GCODE", initfname = False):
        this.fname = fname
        if(initfname):
            this.appendFile(initfname)
        this.x = 0
        this.y = 0
        this.z = 0
        this.e = 0

    def getFLen(this):
        with open(this.fname) as f:
                for i, l in enumerate(f):
                    pass
        this.flen = i + 1

    def appendFile(this, file2add):
        with open(file2add) as f2a:
            with open(this.fname, "a") as f:
                f.write(f2a.read())

    def clr(this):
        open(this.fname, "w")

    def Polar2GCode(rx, layerH, objH, res, **kwargs):
        layers = np.arange(0, objH + layerH, layerH)
        Θ = np.linspace(0, π/2, RES)
        R = 1
        x = R * np.sin(Θ)
        y = R * np.cos(Θ)
        z0 = 0
        
        with open(this.fname, "a") as f:
            for layer in layers:
                for angle in Θ:
                    print(angle)

tmp = gcode("a.GCODE", "gcode.txt")
tmp.getFLen()
print(tmp.flen)
tmp.clr()
