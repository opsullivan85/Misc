from sympy import *
from sympy.matrices import matrix_multiply_elementwise
import numpy as np
from numpy.random import *
#from mpmath import *

x = symbols('x')
precision = 5

class nn:
    def __init__(self):
        self.layers = []
        
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
                    string += pretty(N(layer.weights, precision), use_unicode=True) + '\n'
                if(nodes):
                    string += '\nNODES:\n'
                    string += pretty(N(layer.nodes, precision), use_unicode=True) + '\n'
                if(biases):
                    string += '\nBIASES:\n'
                    string += pretty(N(layer.biases, precision), use_unicode=True) + '\n'
            return(string)
    
    def addLayer(self, size, fx=lambda x:x, layerType=None, weightMode='rand', biasMode='rand'):
        prevSize = self.layers[-1].size if len(self.layers) else 0
        self.layers.append(layer(size, prevSize, fx, layerType, weightMode, biasMode))
        
    def calcNodes(self):
        for i, layer in enumerate(self.layers[1:]):
            layer.calcNodes(self.layers[i].nodes)
            
    def input(self, val):
        self.layers[0].setNodes(val)
        
    def output(self):
        return pretty(N(self.layers[-1].nodes, precision))
    
class layer:
    def __init__(self, size, prevSize, fx=lambda x:x, layerType=None, weightMode='rand', biasMode='rand'):
        self.size = size
        self.nodes = Matrix([[0]*size])
        self.type = layerType
        self._initWeights(prevSize, weightMode)
        self._initBiases(biasMode)
        self.fx = fx
        self.derivative = diff(self.fx(x), x)
        #print(self.fx(2.1232))
        
    def __str__(self):
        string = ''
        string += 'Nodes:\n'
        string += pretty(N(self.nodes, precision), use_unicode=True)
        string += '\n\n'
        string += 'Weights:\n'
        string += pretty(N(self.weights, precision), use_unicode=True)
        string += '\n\n'
        string += 'Biases:\n'
        string += pretty(N(self.biases, precision), use_unicode=True)
        string += '\n'
        return(string)
    
    def _initWeights(self, num, mode='rand'):
        if(mode=='zeros'):
            self.weights = Matrix([[0]*self.size]*num)
        elif(mode=='rand'):
            self.weights = Matrix(random_sample((num,self.size))*2-1)
        
    def _initBiases(self, mode='rand'):
        if(mode=='zeros'):
            self.biases = Matrix([[0]*self.size])
        elif(mode=='rand'):
            self.biases = Matrix(random_sample((1,self.size))*2-1)
            
    def setNodes(self, val):
        if(type(val) == type(self.nodes) and val.shape == self.nodes.shape):
            self.nodes = val
        else:
            self.nodes = ones(self.nodes.shape[0], self.nodes.shape[1])*val

    def calcNodes(self, prevNodes):
        self.nodes = (prevNodes * self.weights + self.biases).applyfunc(self.fx)

    def backProp(self, prevNodes, goal, learningRate):
        functionDerivative = (prevNodes * self.weights + self.biases).applyfunc(lambdify(x, self.derivative))
        #goal -= self.nodes
        #WEIGHTS
        weightChange = prevNodes.T * functionDerivative
        weightScalar = ((goal - self.nodes).T * prevNodes).T
        #print(pretty(N(weightChange, precision), use_unicode=True))
        #print(pretty(N(weightScalar, precision), use_unicode=True))
        weightChange = matrix_multiply_elementwise(weightChange,weightScalar)
        #print(pretty(N(weightChange, precision), use_unicode=True))
        self.weights += weightChange
        #print(weightChange.shape, self.weights.shape)
        #BIASES
        biasChange = functionDerivative
        #print(biasChange.shape, self.biases.shape)
        #NODES
        nodeChange = (self.weights * functionDerivative.T).T
        #print(nodeChange.shape, prevNodes.shape)
        
        
        #lambda x:atan(x)*2/pi
n = nn()
n.addLayer(5, lambda x:x)
n.addLayer(4, lambda x:x)
n.addLayer(2, lambda x:x)
n.addLayer(4, lambda x:x)
n.input(Matrix([[.1,.1,.1,.1,.1]]))
n.calcNodes()
#print(n.output())
print(pretty(N(n.layers[2].nodes, precision), use_unicode=True))
print(pretty(N(n.layers[3].nodes, precision), use_unicode=True))
print(pretty(N(n.layers[3].weights, precision), use_unicode=True))

print("####################")
n.layers[3].backProp(n.layers[2].nodes, Matrix([[1,1,1,1]]), 0.5)
n.calcNodes()
print(pretty(N(n.layers[2].nodes, precision), use_unicode=True))
print(pretty(N(n.layers[3].nodes, precision), use_unicode=True))
print(pretty(N(n.layers[3].weights, precision), use_unicode=True))


#n.layers[3].backProp(n.layers[2].nodes, Matrix([[1,1,1,1]]), 0.5)

#print(n.print(1,0,0))
