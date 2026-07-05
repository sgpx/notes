"""
Math (SVD Foundations): Given the symmetric matrix A=[
3 2
2 3
], find its eigenvalues lambda_1, lambda_2. Because A is symmetric and positive-definite, its singular values sigma_i are simply the absolute values of its eigenvalues (sigma_i = |lambda_i|). Calculate lambda_1, lambda_2 by hand using det(A - lambda * I) = 0.
"""

det(A-lambda*I) = 0

=

|3-lambda 2| = 0
|2 3-lambda|

=

(3-lambda)^2 - 2^2 = 0

=

9-6lambda+lambda^2 - 4 = 0

=

5-6lambda+lambda^2 = 0

using quadratic formula, roots are 1 and 5

(6+-sqrt(36-4*5))/2

= 6+-4/2

= 1 and 5
