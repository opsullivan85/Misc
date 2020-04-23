import numpy as np

def mkppm(name, data, maxVal = 255):
    with open(name, 'w') as f:
        shape = data.shape
        f.write(f"P6\n{shape[0]} {shape[1]}  {maxVal}\n")
        for pos in np.nditer(data):
            print(pos)

def data2RGB(data):
    np.stack((z,z,z), axis=2)

def getCoords(coord=(0,0), zoom=1, res=(100,100)):
    xMin = -2. / zoom + coord[0]
    xMax = 2. / zoom + coord[0]
    yMin = -2. / zoom + coord[1]
    yMax = 2. / zoom + coord[1]
    x = np.linspace(xMin, xMax, res[0])
    y = np.flip(np.linspace(yMin, yMax, res[1]))
    xx, yy = np.meshgrid(x, y, sparse = True)
    return(xx + 1j*yy)

def function(coords, maxIter):
    

print(getCoords(res=(10,10)))

