import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import time
import sys

class function:
    def __init__(self, f):
        
        variables = f.__code__.co_varnames
        assert len(variables) < 4, 'This program only supports upto 3 independend variables'
        for i, var in enumerate(variables):
            assert var=='xyz'[i], 'Please use normal variables and variable ordering'


    def plot():
        pass

    def evaluate(interval, step):
        
        

function(lambda x,z,y:1)
