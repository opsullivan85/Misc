from graphics import *
import random

class board:
    def __init__(self, size = 4,  initTiles = 2, initTilesLst = [2,2,2,4]):
        self.size = 4
        self.tiles = [[0] * size for i in range(size)]
        self.coords = [[r,c] for r in range(size) for c in range(size)]
        randCoords = random.sample(self.coords, initTiles)
        for coord in randCoords:
            self.tiles[coord[0]][coord[1]] = random.choice(initTilesLst)
            
    def __str__(self):
        string = ""
        for row in range(self.size):
            for col in range(self.size):
                string += f"{self.tiles[row][col]:^3}"
            string += "\n"
        return(string)

    def shiftTiles(self, sftDir):
        if(sftDir == [-1,0]):           #Left
            for col in range(1, self.size):
                for row in range(self.size):
                    if(not(self.tiles[row][col-1]) and self.tiles[row][col]):
                        self.tiles[row][col-1] = self.tiles[row][col]
                        self.tiles[row][col] = 0
                
        elif(sftDir == [1,0]):       #Right
            for col in range(self.size-2, -1, -1):
                for row in range(self.size):
                    if(not(self.tiles[row][col+1]) and self.tiles[row][col]):
                        self.tiles[row][col+1] = self.tiles[row][col]
                        self.tiles[row][col] = 0

        elif(sftDir == [0,1]):        #Up
            for row in range(1, self.size):
                for col in range(self.size):
                    if(not(self.tiles[row-1][col]) and self.tiles[row][col]):
                        self.tiles[row-1][col] = self.tiles[row][col]
                        self.tiles[row][col] = 0
                
        elif(sftDir == [0,-1]):       #Down
            for row in range(self.size-2, -1, -1):
                for col in range(self.size):
                    if(not(self.tiles[row+1][col])):
                        self.tiles[row+1][col] = self.tiles[row][col]
                        self.tiles[row][col] = 0

    def mergeTiles(self, mrgDir):
        if(mrgDir == [-1,0]):           #Left
            for col in range(1, self.size):
                for row in range(self.size):
                    if(self.tiles[row][col-1] and self.tiles[row][col] and self.tiles[row][col] == self.tiles[row][col-1]):
                        self.tiles[row][col-1] *= 2
                        self.tiles[row][col] = 0
                
        elif(mrgDir == [1,0]):       #Right
            for col in range(self.size-2, -1, -1):
                for row in range(self.size):
                    if(self.tiles[row][col+1] and self.tiles[row][col] and self.tiles[row][col] == self.tiles[row][col-1]):
                        self.tiles[row][col+1] *= 2
                        self.tiles[row][col] = 0

        elif(mrgDir == [0,1]):        #Up
            for row in range(1, self.size):
                for col in range(self.size):
                    if(self.tiles[row-1][col] and self.tiles[row][col] and self.tiles[row][col] == self.tiles[row][col-1]):
                        self.tiles[row-1][col] *= 2
                        self.tiles[row][col] = 0
                
        elif(mrgDir == [0,-1]):       #Down
            for row in range(self.size-2, -1, -1):
                for col in range(self.size):
                    if(self.tiles[row+1][col] and self.tiles[row][col] and self.tiles[row][col] == self.tiles[row][col-1]):
                        self.tiles[row+1][col] *= 2
                        self.tiles[row][col] = 0

    def move(self, moveDir):
        self.shiftTiles(moveDir)
        self.shiftTiles(moveDir)
        self.shiftTiles(moveDir)
        self.mergeTiles(moveDir)
        self.shiftTiles(moveDir)

brd = board()
#brd.tiles[0] = [2,2,2,2]
print(brd)
brd.move([-1,0])
print(brd)

import getKey

key = getKey()
