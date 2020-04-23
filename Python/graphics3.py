from graphics import *
import math


height = 1000
width = 1000

win = GraphWin("Graphics Window", width, height)
win.setCoords(-width/2,-height/2,width/2,height/2)

Line(Point(0,width/2),Point(0,-width/2)).draw(win)
Line(Point(-height/2,0),Point(height/2,0)).draw(win)

##################################################################################

class Pt3D:
    total = 1
    
    def __init__(self, absCoords):
        self.absCoords = absCoords
        self.relCoords = absCoords
        self.linkedToPts = []
        self.name = "Pt#"+str(Pt3D.total)
        Pt3D.total += 1

    def addLink(self, pt3D):
        if self not in pt3D.linkedToPts:
            self.linkedToPts.append(pt3D)

    def addLinks(self, pts3D):
        for pt3D in pts3D:
            if self not in pt3D.linkedToPts:
                self.linkedToPts.append(pt3D)

    def setCoordSys(self, pt3D):
        self.relOrigin = pt3D
        self.updateRelCoords()

    def updateRelCoords(self):
        for i in range(len(self.relCoords)):
            self.relCoords[i] = self.relOrigin.absCoords[i] - self.absCoords[i]

    def updateAbsCoords(self):
        for i in range(len(self.absCoords)):
            self.absCoords[i] = self.relOrigin.absCoords[i] + self.relCoords[i]

    def moveToRel(self, relCoords):
        for i in range(len(self.relCoords)):
            self.relCoords[i] = relCoords[i]
        self.updateAbsCoords()

    def moveToAbs(self, absCoords):
        for i in range(len(self.absCoords)):
            self.absCoords[i] = absCoords[i]
        self.updateRelCoords()

    def to2D(self,d):
        self.twoD = [d*self.absCoords[0]/(self.absCoords[1]+d),d*self.absCoords[2]/(self.absCoords[1]+d)]

    def toWinObj(self, win, d):
        self.to2D(d)
        self.winObj = Point(self.twoD[0],self.twoD[1])

    def distToComp(self, pt3D):
        dx = self.absCoords[0] - pt3D.absCoords[0]
        dy = self.absCoords[1] - pt3D.absCoords[1]
        dz = self.absCoords[2] - pt3D.absCoords[2]
        return([dx,dy,dz])

    def distToAbs(self, pt3D):
        dx = self.absCoords[0] - pt3D.absCoords[0]
        dy = self.absCoords[1] - pt3D.absCoords[1]
        dz = self.absCoords[2] - pt3D.absCoords[2]
        return(math.sqrt((dx*dx)+(dy*dy)+(dz*dz)))

    def distToRelOrigin(self):
        self.distToRelOrigin = self.distToAbs(self.relOrigin)
        return self.distToRelOrigin

    def rotateAboutPt(self, pt3D, rotVector):
        self.setCoordSys(pt3D)
        #r = self.distToAbs(self.relOrigin)
        for n in range(len(self.relCoords)):
            r = math.sqrt(self.relCoords[(n+1)%3]**2+self.relCoords[(n-1)%3]**2)
            print(r)
            θ = math.atan(self.relCoords[(n+1)%3]/self.relCoords[(n-1)%3])
            self.relCoords[(n-1)%3] = float(r)/(math.cos(θ+rotVector[(n-1)%3]))
            self.relCoords[(n+1)%3] = float(r)/(math.sin(θ+rotVector[(n+1)%3]))
        self.updateAbsCoords()
        #θ
        
    def print(self):
        print(self.name + "'s Coords: " + str(self.absCoords))

    def printLinks(self):
        print(self.name + "'s Links:", end=" ")
        for link in self.linkedToPts:
            print(link.name + ",", end=" ")
        print()

    def draw(self, win, d):
        self.toWinObj(win, d)
        self.winObj.draw(win)

    def undraw(self):
        self.winObj.undraw()

##################################################################################

class Object:
    def __init__(self, pts3D):
        self.pts3D = pts3D
        self.winObjLines = []

    def setCenter(self):
        center = [0,0,0]
        count = 0
        for pt3D in self.pts3D:
            for i in range(3):
                center[i] += pt3D.absCoords[i]
                count += 1
        for i in range(len(center)):
            center[i] /= count
        self.center = Pt3D(center)
        for pt3D in self.pts3D:
            pt3D.setCoordSys(self.center)

    def addPts(self, pts3D):
        self.pts3D.append(pts3D)

    def populateWinObjLines(self, win, d):
        self.winObjLines = []
        for pt3D in self.pts3D:
            pt3D.toWinObj(win, d)
        for pt3D in self.pts3D:
            for linkedPt in pt3D.linkedToPts:
                self.winObjLines.append(Line(pt3D.winObj, linkedPt.winObj))

    def draw(self, win, d):
        self.populateWinObjLines(win, d)
        for line in self.winObjLines:
            line.draw(win)

    def undraw(self):
        for line in self.winObjLines:
            line.undraw()

    def translate(self, coords):
        for pt3D in self.pts3D:
            for i in pt3D.coords:
                pt3D.coords[i] += coords[i]

    def scale(self, scalar):
        for pt3D in self.pts3D:
            for i in pt3D.coords:
                pt3D.coords[i] *= scalar

    def rotateAboutPt(self, origin, rotVector):
        for pt3D in self.pts3D:
            pt3D.rotateAboutPt(origin,rotVector)
    
##################################################################################

s = 300

x = 100-s/2
y = 100-s/2
z = 100-s/2

        
FUL = Pt3D([0+x, 0+y, s+z])
FUR = Pt3D([0+x, s+y, s+z])
FLR = Pt3D([0+x, s+y, 0+z])
FLL = Pt3D([0+x, 0+y, 0+z])
BUL = Pt3D([s+x, 0+y, s+z])
BUR = Pt3D([s+x, s+y, s+z])
BLR = Pt3D([s+x, s+y, 0+z])
BLL = Pt3D([s+x, 0+y, 0+z])

FUL.addLinks([BUL,FUR,FLL])
FLR.addLinks([BLR,FUR,FLL])
BUR.addLinks([BLR,FUR,BUL])
BLL.addLinks([BLR,FLL,BUL])

square = Object([FUL,FUR,FLR,FLL,BUL,BUR,BLR,BLL])

square.setCenter()

pt = Pt3D([1,1,1])
pt.print()
pt.rotateAboutPt(Pt3D([0,0,0]),[0,0,1])
pt.print()


r = 4
res = 4
while(1):
    for i in range(0,360,res):
        #a = math.radians(i)
        square.draw(win,500)
        square.rotateAboutPt(square.center, [0,0,0.01])
        #square.translate([r*math.cos(a)-r*math.cos(a-res),r*math.sin(a)-r*math.sin(a-res),0])
        time.sleep(0.01)
        square.center.draw(win,500)
        square.undraw()

