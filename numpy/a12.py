import numpy as np

def fxn(x):
    # Extract the diagonal elements
    b = np.diagonal(x)
    return b

a = (np.random.rand(4,4) * 100).astype(int)
diagonal_elements = fxn(a)
diagonal_sum = np.sum(diagonal_elements)

print(a, diagonal_elements, diagonal_sum)