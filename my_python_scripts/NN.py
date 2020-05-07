import sympy as sp
import numpy as np
from numpy.random import *
import tensorflow as tf

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


x ,g, n = sp.symbols('x g n')
np.set_printoptions(precision=5, floatmode='fixed')

class NN(object):
    def __init__(self):
        self.layers = []
        self.numLayers = 0

    def __getitem__(self, index):
        return self.layers[index]

    def __str__(self):
        s = ''
        for layer in self.layers:
            s += layer.__str__()
        return(s)

    def add(self, layer):
        self.numLayers += 1
        self.layers.append(layer)
        layer.network = self
        layer.index = self.numLayers-1

    def build(self):
        for layer in self.layers:
            layer.build()

    def eval(self):
        for layer in self.layers:
            layer.eval()

        return self[-1].nodes

    def input(self, values, evaluate=True):
        assert values[None, :].shape == self[0].shape, 'Input shape must match network first layer shape.'

        self[0].nodes = values[None,:]
        
        if evaluate: return self.eval()

    def backProp(self, goal, learningRate, lossFunc = (g-n)**2):

        #for layer in reversed(self.layers):
        #    layer.updateOuter()
        
        self.layers[-1].backProp(lossFunc, goal)
        for layer in reversed(self.layers[:-1]):
            layer.backProp()
            layer.descend(learningRate)
            layer.updateOuter()

        #for layer in reversed(self.layers):
        #    layer.descend(learningRate)

    def loss(self, lossFunc, goal):
        return(np.sum(sp.lambdify((g,n), lossFunc, 'numpy')(goal, self[-1].nodes)))

    def train(self, data, epocs, report = 1):
        

class layer(object):
    def __init__(self, shape):
        #Make sure the layer class is not being used itself
        assert not self.__class__.__name__ == 'layer', 'Layer should only be used as a parent class'

        self.network = None
        self.index = None
        self.nodes = np.zeros(shape)[None, :]
        self.shape = self.nodes.shape
        self.normFunc = lambda x: x
        self.normFuncDer = lambda x: 1
        self.outer = self.normFuncDer(self.nodes)
        #self.lossFunc = None

        #Derivative of the lo
        self.dLdn = None


    def __str__(self):
        s = ''
        s += f'{self.__class__.__name__} [{self.index}]:\n\n'
        s += 'Nodes:\n'
        s += np.array2string(self.nodes) + '\n'
        s += '\n'
        return(s)

    @classmethod
    def addtoNetwork(cls, nn, **kwargs):
        nn.add(cls(**kwargs))

    #This function should serve to finalize setup of the layer
    #with respect to its neighbors in the network
    def build(self):
        raise(Exception(f"The {self.__class__.__name__} class must implent its"
                        f" own build function"))

    #This function should update the layer's nodes
    #with respect to its neighbors in the network
    def eval(self):
        raise(Exception(f"The {self.__class__.__name__} class must implent its"
                        f" own eval function"))

    def backProp(self):
        raise(Exception(f"The {self.__class__.__name__} class must implent its"
                        f" own backProp function"))
        
    #the whole outer system should die...
    def updateOuter(self): 
        raise(Exception(f"The {self.__class__.__name__} class must implent its"
                        f" own updateOuter function"))

    
    def descend(self, *args, **kwargs):
        pass

