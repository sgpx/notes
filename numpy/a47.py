"""
Given two vectors a = ([1,,2,,-3]) and b = ([4,,-1,,2]) in ℝ³, compute their inner (dot) product (\mathbf{a}\cdot\mathbf{b}). Then, using the result, determine the angle (\theta) between the two vectors. Finally, scale vector a by (\sin(\theta)) and compute the Euclidean norm of the scaled vector.

given 2 vectors a = [1,2,-3] and b = [4,-1,2] in R^3

compute their dot product

using the result, determine the angle theta between the two vectors

finally scale the vectors by sin(theta) and compute the euclidean norm of the scaled vector
"""

import numpy as np

a = np.array([1,2,-3])
b = np.array([4,-1,2])

dot_product = np.dot(a,b)

"""
A.B = ||A||.||B||.cos(theta)

=>

cos(theta) = A.B/(||A||.||B||)
"""

norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

cos_theta = dot_product/(norm_a*norm_b)

theta_rads = np.arccos(cos_theta)

sin_theta = np.sin(theta_rads)

a_scaled = sin_theta * a
b_scaled = sin_theta * b

norm_a_scaled = np.linalg.norm(a_scaled)
norm_b_scaled = np.linalg.norm(b_scaled)


