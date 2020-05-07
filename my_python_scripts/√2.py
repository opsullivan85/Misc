from numpy import log2
from math import ceil
import random
import timeit
precision=10000

def main():
    n=1
    d=1
    f=''
    for _ in range(ceil(log2(precision))+2):
        n,d=n**2+2*d**2,2*d*n
    for _ in range(precision+1):
        q=n//d
        f+=str(q)
        n-=q*d
        d//=10
    print(f[0]+'.'+f[1:])
#main()

print(2)

