# Problem: Create a 1D numpy array of 10 elements evenly spaced between 0 and 1. Then, compute the sine of each element. Goal: Get comfortable with numpy array creation and vectorized operations.


import numpy as np
result = np.sin(np.linspace(0,1,10))
print(result)