class denseLayer(layer):
    def __init__(self, normFunc=x, weightInitMode='rand1', biasInitMode='rand1', **kwargs):
        super().__init__(**kwargs)
        
        self.normFunc = sp.lambdify(x, normFunc, 'numpy')
        self.normFuncDer = sp.lambdify(x, normFunc.diff(x), 'numpy')
        
        self.weights = None
        self.weightInitMode = weightInitMode
        self.biases = None
        self.biasInitMode = biasInitMode

    def __str__(self):
        s = ''
        s += f'{self.__class__.__name__} [{self.index}]:\n\n'
        s += 'Weights:\n'
        s += np.array2string(self.weights) + '\n'
        s += '\n'
        s += 'Nodes:\n'
        s += np.array2string(self.nodes) + '\n'
        s += '\n'
        s += 'Biases:\n'
        s += np.array2string(self.biases) + '\n'
        s += '\n'
        return(s)

    def build(self):
        #setup weights
        if(self.weightInitMode=='zeros'):
            self.weights = np.zeros((self.network[self.index-1].shape[1],self.shape[1]))
        elif(self.weightInitMode=='rand1'):
            self.weights = np.array(random_sample((self.network[self.index-1].shape[1],self.shape[1]))*2-1)
            
        #setup biases
        if(self.biasInitMode=='zeros'):
            self.biases = np.zeros((1,self.shape[1]))
        elif(self.biasInitMode=='rand1'):
            self.biases = np.array(random_sample((1,self.shape[1]))*2-1)

    def eval(self):
        self.nodes = self.normFunc(np.dot(self.network[self.index-1].nodes, self.weights) + self.biases)

    def updateOuter(self):
        self.outer = self.normFuncDer(np.dot(self.network[self.index-1].nodes, self.weights) + self.biases)

    def backProp(self):
        nextLayer = self.network[self.index+1]
        prevLayer = self.network[self.index-1]
        
        self.dLdn = np.sum(nextLayer.outer*nextLayer.weights*nextLayer.dLdn,axis=1)[None,:]
        self.dLdb = self.outer*self.dLdn
        #self.dLdw = np.dot((prevLayer.outer*prevLayer.nodes).T,self.dLdn)
        self.dLdw = np.dot(prevLayer.nodes.T,self.dLdn)
        #dL/dn = sum for x in p {(dp_x/dn)*(dL/dp_x)}
        return([self.dLdw, self.dLdb])

    def descend(self, learningRate, grad = None):
        if grad = None:            
            self.weights -= self.dLdw*learningRate[0]
            self.biases -= self.dLdb*learningRate[1]
        else:
            dLdw, dLdb = grad
            self.weights -= dLdw*learningRate[0]
            self.biases -= dLdb*learningRate[1]

class inputLayer(layer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        pass

    def eval(self):
        pass

    def backProp(self):
        pass

    def updateOuter(self):
        self.outer = self.normFuncDer(self.nodes)

class outputLayer(layer):
    #super().__init__ is not used
    #because this object should
    #not be passed a shape
    def __init__(self, normFunc=x):
        self.network = None
        self.index = None
        self.nodes = None
        self.shape = None
        self.normFunc = sp.lambdify(x, normFunc, 'numpy')
        self.normFuncDer = sp.lambdify(x, normFunc.diff(x), 'numpy')
        self.outer = None
        

    def build(self):
        self.updateOuter()
        self.nodes = self.network[-2].nodes
        self.shape = self.nodes.shape
        self.weights = np.eye(self.shape[1])

    def eval(self):
        self.nodes = self.normFunc(self.network[-2].nodes)

    def updateOuter(self):
        self.outer = self.normFuncDer(self.nodes)

    def backProp(self, lossFunc, goal):
        #Derivative of the loss function with respect to each output node
        self.dLdn = sp.lambdify((g,n), lossFunc.diff(n), 'numpy')(goal, self.nodes)
        #dL/dn = lossFunction'(goal, output layer)

    def descend(self, *args, **kwargs):
        pass

getData = 1
if(getData):
    print("Loading Data...", end="")
    mnist = tf.keras.datasets.mnist
    (x_train, y_train),(x_test, y_test) = mnist.load_data()
    x_train, x_test = x_train / 255.0, x_test / 255.0
    print("Done!")

network=NN()

network.add(inputLayer(shape=28**2))
network.add(denseLayer(shape=28, normFunc=sp.tanh(x)/2+0.5))
network.add(denseLayer(shape=28, normFunc=sp.tanh(x)/2+0.5))
network.add(denseLayer(shape=10, normFunc=sp.tanh(x)/2+0.5))

network.add(outputLayer())

network.build()

learningRate = (0.0001,0.0001)

lossFunc = (g-n)**2

epochs=10
batchSize=1000
testSize=20
finalTestSize=1000

for i in range(batchSize):
    #Input and update NN
    network.input(np.ravel(x_train[(epoch*batchSize+i)%60000]))

    #Get solution in correct format
    solution = np.zeros((1, 10))
    solution[0, y_train[(epoch*batchSize+i)%60000]] = 1

    network.backProp(goal=solution, learningRate=learningRate, lossFunc=lossFunc)


print(network)
print(solution)

fig = plt.figure()
ax = fig.subplots()
#fig.show()
