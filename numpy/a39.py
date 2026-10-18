# Write a NumPy program to compute the Hessian matrix for the function f(x,y)=3x^2 +2y^2 given x = 2 and y = 3

"""
# hessian matrix

for a function z = f(x,y)

the hessian matrix of the function is a matrix of second derivatives of the function

H(f)

=

d^2(f)/dx^2 d^2(f)/dxdy

d^2(f)/dydx d^2(f)/dy^2

---

for f(x,y) = 3x^2 + 2y^2

d^2(f)/dx^2 = 6

d^2(f)/dy^2 = 4

d^2(f)/dxdy = d(df/dx)/dy = 0

d^2(f)/dydx = d(df/dy)/dx = 0

therefore, 

H(f) 

=

6 0
0 4
"""

# ===
import numpy as np

f = lambda x,y : (3*x**2) + (2*y**2)

val = f(2,3)

print(val)

res = np.array([[6,0],[0,4]])
print(res)


