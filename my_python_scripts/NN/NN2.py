from sympy import *
#from sympy.matrices import matrix_multiply_elementwise
import numpy as np
from numpy.random import *
#from mpmath import *

x = symbols('x')
np.set_printoptions(precision=3)#, floatmode='fixed')

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
        
    def calcNodes(self):
        for i, layer in enumerate(self.layers[1:]):
            layer.calcNodes(self.layers[i].nodes)
            
    def input(self, val):
        self.layers[0].setNodes(val)
        
    def output(self):
        return pretty(self.layers[-1].nodes, precision)
    
class layer:
    def __init__(self, size, prevSize, fx=lambda x:x, layerType=None, weightMode='rand', biasMode='rand'):
        self.size = size
        self.nodes = np.empty((1, size))
        self.type = layerType
        self._initWeights(prevSize, weightMode)
        self._initBiases(biasMode)
        self.fx = lambdify(x, fx, 'numpy')
        self.derivative = lambdify(x, fx.diff(x), 'numpy')
        
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
        #print(self.fx(np.dot(prevNodes, self.weights) + self.biases))
        print(type((np.dot(prevNodes, self.weights) + self.biases)[0,0]))
        self.nodes = self.fx(np.dot(prevNodes, self.weights) + self.biases)

    def backProp(self, prevNodes, goal, learningRate):
        functionDerivative = self.derivative(np.dot(prevNodes, self.weights) + self.biases)
        #WEIGHTS
        weightChange = np.dot(prevNodes.transpose(), functionDerivative)
        #print(np.array2string((goal - self.nodes)))
        weightScalar = ((goal - self.nodes).transpose() / prevNodes).transpose()

        weightChange = np.multiply(weightChange, weightScalar)
        self.weights = self.weights + weightChange
        #BIASES
        biasChange = functionDerivative
        #NODES
        nodeChange = (np.dot(self.weights, functionDerivative.transpose())).transpose()
        
def main():
    np.set_printoptions(suppress=True)
            #lambda x:atan(x)*2/pi
    f = atan(x)*2/pi
    n = nn()
    n.addLayer(5, f)
    n.addLayer(4, f)
    n.addLayer(2, f)
    n.addLayer(4, f)
    n.input(np.array([[.1,.1,.1,.1,.1]]))
    n.calcNodes()
    #print(n.print(1,0,0))
    n.layers[3].backProp(n.layers[2].nodes, np.matrix([[1,1,1,1]]), 0.5)
    n.calcNodes()
    #print(n.output())
    #print(n.print(1,0,0))



#n.layers[3].backProp(n.layers[2].nodes, Matrix([[1,1,1,1]]), 0.5)
main()
#print(n.print(1,0,0))
