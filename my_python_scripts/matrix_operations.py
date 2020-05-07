from matplotlib import pyplot as plt
import numpy as np
import numpy.linalg as la

x = np.arange(-5,6)
y = np.arange(-1,2)

class camera():
    def __init__(self, coords, facing, focalLen, res = (500,500)):
        '''
        args:
         -coords: tuple(3 float)
             Coordinates of the Camera
         -facing: tuple(3 float)
             Unit vector to define the direction the camera is pointing
         -focalLen: float
             The Focal length of the camera
         -res: tuple(2 int)
             The resolution of the output of the camera

        methods:
         -show()
             displays the camera output
        '''
        
        self.facing = np.array(facing)/la.norm(np.array(facing))
        #assert la.norm(facing)==1, '\'facing\' must be a vector of magnitude 1'
        
        self.coords = np.array(coords)
        self.focalLen = focalLen
        self.focalPt = -self.facing*self.focalLen
        
        
    def show(self, ax):
        ax.arrow(self.coords[0],
                 self.coords[1],
                 self.facing[0],
                 self.facing[1],
                 width=0.05,
                 color='black')

def plot_pt_sets(pt_sets, colors, ax):
    for s, pt_set in enumerate(reversed(pt_sets)):
        color = colors[s]
        for p, pt in enumerate(pt_set):
            ax.scatter(pt[0],pt[1],color=color,label=str(p),s=((len(pt_sets)-s)*10)**2)



x, y = np.meshgrid(x,y)

tmp = np.ones_like(x)

orig = np.stack((x.ravel(),y.ravel(), tmp.ravel()), axis=1)

c = camera([4,3],[-3/5,0], 1)

modifier = np.array([[1, 0, 0],
                     [0, 1, 0],
                     [0, 0, 1]])[None,:,:]
                    #Remaps x=1
                    #Remaps y=1

modifierTensor = np.repeat(modifier, orig.shape[0], axis=0)

#print(orig[0])
#print(modifierTensor[0])

#new = np.tensordot(modifierTensor,orig,axes=([1],[1]))
new = np.einsum('ijk,ik->ij', modifierTensor, orig)

#print()
#print(orig[0])
#print(modifierTensor[0])
#print(new[0])
#print(np.dot(modifierTensor[0],orig[0]))

ax = plt.subplot()
#print(orig.shape)
#print(new.shape)


plot_pt_sets([orig, new],
             ['orange', 'blue'],
             ax)


c.show(ax)

#ax.scatter(pts[:,0],pts[:,1], label = np.arange(10))
#ax.scatter(new[:,0],new[:,1])
#ax.set_xlim(-6,6)
#ax.set_ylim(-6,6)
#ax.legend()
plt.show()
