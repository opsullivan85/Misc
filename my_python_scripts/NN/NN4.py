import sympy as sp
import numpy as np
from numpy.random import *
import tensorflow as tf

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

getData = 1
if(getData):
    print("Loading Data...", end="")
    mnist = tf.keras.datasets.mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    print("Done!")


x = sp.symbols('x')
np.set_printoptions(precision=5, floatmode='fixed')

class nn:
    def __init__(self, evalMode='max', dtype='float64'):
        self.layers = []
        self.numLayers = 0
        self.evalMode = evalMode
        self.dtype = dtype
        
    def __str__(self):
        string = ''
        for num, layer in enumerate(self.layers):
            string += f'\n\nLAYER {num}.\n'
            string += layer.__str__()
        return(string)
    
    def print(self, weights, nodes, biases):
            string = ''
            for num, layer in enumerate(self.layers):
                string += f'\n\n########## L {num}. ##########\n'
                if(weights):
                    string += '\nWEIGHTS:\n'
                    #print(layer.weights)
                    string += np.array2string(layer.weights) + '\n'
                if(nodes):
                    string += '\nNODES:\n'
                    string += np.array2string(layer.nodes) + '\n'
                if(biases):
                    string += '\nBIASES:\n'
                    string += np.array2string(layer.biases) + '\n'
            return(string)

    
    def addLayer(self, size, fx=lambda x:x, cost=None, layerType=None, weightMode='rand', biasMode='rand'):
        prevSize = self.layers[-1].size if len(self.layers) else 0
        self.layers.append(layer(size=size, prevSize=prevSize, fx=fx, cost=cost, layerType=layerType, weightMode=weightMode, biasMode=biasMode, dtype=self.dtype))
        self.numLayers += 1
        
    def calcNodes(self):
        for i, layer in enumerate(self.layers[1:]):
            layer.calcNodes(self.layers[i].nodes)
            
    def input(self, val):
        self.layers[0].setNodes(val)
        
    def output(self):
        return np.array2string(self.layers[-1].nodes)-1

    def backProp(self, goal, learningRate):
        for i in range(self.numLayers-1, 0, -1):
            goal = self.layers[i].backProp(self.layers[i-1].nodes, goal, learningRate)
        self.layers[0].backPropBiases(self.layers[1].nodes, goal, learningRate)

    def score(self, goal):
        return((np.sum(np.abs(self.layers[-1].nodes-goal)),self.eval(goal)))

    def eval(self, goal):
        if(self.evalMode == 'max'):
            return(np.array_equal(self.layers[-1].nodes==np.max(self.layers[-1].nodes),goal))
    
