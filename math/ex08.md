""""
Math (Eigenvalues & Trace Mechanics): Given the square matrix M=[[4,2],[1,3]], calculate its eigenvalues lambda1 and lambda2 by hand using the characteristic equation det(M−lambda*I)=0.
Show your step-by-step polynomial expansion and final values. (Do not write any code for this drill—calculate it raw).
"""

to find eigenvector v,

Mv = lambda*v

4 2 x v1 = lambda x v1
1 3   v2             v2


=> (M-lambda*I)*v = 0

=> det(M-lambda*I) = 0

=> |4 2 - lambda 0|
   |1 3   0 lambda|

=> |4-lambda 2| = 0
   |1 3-lambda|

=> (4-lambda)*(3-lambda) - (2) = 0
=> 12+lambda^2-7lambda - 2 = 0
=> 10 + lambda^2 - 7lambda = 0

using quadratic formula for ax^2 + bx + c = 0, the roots of x are (-b +- sqrt(b^2-4ac))/2a

here a = 1, b = -7, c = 10

lambda1 = (-(-7) + sqrt(49 - 40))/2 = (7+3)/2 = 5
lambda2 = (-(-7) - sqrt(49 - 40))/2 = (7-3)/2 = 2

