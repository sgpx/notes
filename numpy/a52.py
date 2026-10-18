"""
Write a 10-line script computing a 1D running moving average over an array using np.convolve with mode 'valid'.
"""

import numpy as np

data = np.arange(1,10+1)
print(data)

window_size = 3

kernel = np.ones(window_size) / window_size

moving_avg = np.convolve(data, kernel, mode='valid')

print(f"Original data: {data}")
print(f"Moving average (window={window_size}): {moving_avg}")

"""
>>> import numpy as np
>>> b = np.array([1, 2, 3])
>>> a = np.array([1, 2, 3])
>>> np.convolve(a,b,'valid') # = 3+4+3
array([10])
"""
