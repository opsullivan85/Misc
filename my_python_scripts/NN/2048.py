import random

class game:
    def __init__(self, size=4):
        self.size=size
        self.board=[[0]*size for _ in range(size)]
        self.score=0
        self.getAval()
        #self.open = [[True,(r,c)] for r in range(size) for c in range(size)]
        #print(self.open)
        #self.getOpen()
        
        #print(self.board)

    def __str__(self, hSpace=5, vSpace=0):
        line = "+"+"-"*(4*(hSpace+1)-1)+"+\n"
        string = line
        for r in self.board:
            for _ in range(vSpace):
                string += ("|"+" "*hSpace)*4+"|\n"
            for c in r:
                if(c):
                    string += f"|{c:^{hSpace}}"
                else:
                    string += f"|{' ':^{hSpace}}"
            string += "|\n"
            for _ in range(vSpace):
                string += ("|"+" "*hSpace)*4+"|\n"
            string += line
        return(string)

    def __getitem__(self, i):
        return(self.board[i[0]][i[1]])

    def newTile(self, choices=[2,2,2,4]):
        #Populate an open position and remove
        #that position from the open list
        pos = random.randint(0, self.aval-1)
        for r in range(self.size):
            for c in range(self.size):
                if(not self[r,c]):
                    if(not pos):
                        self.board[r][c] = random.choice(choices)
                        self.aval -= 1
                        return
                    pos -= 1

    def getScore(self):
        self.score=sum(sum(self.board[r]) for r in range(self.size))
        return(self.score)
    
    def shift(self, direction):
        changed = False
        if(direction[0]): #up
            for r in range(1, self.size):
                for c in range(self.size):
                    if(not self[r-1,c]):
                        if(not changed):
                            changed = True
                        self.board[r-1][c] = self[r,c]
                        self.board[r][c]=0
        elif(direction[1]): #left
            for c in range(1, self.size):
                for r in range(self.size):
                    if(not self[r,c-1]):
                        if(not changed):
                            changed = True
                        self.board[r][c-1] = self[r,c]
                        self.board[r][c]=0
        elif(direction[2]): #down
            for r in range(self.size-2,-1,-1):
                for c in range(self.size):
                    if(not self[r+1,c]):
                        if(not changed):
                            changed = True
                        self.board[r+1][c] = self[r,c]
                        self.board[r][c]=0
        else: #right
            for c in range(self.size-2, -1, -1):
                for r in range(self.size):
                    if(not self[r,c+1]):
                        if(not changed):
                            changed = True
                        self.board[r][c+1] = self[r,c]
                        self.board[r][c]=0

        return changed

    def merge(self, direction):
        changed = False
        if(direction[0]): #up
            for r in range(1, self.size):
                for c in range(self.size):
                    if(self[r-1,c] == self[r,c]):
                        if(not changed):
                            changed = True
                        self.board[r-1][c] += self[r,c]
                        self.board[r][c]=0
                        self.aval += 1
        elif(direction[1]): #left
            for c in range(1, self.size):
                for r in range(self.size):
                    if(self[r,c-1] == self[r,c]):
                        if(not changed):
                            changed = True
                        self.board[r][c-1] += self[r,c]
                        self.board[r][c]=0
                        self.aval += 1
        elif(direction[2]): #down
            for r in range(self.size-2,-1,-1):
                for c in range(self.size):
                    if(self[r+1,c] == self[r,c]):
                        if(not changed):
                            changed = True
                        self.board[r+1][c] += self[r,c]
                        self.board[r][c]=0
                        self.aval += 1
        else: #right
            for c in range(self.size-2, -1, -1):
                for r in range(self.size):
                    if(self[r,c+1] == self[r,c]):
                        if(not changed):
                            changed = True
                        self.board[r][c+1] += self[r,c]
                        self.board[r][c]=0
                        self.aval += 1

        return changed

    def move(self, direction):
        for i in range(self.size-1):
            if(not self.shift(direction)):
                break
        self.merge(direction)
        self.shift(direction)
        self.newTile()
        if(not self.aval):
            return(self.isDone())

    def isDone(self):
        #up
        for r in range(1, self.size):
            for c in range(self.size):
                if(self[r-1,c] == self[r,c]):
                    return True
        #left
        for c in range(1, self.size):
            for r in range(self.size):
                if(self[r,c-1] == self[r,c]):
                    return True
        #down
        for r in range(self.size-2,-1,-1):
            for c in range(self.size):
                if(self[r+1,c] == self[r,c]):
                    return True
        #right
        for c in range(self.size-2, -1, -1):
            for r in range(self.size):
                if(self[r,c+1] == self[r,c]):
                    return True
        return False

    def getAval(self):
        self.aval = sum([self[r,c]==0 for r in range(self.size) for c in range(self.size)])
                
                

a = game()
#print(a.open)
'''
a.board = [[1,1,1,0],
           [0,0,1,1],
           [0,1,0,1],
           [0,0,0,1]]'''
for i in range(10):
    a.newTile()
print(a)
a.move((0,1,0,0))
print(a)
