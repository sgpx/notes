##Topic: Array Indexing and Slicing##

##Challenge:## Create a function that takes a 4x4 NumPy array and returns a new array containing only the diagonal elements. Then calculate the sum of these diagonal elements.

import numpy as np

def fxn(x):
    b = np.array([])
    for i in range(4):
        b=np.append(b, x[i,i])
        #b=np.append(b, x[4-i-1,i])
    return b

a = (np.random.rand(4,4)*100).astype(int)
print(a, fxn(a), sum(fxn(a)))
