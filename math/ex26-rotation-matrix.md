# rotation matrix

for a column vector [x,y]

the rotation matrix is a square matrix multiplying by which the point gets rotated by theta degrees counterclockwise

R(theta)

=

cos(theta) -sin(theta)
sin(theta) cos(theta)



let A_rotated = R(theta) x A

x' = cos(theta) -sin(theta) . x
y'   sin(theta) cos(theta)  . y

=>

x' = x.cos(theta) - y.sin(theta)
y'   x.sin(theta) + y.cos(theta)

# properties

- the inverse of a rotation matrix is euqal to its transpose i.e. R^-1 = R^T
- determinant is always exactly 1 because cos^2(theta) + sin^2(theta) = 1
- multiplication with R(theta) does not shrink or expand the vector i.e. |A_rotated| = |
