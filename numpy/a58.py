"""
Write a 6-line NumPy function stable_softmax(x) that subtracts max(x) from the input vector before applying np.exp() and normalizing

Objective: Test it against the naive implementation on the vector x = np.array([1000.0, 1001.0, 1002.0]) to confirm that naive evaluation yields nan due to floating-point overflow while the stable implementation produces valid probabilities.

"""

import numpy as np
from typing import List

def stable_softmax(x : np.array) -> np.array:
	x_max = np.max(x)	
	x2 = x - x_max
	x3 = np.exp(x2)
	x_norm = x3 / np.sum(x3)
	return x_norm

def naive_softmax(x : np.array) -> np.array:
	x2 = np.exp(x)
	return x2 / np.sum(x2)

"""
# overflow code
import math
def naive_softmax(x : List[float]) -> List[float]:
	x2 = [math.exp(i) for i in x]
	s = sum(x2)
	return [i/s for i in x2]
"""

ref = [1000.0, 1001.0, 1002.0]
nref = np.array(ref, dtype=np.float32)
r1 = stable_softmax(nref)
r2 = naive_softmax(nref)

print(np.isclose(r1, r2, atol=1e-5, rtol=1e-5))

