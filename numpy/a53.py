"""
Create a 1D NumPy array of values, then use vectorized operations to calculate:

    The cumulative sum using np.cumsum()
    The cumulative average after each element
    Verify the final cumulative average equals the array’s overall mean

Given the array [4, 7, 2, 9, 5], compute and print its cumulative sum and cumulative average without using Python loops.

"""

import numpy as np
a = np.array([4, 7, 2, 9, 5], dtype=np.float32)
b = np.cumsum(a)/np.arange(1,6)
print(a, np.cumsum(a), b, np.isclose(np.mean(a), b))
