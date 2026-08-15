"""
Monte Carlo Estimation of π

Generate N = 2,000,000 points uniformly at random in the unit square [0,1) × [0,1) using NumPy. Count how many fall inside the quarter-circle x² + y² ≤ 1 using a boolean mask. Estimate π as 4 * (count / N). Print your estimate, the absolute error versus np.pi, and the relative error in percent. Use only vectorized operations (no Python loops). Keep it under 15 lines.
"""

import numpy as np

N = 2_000_000
a = np.random.rand(N, 2)

x = a[:,0]
y = a[:,1]

mask = (x**2 + y**2 <= 1)
result = a[mask]

pi = 4 * len(result)/N

err = np.abs(np.pi - pi)
print(err)

