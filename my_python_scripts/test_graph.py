from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from numpy import linalg as la
from PIL import Image, ImageDraw

class shape():
    __slots__  = ['verts', 'faces', 'tris', 'centers', 'norms']

    def __init__(self, verts, faces = None):
        dim = verts.ndim
        
        if dim == 3:
            assert faces == None, 'Faces should not be used if verticies are grouped.'
            self.faces = np.arange(verts.shape[0]*3).reshape((-1,3))
            self.verts = verts.reshape(-1,3)
        elif dim == 2:
            assert faces != None, 'Faces must be used if verticies are not grouped.'
            self.verts = verts
        else:
            raise Exception('Verticies must be an array of shape (n,3) or (n,3,3).')

        self.numVerts = verts.shape[0]
        self._updateTris()
        self._calcNorms()
        self._calcCenters()
        print(self.verts,'\n')
        print(self.faces,'\n')
        print(self.tris,'\n')
        print(self.norms,'\n')

        
    def _updateTris(self):
        self.tris = self.verts[self.faces]

    def _calcNorms(self):
        self.norms = np.cross(self.tris[:,2]-self.tris[:,0],self.tris[:,2]-self.tris[:,1])
        self.norms = self.norms/la.norm(self.norms, axis=1)[:,None]
        
    def _calcCenters(self):
        self.centers = np.sum(self.tris, axis=1)/3

    def matrixtransform(self, matrix):
        #repeat the matrix to get the right shape
        transformTensor = np.repeat(modifier[None,:,:], self.numVerts, axis=0)
        #element wise dot product between the transform tensor and self.verts
        self.verts = np.einsum('ijk,ik->ij', modifierTensor, self.verts)
        
        

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
        self.coords = np.array(coords)
        self.focalLen = focalLen
        self.focalPt = -self.facing*self.focalLen
        
        self.image = Image.new('RGB', res, (255,255,255))
        self.draw = ImageDraw.Draw(self.image)
        
    def show(self):
        self.image.show()

    def translate(self, vector):
        self.coords = self.coords+vector

    def lookAt(self, coords):
        self.facing = (coords-self.coords)/la.norm(coords-self.coords)

    def moveTo(self, coords):
        self.coords = np.array(coords)
        

shape(np.array([[[0,0,0],[1,0,0],[0,2,0]],
                [[1,1,1],[2,2,2],[3,3,3]]]))

c = camera(coords=(0,0,0), facing=(1,0,0), focalLen=1)
c.show()

