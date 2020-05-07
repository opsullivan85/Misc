from random import random, randint
import time

choices = ['x y z tmp'.split(),#Variables
           'print wait'.split()#Const Functions
           'func split'.split(),#Functions
           ]

def leetHacker():
    indent = 0
    defining = 0
    for _ in range(10):
        

def simType(string):
    
    for c in string:
        #print(random())
        print(c, end='')
        wait()
        #time.sleep(random()%timeRange[0]+(timeRange[1]-timeRange[0]))

def wait(timeRange = (0.025,0.1)):
    time.sleep(random()*(timeRange[1]-timeRange[0])+timeRange[0])

simType("Hello There!")
