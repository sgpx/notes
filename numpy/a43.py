# Write a NumPy script to manually perform Singular Value Decomposition (SVD) on a 2x2 matrix by finding the eigenvalues of A^T*A

import numpy as np

A = np.random.randint(0,10,(2,2))

print(A)

prod = np.matmul(A.T, A)
print(prod)

eigval, eigvec = np.linalg.eig(prod)

print(eigval)
print(eigvec)

"""

A = U x Sigma x V^T




"""
