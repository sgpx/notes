### Next Topic: NumPy Linear Algebra - Eigenvalues and Eigenvectors

### Problem: Write a function that computes the eigenvalues and eigenvectors of a square matrix using `numpy.linalg.eig()`. Create a random (3 times 3) matrix and print the matrix alongside its eigenvalues and eigenvectors.

### Learning Resource: Familiarize yourself with the concepts of eigenvalues and eigenvectors, and how they are used in various applications like PCA (Principal Component Analysis) or solving systems of linear equations.

import numpy as np

a = np.random.randint(1,10,(3,3))
print(a, np.linalg.eig(a))
