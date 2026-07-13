"""

# Problem 1: Write a Python function to compute eigenvalues of a 2×2 matrix by hand (solve characteristic equation). Test on [[4, 2], [1, 3]].


let

A

=

p q
r s


A-lambda*I

=

p - lambda q
r s - lambda


det(A-lambda*I) = 0

= (p-lambda)*(s-lambda) - (q*r) = 0

= p*s + lambda^2 - ((p+s)*lambda) - (q*r) = 0

= (p*s - q*r) + lambda^2 - ((p+s)*lambda) = 0

lambda = (-b +- sqrt(b^2 - 4ac))/2a 

term = (p+s)^2 - 4*(p-s)

"""

import numpy as np
import math

arr = [[4,2],[1,3]]

def get_eigenvalues(A):
	[[p,q],[r,s]] = A
	_a = 1
	_b = -(p+s)
	_c = (p*s) - (q*r)
	_q = math.sqrt(_b**2 - 4*_a*_c)
	factor1 = (-_b + _q)/(2*_a)
	factor2 = (-_b - _q)/(2*_a)
	return factor1, factor2


e1,e2 = get_eigenvalues(arr)

eig = np.linalg.eig(np.array(arr))
print(eig[0], e1, e2)
