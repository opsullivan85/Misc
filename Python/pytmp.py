from graphics import *
from random import randint
import numpy as np


bounds=((-100,100),(-100,100))

winW=1000
winH=1000

win = GraphWin("graphics", winW, winH, autoflush=False)
win.setCoords(bounds[0][0], bounds[1][0], bounds[0][1], bounds[1][1])

numPts = 10

def inBounds(p):
    return bounds[0][0]<p[0]<bounds[0][1], bounds[1][0]<p[1]<bounds[1][1]

class pt:
    def __init__(self, name, p=(0,0),v=(0,0),a=(0,0),size=5):
        self.name=name
        self.p=np.array(p,dtype='float64')
        self.v=np.array(v,dtype='float64')
        self.a=np.array(a,dtype='float64')
        self.size=size
        self.graphic=Circle(Point(p[0],p[1]),size)

    def __str__():
        return (f'pt {self.name}:'
                f'  pos={self.p[0]}, {self.p[1]}\n'
                f'  vel={self.v[0]}, {self.v[1]}\n'
                f'  acc={self.a[0]}, {self.a[1]}\n')

    def tStep(self,others,f,t=1):
        self.getA(others,f)
        self.updateV(t)
        tmp=inBounds(self.p)
        if(not all(tmp)):
            #self.a[None]=0
            self.v[0]=-(not t[0])*se.l
        self.updateP(t)

    def updateP(self,t):
        self.graphic.undraw()
        dp=self.v*t
       # print(dp)
        self.graphic.move(dp[0],dp[1])
        self.p+=dp
        self.graphic.draw(win)
        
    def updateV(self,t):
        self.v+=self.a*t
        
    def getA(self,others,f):
        for other in others:
            self.a+=self.reactionVector(other,f)

    def reactionVector(self, other, f):
        #divide distance components by distance to get
        #unit vector then take the function of that
        return f((self.p-other.p)/np.linalg.norm(self.p-other.p))

class ptcloud:
    def __init__(self,numPts):
        self.pts=[]
        for i in range(numPts):
            self.pts.append(pt(i, (randint(bounds[0][0],bounds[0][1]),randint(bounds[0][0],bounds[0][1]))))
                               
    def __str__(self):
        s=''
        for pt in self.pts:
            s+=str(pt)
        return(s)

    def tStep(self, t=1,f=lambda x:1/(abs(x)+0.1)):
        for i, pt in enumerate(self.pts):
            pt.tStep(self.pts[:i]+self.pts[i+1:],f,t)
        update()

pts=ptcloud(10)

#for frame in range(100):
while(1):
    pts.tStep(0.01)
    time.sleep(1/10)
