"""
Given a 2x3 matrix A = [[1, 2, 3], [4, 5, 6]] and a 3x2 matrix B = [[7, 8], [9, 10], [11, 12]], compute the product C = A × B manually using the standard matrix multiplication rule. Show each element of C and verify the result with a 3-line PyTorch script.

# solution

A 

=

1 2 3
4 5 6

B

= 

7 8
9 10
11 12

AxB

=

7+18+33 8+20+36
28+45+66 32+50+72

=

58 64
139 154
"""

import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]] )
B = np.array([[7, 8], [9, 10], [11, 12]])
C = A @ B

res = np.array([[58,64],[139,154]])

print(np.isclose(res, C))