class layer:
    def __init__(self, size, prevSize, fx=lambda x:x, cost=None, layerType=None, weightMode='rand', biasMode='rand', dtype='float64'):
        self.size = size
        self.nodes = np.empty((1, size), dtype)-1
        self.type = layerType
        self._initWeights(prevSize, weightMode, dtype)
        self._initBiases(biasMode, dtype)
        if cost is None:
            self.cost = lambda n,g:g-n
        else:
            self.cost = cost
        #print(self.cost(2,4))
        if(type(fx) == str):
            if(fx=='relu'):
                self.fx = lambda x: np.fmax(0,x)
                self.der = lambda x: x > 0
            if(fx=='linear'):
                self.fx = lambda x: x
                self.der = lambda x: 1
        else:
            self.fx = sp.lambdify(x, fx, 'numpy')
            self.der = sp.lambdify(x, fx.diff(x), 'numpy')
        
    def __str__(self):
        string = ''
        string += 'Weights:\n'
        string += np.array2string(self.weights) + '\n'
        string += '\n\n'
        string += 'Nodes:\n'
        string += np.array2string(self.nodes) + '\n'
        string += '\n\n'
        string += 'Biases:\n'
        string += np.array2string(self.biases) + '\n'
        string += '\n'
        return(string)
    
    def _initWeights(self, num, mode='rand', dtype='float64'):
        if(mode=='zeros'):
            self.weights = np.zeros((num,self.size), dtype)
        elif(mode=='rand'):
            self.weights = np.array(random_sample((num,self.size))*2-1, dtype)
        
    def _initBiases(self, mode='rand', dtype='float32'):
        if(mode=='zeros'):
            self.biases = np.zeros((1, self.size), dtype)
        elif(mode=='rand'):
            self.biases = np.array(random_sample((1,self.size))*2-1, dtype)
            
    def setNodes(self, val, dtype='float32'):
        if(type(val) == type(self.nodes) and val.shape == self.nodes.shape):
            self.nodes = val
        else:
            self.nodes = np.full_like(self.nodes, val, dtype)

    def calcNodes(self, prevNodes):
        self.nodes = self.fx(np.dot(prevNodes, self.weights) + self.biases)

    def backProp(self, prevNodes, goal, learningRate):
        fDer = self.der(np.dot(prevNodes, self.weights) + self.biases)
        
        #print(fDer, type(fDer), not(type(fDer) == 'numpy.ndarray'))
        if not(type(fDer) == 'numpy.ndarray'):
            fDer = np.full(self.nodes.shape, fDer)

        cost = self.cost(self.nodes, goal)
        
        self.weights += np.matmul(prevNodes.T,learningRate[0]*np.multiply(cost,fDer))
        self.biases += learningRate[2]*np.multiply(cost,fDer)
        #recommended next node values
        return(prevNodes+np.dot(learningRate[1]*np.multiply(cost,fDer), self.weights.T))
    
    def backPropBiases(self, prevNodes, goal, learningRate):
        pass
        fDer = self.der(self.nodes + self.biases)
        
        #print(fDer, type(fDer), not(type(fDer) == 'numpy.ndarray'))
        if not(type(fDer) == 'numpy.ndarray'):
            fDer = np.full(self.nodes.shape, fDer)
            
        self.biases += learningRate[2]*np.multiply((goal-self.nodes),fDer)
        
def main():
    '''
    n = nn(dtype='float64')
    f = sp.atan(x)*2/sp.pi
    n.addLayer(10, 'linear', cost=lambda n,g:(g-n))

    n.addLayer(10, 'linear', cost=lambda n,g:(g-n))
    print(n)

    goal = np.full((10),0)
    goal[5] = 1

    costs = []
    
    for i in range(1000):
        costs.append(n.score(goal)[0])
        n.backProp(goal, (0.01, 0.01, 0.1))
        n.calcNodes()
        
    #quit()    
    '''
    f = sp.atan(x)*2/sp.pi
    relu = 1/(np.e**(1-x))
    #g = (sp.Abs(x)+x)/2
    n = nn(dtype='float64')

#   sum((goals-nodes)**2) /    
    n.addLayer(28**2, f, cost=lambda n,g:(g-n))
    #n.addLayer(28, f, cost=lambda n,g:(g-n))
    n.addLayer(10, f, cost=lambda n,g:(g-n))

    
    accuracy=[]
    its = 60000
    
    epochs=60
    batchSize=500
    testSize=500
    for epoch in range(epochs):
        for i in range(batchSize):
            #Input and update NN
            n.input(np.ravel(x_train[(epoch*batchSize+i)%60000]))
            n.calcNodes()
            
            #Get solution in correct format
            solution = np.zeros((1, 10))
            solution[0, y_train[(epoch*batchSize+i)%60000]] = 1

            #Store costs
            #costs.append(n.score(solution)[0])

            #Back propogate
            n.backProp(solution, (1/600, 1/600, 1/600))
        costs = []
        for j in range(testSize):
            
            n.input(np.ravel(x_test[j]))
            n.calcNodes()

            solution = np.zeros((1, 10))
            solution[0, y_test[j]] = 1

            costs.append(n.score(solution)[1])
        print(f"epoch {epoch}")
        accuracy.append(sum(costs)/len(costs))
        print(sum(costs)/len(costs))
    
    print(n.print(1,1,1))
    #print(solution)
    
    fig = plt.figure()
    ax = fig.subplots()
    ax.plot(accuracy)
    #print(costs)
    fig.show()
    

    #n.layers[3].calcNodes(n.layers[2].nodes)
    #print(n.layers[3].nodes)

main()
'''
p = +0.1 -0.2
w = ++
n = --

p = -0.4 -0.1
w = ++
n = --

p = +0.6 + 0.5
w = ++ ~1
n = 0.5

p = -0.2 -0.4
w = + + + - x2
n = - - - +
'''

















