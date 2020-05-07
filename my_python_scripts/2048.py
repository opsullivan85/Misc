from graphics import *
import random

class tile:
    def __init__(self, val = 0):
        self.val = val
        self.coords = [0,0]
        self.x = 0
        self.y = 0

    def __str__(self):
        return(f"{self.val}")

class board:
    def __init__(self, size = 4, initTiles = 2, initTileLst = [2, 2, 2, 4]):
        self.size = size
        self.tiles = [[0]*self.size]*self.size
        coordsList = []
        coord = []
        for row in range(self.size):
            for col in range(self.size):
                self.tiles[row][col] = tile(0)
                self.tiles[row][col].coords = [row, col]
                coordsList.append([row, col])
        for i in range(initTiles):
            coord = coordsList.pop(random.randint(0,len(coordsList)-1))
            print(coord)
            self.tiles[i][i+1].val = 2
            #print(self.tiles.__str__())
            #print(initTileLst.pop(random.randint(0,len(initTileLst)-1)))
            #self.tiles[coord[0]][coord[1]].val = initTileLst.pop(random.randint(0,len(initTileLst)-1))
            

    #def shift(self, direction):
    #    for

    def swapPos(self, pos1, pos2):
        tile = self.tiles[pos2[0]][pos2[1]]
        self.tiles[pos2[0]][pos2[1]] = self.tiles[pos1[0]][pos1[1]]
        self.tiles[pos1[0]][pos1[1]] = tile
        

    def merge(self, pos1, pos2):
        if (self.tiles[pos1[0]][pos1[1]].val == self.tiles[pos2[0]][pos2[1]].val):
            self.tiles[pos1[0]][pos1[1]].val *= 2
            self.tiles[pos2[0]][pos1[1]].val = 0

    def shiftTile(self, tile, dir):
        while(-1 < tile.x + dir[0] < 5 and -1 < tile.y + dir[1] < 5 and not(self.tiles[tile.x + dir[0]][tile.y + dir[1]].val)):
            swapPos([tile.x, tile.y], [tile.x + dir[0], tile.y + dir[1]])

    def __str__(self):
        string = ""
        for row in range(self.size):
            for col in range(self.size):
                string += f"{self.tiles[row][col].val:^5}"
            string += "\n"
        return(string)
    
    #def print(self):

board = board()
print(board)
