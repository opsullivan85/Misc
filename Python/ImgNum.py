import math
import cmath
from functools import singledispatch

class ImgNum:
    
    
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def __add__(self, num):
        return ImgNum(self.a + num.a, self.b + num.b)

    def __str__(self):
        return(str(self.a) + "+" + str(self.b) + "i")

num = ImgNum(1,1)
num1 = num + 1
num2 = num + num
print(num1)
print(num2)
