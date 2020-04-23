import numpy as np

a = np.arange(-19,17).reshape(6,6)

print(a)
a=-1==np.sign(a)
print(a)

b = np.zeros((a.shape[0]-2,a.shape[1]-2))

with np.nditer(b,flags=['multi_index'], op_flags=['readwrite']) as it:
    for val in it:
        val[...]=np.any(a[it.multi_index] != a[it.multi_index[0]:3+it.multi_index[0],it.multi_index[1]:3+it.multi_index[1]])

print(b)
print(a[1:3+1,:3])
