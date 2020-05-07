import matplotlib.animation as animation
from matplotlib import pyplot as plt
import numpy as np


num_pts = 10

max_val = 5

def get_line_coords(p, a=0):
    tmp = np.array([np.cos(a), np.sin(a)])*max_val*3
    return(np.stack([tmp+p,-tmp+p]))

def skip_diag_strided(A):
    m = A.shape[0]
    strided = np.lib.stride_tricks.as_strided
    s0,s1 = A.strides
    return strided(A.ravel()[1:], shape=(m-1,m), strides=(s0+s1,s1)).reshape(m,-1)

def get_angles(pts):
    diff = pts[:,None,:]-pts[:,:]
    diff = diff/diff*diff
    angles = np.arctan2(diff[:,:,1],diff[:,:,0])
    print(diff)
    return angles+np.pi

def get_next(angles, a):
    return np.nanargmin((angles-a)%(2*np.pi))

pts = np.random.random([num_pts, 2])*2*max_val - max_val
pt = 1
angles = get_angles(pts)
print(angles)
angle = 0
s=1
next_angle = angles[pt][get_next(angles[pt],0)]
print(next_angle)
fig, ax = plt.subplots()

tmp = get_line_coords(pts[0])
line, = ax.plot(tmp[:,0],tmp[:,1])

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * 2)
    line.set_xdata([np.nan] * 2)
    s=1
    return line,

def animate(i):
    global angle, pts, pt, next_angle, s
    angle = (angle+np.pi/3600)%(2*np.pi)
    if not np.sign([next_angle-angle]) == s:
        pt = get_next(angles[pt], angle)
        print(pt)
        angle = angles[pt,get_next(angles[pt],0)]
        next_angle = angles[pt,get_next(angles[pt],next_angle)]
        s = np.sign([next_angle])
    tmp = get_line_coords(pts[pt], angle)

    line.set_xdata(tmp[:,0])
    line.set_ydata(tmp[:,1])
    return line,



ax.scatter(pts[:,0],pts[:,1])
ax.set_xlim(-max_val,max_val)
ax.set_ylim(-max_val,max_val)

ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True)

plt.show()
