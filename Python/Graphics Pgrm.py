from graphics import *
from math import *

#Graphics window height and width
height = 1000
width = 1000

#Graphics window init
win = GraphWin("Graphics Window", width, height)
#Set center coordinate system
win.setCoords(-width/2,-height/2,width/2,height/2)

#Draw axes
Line(Point(0,width/2),Point(0,-width/2)).draw(win)
Line(Point(-height/2,0),Point(height/2,0)).draw(win)

#<>--------------------------------------------------------------------------<>#

class pt2D:
    #2DPoint = pt2D([x,y])
    def __init__(self, cords):
        self.cords = cords
        self.winObj = Point(self.cords[0], self.cords[1])

##    #2DPoint = pt2D(x,y)
##    def __init__(self, x, y):
##        self.cords = [x,y]
##        self.winObj = Point(self.cords[0], self.cords[1])

    #Returns point's coordinates as list[x,y]
    def getCordsList(self):
        return(self.cords)

    #Prints point's coordinates to console
    def print(self, n=0, s=0, name = "Point2D"):
        print("\n"*n + " "*s + name + "=" + str(self.cords))

#<>--------------------------------------------------------------------------<>#

class pt3D:
    #3DPoint = pt3D([x,y,z])
    def __init__(self, cords):
        self.cords = cords
        self.winObj = Point(self.cords[0], self.cords[1])

##    #3DPoint = pt3D([x,y,z])
##    def __init__(self, x, y, z):
##        self.cords = [x,y,z]
##        self.winObj = Point(self.cords[0], self.cords[1])

    #Vector addition
    def __add__(self, cords):
        return pt3D([self.cords[0] + cords[0], self.cords[1] + cords[1], self.cords[2] + cords[2]])

    #Returns point's coordinates as list[x,y]
    def getCordsList(self):
        return(self.cords)

    #Prints point's coordinates to console
    def print(self, n=0, s=0, name="Point3D"):
        print("\n"*n + " "*s + name + " = " + str(self.cords))

    #Returns a point's displayed projection with ?focal length? "d"
    def to2D(self, d):
        return(pt2D([d*self.cords[1]/(self.cords[0]+d),d*self.cords[2]/(self.cords[0]+d)]))

#<>--------------------------------------------------------------------------<>#

class tri:
    #Triangle = tri([pt3D, pt3D, pt3D])
    def __init__(self, pts3D):
        self.pts3D = pts3D

##    #Triangle = tri(pt3D, pt3D, pt3D)
##    def __init__(self, a3D, b3D, c3D):
##        self.pts3D = [a3D, b3D, c3D]

    #Vector addition applied to whole triangle
    def __add__(self, cords):
        return tri([self.pts3D[0] + cords, self.pts3D[1] + cords, self.pts3D[2] + cords])
    
    #Prints all coordinates of triangle's points to console
    def print(self, n=0, s=0, name = "Triangle"):
        print("\n"*n + " "*s + name + ":")
        for i in range(len(self.pts3D)):
            self.pts3D[i].print(0, 1, "Point" + str(i))

    #Draws the triangle with orthographic projection
    def drawO(self, win):
        Polygon(self.pts3D[0].winObj, self.pts3D[1].winObj, self.pts3D[2].winObj).draw(win)

    #Updates perspective projections of triangles points
    def updateP(self, d):
        self.pts2D = self.pts3D
        for i in range(len(self.pts2D)):
            self.pts2D[i] = self.pts2D[i].to2D(d)

    #Draws the triangle on Graphical window "win"
    #with perspective projection and ?focal length? "d"
    def drawP(self, win, d):
        self.updateP(d)
        Polygon(self.pts2D[0].winObj, self.pts2D[1].winObj, self.pts2D[2].winObj).draw(win)

#<>--------------------------------------------------------------------------<>#

class chain3D:
    def __init__(self, pts3D):
        self.pts3D = pts3D
        self.connectionLines2DWinObj = []

    def print(self, n=0, s=0, name = "Chain3D"):
        print("\n"*n + " "*s + name + ":")
        for i in range(len(self.pts3D)):
            self.pts3D[i].print(0, 1, "Point " + str(i))

    def updatePts2DWinObj(self, d):
        self.pts2DWinObj = []
        for i in range(len(self.pts3D)):
            self.pts2DWinObj.append(self.pts3D[i].to2D(d).winObj)

    def updateLines2DWinObj(self, d):
        self.updatePts2DWinObj(d)
        self.lines2DWinObj = []
        for i in range(len(self.pts2DWinObj)-1):
            self.lines2DWinObj.append(Line(self.pts2DWinObj[i], self.pts2DWinObj[i+1]))

    def drawP(self, win, d):
        self.updateLines2DWinObj(d)       
        for line in self.lines2DWinObj:
            line.draw(win)

    def undrawP(self):       
        for line in self.lines2DWinObj:
            line.undraw()

    def drawPConnected(self, chain, win, d):
        self.connectionLines2DWinObj = []
        self.updateLines2DWinObj(d)
        chain.updateLines2DWinObj(d)
        if(len(self.pts2DWinObj) == len(chain.pts2DWinObj)):
            self.drawP(win,d)
            chain.drawP(win,d)
            for i in range(len(self.pts2DWinObj)):
                self.connectionLines2DWinObj.append(Line(self.pts2DWinObj[i], chain.pts2DWinObj[i]))
                self.connectionLines2DWinObj[i].draw(win)
        else:
            print("Chains must be the same length to connect!")

    def undrawPConnected(self, chain):
        self.undrawP()
        chain.undrawP()
        for i in range(len(self.connectionLines2DWinObj)):
            self.connectionLines2DWinObj[i].undraw()
#<>--------------------------------------------------------------------------<>#

class connection:
    def __init__(self, ptA3D, ptB3D):
        self.connections3D = [ptA3D, ptB3D]
#    def

#<>--------------------------------------------------------------------------<>#

#Scale
s = 300

#x, y, and z shift
x = 50
y = 100
z = 150

#Defining 8 corners of the cube
ptFUL = pt3D([0+x, 0+y, s+z])
ptFUR = pt3D([0+x, s+y, s+z])
ptFLR = pt3D([0+x, s+y, 0+z])
ptFLL = pt3D([0+x, 0+y, 0+z])
ptBUL = pt3D([s+x, 0+y, s+z])
ptBUR = pt3D([s+x, s+y, s+z])
ptBLR = pt3D([s+x, s+y, 0+z])
ptBLL = pt3D([s+x, 0+y, 0+z])


chainA = chain3D([ptFUL, ptFUR, ptFLR, ptFLL, ptFUL])
chainB = chain3D([ptBUL, ptBUR, ptBLR, ptBLL, ptBUL])

for d in range(10,1000,10):
    chainA.drawPConnected(chainB, win, d)
    time.sleep(1)
    chainA.undrawPConnected(chainB)
