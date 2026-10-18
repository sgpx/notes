"""
Implement 2D image rotation from scratch using a rotation matrix and NumPy broadcasting. Test it on a simple 5×5 coordinate grid.

# rotation matrix

for a column vector [x,y]

the rotation matrix is a square matrix multiplying by which the point gets rotated by theta degrees counterclockwise. for a 2x2 matrix

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

"""

import numpy as np

def rotation_matrix_2d(theta_deg):
	theta = np.deg2rad(theta_deg)
	A = np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])
	return A

N = 5
center = (N - 1) / 2

image = np.random.randn(N,N) # grayscale
coords = np.array([(i, j) for i in range(N) for j in range(N)])
coords_centered = coords - center

R = rotation_matrix_2d(60)
R_inv = R.T

rotated = coords_centered @ R_inv + center
rotated_int = np.round(rotated).astype(int)

output = np.zeros_like(image)

for ((x_out, y_out), (x_orig, y_orig)) in zip(rotated_int, coords):
    if (0 <= y_out < N) and (0 <= x_out < N): # <-- y_out is row, x_out is col
        output[y_out, x_out] = image[y_orig, x_orig]
