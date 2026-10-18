##Next Topic:## Learn about NumPy broadcasting, which allows you to perform operations on arrays of different shapes.

##Practical Challenge:## Write a function that takes a 2D array of random integers and a 1D array of weights (size corresponding to the number of columns). The function should return a new array where each column of the 2D array is multiplied by the corresponding weight from the 1D array.


import numpy as np


a = (np.random.rand(2,3)*10).astype(int)

b=(np.random.rand(3)*10).astype(int)

print(a,b)
print(a*b)
