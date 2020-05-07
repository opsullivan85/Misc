'''
l = float(input('Beam Len: '))

f = float(input('Force: '))

a, b = 0, 0

while 1:
    
    d = float(input('Distance: '))
    
    a += (l - d) / l * f

    b += d / l * f
    try:
        f = float(input('Force: '))
    except:
        break

print((-a, -b))
'''
class beam:
    def __init__(self, forces, length):
        self.forces = forces,
        self.length = length
        print(self.forces)

    def solve_reactions(self):
        for force, pos in self.forces:
            a += (self.length - pos) / self.length * f
            b += pos / self.length * f
        self.forces += ((a, 0), (b, self.length))

    @classmethod
    def from_strs(cls, f, d, l):
        f = f.split(' ')
        f = [float(i) for i in f]
        d = d.split(' ')
        d = [float(i) for i in d]
        f = [[f[i], d[i]] for i in range(len(f))]
        return(cls(f, l))

print()

b = beam.from_strs(input('Forces: '), input('Distances: '), input('Length: '))

b.solve_reactions()
print(b.forces)
