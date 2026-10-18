"""
Write an exact 3-line NumPy script that creates a 6×6 matrix containing consecutive integers from 0 to 35, and extracts all elements that sit on both an even row index and an odd column index into a flat 1D array.
"""

import numpy as np
print(np.arange(0,36).reshape(6,6)[::2,1::2].flatten())
