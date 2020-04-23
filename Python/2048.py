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
        self.tiles = [[0]*self.size for i in range(self.size)]
        coordsList = []
        coord = []
        for row in range(self.size):
            for col in range(self.size):
                self.tiles[row][col] = tile(0)
                self.tiles[row][col].coords = [row, col]
                coordsList.append([row, col])
        for i in range(initTiles):
            coord = coordsList.pop(random.randint(0,len(coordsList)-1))
            self.tiles[coord[0]][coord[1]].val = initTileLst.pop(random.randint(0,len(initTileLst)-1))
        self.tiles[3][3].val = 8
            

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

    def shiftTile(self, tile, direction):
        while(-1 < tile.x + direction[0] < 5 and -1 < tile.y + direction[1] < 5 and not(self.tiles[tile.x + direction[0]][tile.y + direction[1]].val)):
            self.wapPos([tile.x, tile.y], [tile.x + direction[0], tile.y + direction[1]])

    def getInput(self):
        input = raw_input()
        if(input == "w"):
            return([0,1])
        elif(input == "a"):
            return([-1,0])
        elif(input == "s"):
            return([0,-1])
        else:
            return([1,0])

    def __str__(self, space = 2):
        string = ""
        for row in range(self.size):
            for col in range(self.size):
                string += f"{self.tiles[row][col].val:^{space}}"
            string += "\n"
        return(string)
    
    #def print(self):

board = board()
print(board)
board.shiftTile(board.tiles[3][3], [-1,0])
#board.swapPos([1,1], [3,3])
print(board)
