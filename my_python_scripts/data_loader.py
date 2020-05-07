import numpy as np

class data_loader:
    def __init__(self, data,):
        self.data = data

    def to_one_hot(self, return_key = False):
        uniques = np.unique(self.data)
        key = {}
        
        for i, val in enumerate(uniques):
            key[val] = i

        one_hot = np.zeros_like(self.data)

        print(one_hot.shape)
d = data_loader(np.arange(5))
d.to_one_hot()
        
