import numpy as np
import random

class grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * self.size for _ in range(self.size)]
        self.moves = [[0] * self.size for _ in range(self.size)]
        ordinal_nums = [[0] * self.size for _ in range(self.size)]
        #print(self.grid)

    def __str__(self):
        s = ''
        for r in range(self.size):
            for c in range(self.size):
                s += f'{self.grid[r][c]:<2} '
            s += '\n'
        return(s)

    def __getitem__(self, pos):
        return(self.grid[pos[0]][pos[1]])

    def __setitem__(self, pos, val):
        self.grid[pos[0]][pos[1]] = val
    
    def possible_moves(self, pos):
        moves = []
        if pos[0] < self.size - 1: #not bottom row
            moves.append([1, 0])
        if 0 < pos[0]: #not top row
            moves.append([-1, 0])
        if pos[1] < self.size - 1: # not right col
            moves.append([0, 1])
        if 0 < pos[1]: #not left col
            moves.append([0, -1])
        return moves
            
    def all_possible_moves(self):
        self.possible_moves = [[self.possible_moves((row, col)) for row in range(self.size)] for col in range(self.size)]

    def step(self):
        for r in range(self.size):
            for c in range(self.size):
                next_to = []
                for i in range(len(self.possible_moves[r][c])):
                    next_to.append(self[self.possible_moves[r][c][i]])
                    #print(self.possible_moves[r][c][self.grid.index(min(self.grid))])
                self.moves[r][c] = self.possible_moves[r][c][next_to.index(min(next_to))]
                print(r, c)
        self.move()

    def move(self):
        for r in range(self.size):
            for c in range(self.size):
                if self[r,c] <= 1:
                    continue
                self[r,c] -= 1
                print(r, c, self.moves[r][c], self.possible_moves[r][c])
                self[self.moves[r][c][0] + r, self.moves[r][c][1] + c] += 1
                

    def set(self, pos, val):
        self.grid[pos[0]][pos[1]] = val

    def grid_init_rand(self, num=10, r = [0,100]):
        total_postions = self.size * self.size-1
        data = [[random.randint(0, total_postions), random.randint(r[0], r[1])] for _ in range(num)]
        #print(data)
        for i in range(num):
            self.grid[data[i][0] // self.size][data[i][0] % self.size] = data[i][1]
            
        

g = grid(5)

g.grid_init_rand()
print(g)
g.all_possible_moves()
g.step()
print(g.moves)

