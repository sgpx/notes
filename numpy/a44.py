"""
### 📐 **3. Linear Algebra / Math Domain**  
**Context**: You’ve studied eigenvalues, SVD, and Hessian (e.g., `math/ex09-svd-eigenvalues.md`, `math/ex13-hessian-matrix.md`).  
**Problem**:  
> Given a symmetric matrix `A = [[4, 1], [1, 4]]`:  
> - **Part 1**: Compute its **eigenvalues and eigenvectors** manually using the characteristic equation `det(A - λI) = 0`.  
> - **Part 2**: Verify your result using **NumPy’s `np.linalg.eigh()`** (not `eig()`).  
> - **Part 3**: **Bonus**: Explain *why* `eigh()` is preferred for symmetric matrices (hint: numerical stability and efficiency).  
> **Output**: Print eigenvalues/eigenvectors from both manual and NumPy methods.  

> **Why this tests your math skills**:  
> Directly applies `math/ex03-eigenvectors-matrixA.md` and `math/ex09-svd-eigenvalues.md`. The bonus tests *deeper conceptual understanding* of linear algebra optimizations (beyond rote calculation).

# solution

A
=
4 1
1 4

det(A - lambda*I) = 0

4-lambda 1
1 4-lambda

(4-lambda)^2 - 1 = 0

16+lambda^2-2*4*lambda-1=0

15 + lambda^2 - 8*lambda = 0

(lambda-3)(lambda-5) = 0

lambda = 3,5

if lambda = 3


A*v = lambda*v

4 1 * a = 3a
1 4   b   3b

4a+b = 3a
a+4b   3b

4a+b = 3a
a+4b = 3b

a+b = 0

a = -b, therefore v1 = [-1 1]

if lambda = 5

4a+b = 5a
a+4b   5b

=> 
b = a
a = b

which leads to a = b

therefore v2 = [1 1]

coff_normalize = sqrt(a^2 + b^2) = sqrt(1 + 1) = sqrt(2)

V = -1/sqrt(2) 1/sqrt(2) = (1/coff_normalize) * v1
    1/sqrt(2) 1/sqrt(2)                        v2
"""

import numpy as np

a = [[4,1],[1,4]]
eigval, eigvec = np.linalg.eigh(a)
print(eigval, eigvec)

"""
eigh is preferred because

- numerical stability: algorithms like householder's algorithm are designed for symmetric matrices and reduce rounding errors
- efficiency: symmetric matrices have half the info of general matrices so eigh() exploits this
- guaranteed real eigenvalues: for symmetric matrices, the eigenvalues are guaranteed to be real
- works only for symmetric matrices: if a non-square matrix is used in eigh() it will throw a error
"""
