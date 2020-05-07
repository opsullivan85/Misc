import sympy as sp
import numpy as np
from numpy.random import *
import tensorflow as tf

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

print("Loading Data...", end="")
mnist = tf.keras.datasets.mnist
#print(np.shape(mnist.load_data()))
(x_train, y_train),(x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
print("Done!")

#print(x_test.shape, y_train[0])

x = sp.symbols('x')
np.set_printoptions(precision=5, floatmode='fixed')

class nn:
    def __init__(self):
        self.layers = []
        self.numLayers = 0
        
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
    
    def addLayer(self, size, fx=lambda x:x, layerType=None, weightMode='rand', biasMode='rand'):
        prevSize = self.layers[-1].size if len(self.layers) else 0
        self.layers.append(layer(size, prevSize, fx, layerType, weightMode, biasMode))
        self.numLayers += 1
        
    def calcNodes(self):
        for i, layer in enumerate(self.layers[1:]):
            layer.calcNodes(self.layers[i].nodes)
            
    def input(self, val):
        self.layers[0].setNodes(val)
        
    def output(self):
        return np.array2string(self.layers[-1].nodes)

    def backProp(self, goal, learningRate):
        for i in range(self.numLayers-1, 1, -1):
            goal = self.layers[i].backProp(self.layers[i-1].nodes, goal, learningRate)

    def score(self, goal):
        return(np.sum(np.abs(self.layers[-1].nodes-goal)))
    
class layer:
    def __init__(self, size, prevSize, fx=lambda x:x, layerType=None, weightMode='rand', biasMode='rand'):
        self.size = size
        self.nodes = np.empty((1, size))
        self.type = layerType
        self._initWeights(prevSize, weightMode)
        self._initBiases(biasMode)
        self.fx = sp.lambdify(x, fx, 'numpy')
        self.derivative = sp.lambdify(x, fx.diff(x), 'numpy')
        
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
    
    def _initWeights(self, num, mode='rand'):
        if(mode=='zeros'):
            self.weights = np.zeros((num,self.size))
        elif(mode=='rand'):
            self.weights = np.array(random_sample((num,self.size))*2-1)
        
    def _initBiases(self, mode='rand'):
        if(mode=='zeros'):
            self.biases = np.zeroes((self.size))
        elif(mode=='rand'):
            self.biases = np.array(random_sample((1,self.size))*2-1)
            
    def setNodes(self, val):
        if(type(val) == type(self.nodes) and val.shape == self.nodes.shape):
            self.nodes = val
        else:
            self.nodes = np.full_like(self.nodes, val)

    def calcNodes(self, prevNodes):
        self.nodes = self.fx(np.dot(prevNodes, self.weights) + self.biases)

    def backProp(self, prevNodes, goal, learningRate):
        functionDerivative = self.derivative(np.dot(prevNodes, self.weights) + self.biases)

        if not(type(functionDerivative) == 'numpy.ndarray'):
            functionDerivative = np.full(self.nodes.shape, functionDerivative)

        #WEIGHTS
        weightDerivative = np.dot(prevNodes.transpose(), functionDerivative)
        weightScalar = ((goal - self.nodes).transpose() / prevNodes).transpose() * learningRate[0]
        #print(weightChange)
        weightChange = np.multiply(weightDerivative, weightScalar)
        #print(weightChange)
        self.weights += weightChange

        #BIASES
        '''
        biasDerivative = functionDerivative
        print(functionDerivative)
        biasScalar = (goal - self.nodes)*learningRate
        biasChange = biasDerivative * learningRate
        self.biases += biasChange
        '''
        biasDerivative = (goal - self.nodes)
        biasScalar = learningRate[1]
        self.biases += biasDerivative * biasScalar
        #print(biasChange.shape)

        #NODES
        nodeDerivative = (np.dot(self.weights, functionDerivative.transpose())).transpose()
        nodeScalar = learningRate[2]
        nodeChange = nodeDerivative * nodeScalar
        return(nodeChange)
        
def main():
    #np.set_printoptions(suppress=True)
            #lambda x:atan(x)*2/pi
    f = sp.atan(x)*2/sp.pi
    #g = (sp.Abs(x)+x)/2
    n = nn()
    
    n.addLayer(28**2, f)
    n.addLayer(128, f)
    #n.addLayer(28, f)
    n.addLayer(10, f)
    #n.input(np.array([[.1,.1,.1,.1,.1]]))
    n.calcNodes()
    h = []
    #h[0] = n.score(np.matrix([[0.5,0.5,0.5,0.5]]))
    
    for i in range(1200):
        #print(x_train[i].reshape(-1).shape)
        n.input(np.ravel(x_train[i%60000]))
        n.calcNodes()
        solution = np.zeros((1, 10))
        #print(solution.shape, n.layers[2].nodes.shape)
        solution[0, y_train[i%60000]] = 1
        #print(solution)        
        n.backProp(solution, (2, 0, 1))
        #print(n.layers[3].nodes)
        #n.layers[3].backProp(n.layers[2].nodes, np.matrix([[0.5,0.5,0.5,0.5]]), (0.1, 0.1, 0))
        h.append(n.score(solution))
        #print(i)#, h[-1])
    print(n.print(1,1,1))
    #print(n.layers)
    fig = plt.figure()
    ax = fig.subplots()
    ax.plot(h)
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

















