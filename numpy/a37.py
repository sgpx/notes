"""

# SVD

we can decompose a matrix `A` into

A = U * sigma * V^T

where U is left singular matrix, V is right singular matrix and sigma is diagonal matrix filled of singular values sigma_i, where sigma_i is non-negative

let A = [[3,1],[1,3]]

first we calculate

A^T*A  = [[3,1],[1,3]] * [[3,1],[1,3]]


3*3+1*1 3*1+1*3
1*3+3*1 1*1+3*3

A^T*A 

= 

10 6

6  10


to find eigenvalues, 

det((A^T*A)-lambda*I) = 0

det |10-lambda 6| = 0
    |6 10-lambda|


100+lambda**2=20lambda - 36 = 0

(16-lambda)*(4-lambda) = 0

lambda = 4,16


singular values are square roots of eigenvalues => 2,4

sigma = [[4,0],[0,2]]

Av = Lv

(A-L)v = 0

for lambda equals = 4

10-4 6-0 = 6 6
6-0 10-4   6 6

10-2 6-0 = 8 6
6-0 10-2   6 8



6 6 * v1 = 0
6 6   v2 
   
6v1+6v2 = 0
=> v1 = -v2

eigenvector = 1
              -1

normalized = 1/sqrt(2)
             -1/sqrt(2)

V = 1/sqrt(2) 1/sqrt(2)
    1/sqrt(2) -1/sqrt(2)

for lambda = 16


-6 6 * v1 = 0
6 -6   v2   0

-6v1 + 6v2 = 0
6v1 - 6v2 = 0

v1 = v2


eigenvector = [1 1]

V = 1/sqrt(2) 1/sqrt(2)
    1/sqrt(2) 1/sqrt(2)

AxV = 3 1 x 1/sqrt(2) 1/sqrt(2) = 4/sqrt(2) 2/sqrt(2) = 2*sqrt(2) sqrt(2)
      1 3   1/sqrt(2) -1/sqrt(2)  4/sqrt(2) -2/sqrt(2)  2*sqrt(2) -sqrt(2)

sigma = 4 0
        0 2

sigma_inv = a b
            c d


sigma*sigma_inv = I

4a 4b = 1 0
2c 2d   0 1

a = 1/4
b = 0
c = 0
d = 1/2

sigma_inv = 1/4 0
            0  1/2

U = A * V * sigma_inv = 2*sqrt(2) sqrt(2) * 1/4 0 = 1/sqrt(2) 1/sqrt(2)
                        2*sqrt(2) -sqrt(2)  0 1/2   1/sqrt(2) -1/sqrt(2)

for verification

A = U*sigma*V^T

=

1/sqrt(2) 1/sqrt(2) * 4 0 * 1/sqrt(2) 1/sqrt(2)
1/sqrt(2) -1/sqrt(2)  0 2   1/sqrt(2) -1/sqrt(2)


= 4/sqrt(2) 2/sqrt(2) * 1/sqrt(2) 1/sqrt(2)
  4/sqrt(2) -2/sqrt(2)  1/sqrt(2) -1/sqrt(2)

= 4/2 + 2/2 4/2-2/2
  4/2 - 2/2 4/2+2/2

= 2+1 2-1
  2-1 2+1

= 3 1
  1 3


"""
import numpy as np

A = np.array([[3,1],[1,3]])
A_T = A.T
prod = A_T @ A

eigenvalues, eigenvectors = np.linalg.eig(prod)

idx = np.argsort(eigenvalues)
idx = idx[::-1] # largest first
eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]

s = np.sqrt(np.real_if_close(eigenvalues))
s.sort()
l1 = s[-1]

print(np.diag(s))
print(prod)
print(l1)

sol = prod - l1*np.eye(2)
dt = np.linalg.det(sol)
print(dt)

V = eigenvectors
S_inv = np.diag(1/s)
U = A @ V @ S_inv

print(U)

V_T = V.T

print("U =\n", U)
print("Sigma =\n", s)
print("V_T =\n", V_T)

print("U @ Sigma @ V_T =\n", U @ np.diag(s) @ V_T)
