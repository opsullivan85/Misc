import numpy as np

def auc(func, interval, num):
    b = (interval[1] - interval[0])/num
    print(np.linspace(interval[0], interval[1]-b, num))
    
    rram = b*np.sum(func(np.linspace(interval[0]+b, interval[1], num)))
    print("RRAM: ", rram)

    lram = b*np.sum(func(np.linspace(interval[0], interval[1]-b, num)))
    print("CRAM: ", lram)

    mram = b*np.sum(func(np.linspace(interval[0]+b/2, interval[1]-b/2, num)))
    print("MRAM: ", mram)

auc(lambda x:2**x+3, (0,2), 4)
