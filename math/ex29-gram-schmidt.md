# Gram-Schmidt orthonormalization

- takes a set of linearly independent vectors
- transforms them into an orthonormal basis

# orthonormal basis

vectors that are mutually perpendicular and each has a unit length of 1

# writing out the classical Gram-Schmidt orthonormalization steps for a 2x2 matrix

for two vectors A = a_1*i + a_2*j and B = b_1*i + b_2*j the orthonormal unit vectors are q1 and q2

u1 = A

magn_A = sqrt(a_1**2 + a_2**2)

q1 = u1/|u1| = (a_1/magn_A) * i + (a_2/magn_A) * j

u2 = B - projection(B, q1)

where projection(B, q1) = (B.q_1)*q_1

q2 = u2/|u2|

if we are trying to do gram schmidt orthonormalization to a 2x2 matrix, it means we are treating the two columns vectors C1 and C2 as input vectors in our above process

# writing out the classical Gram-Schmidt orthonormalization steps for a 3×3 matrix

for 3 vectors v1, v2, v3

u1 = v1
q1 = u1/|u1|

u2 = v2 - projection(v2, q1)
q2 = u2/|u2|

u3 = v3 - projection(v3, q1) - projection(v3, q2)
q3 = u3/|u3|


# for NxN matrix

for N vectors v1, v2, v3 ... vN

u1 = v1
q1 = u1/|u1|

u2 = v2 - projection(v2, q1)
q2 = u2/|u2|

u3 = v3 - projection(v3, q1) - projection(v3, q2)
q3 = u3/|u3|

u4 = v4 - projection(v4, q1) - projection(v4, q2) - projection(v4, q3)
q3 = u4/|u4|

...

uk = vk - summation(from i=1, to i=k-1)( projection(v_k, q_i) )
qk = uk/|uk|

the resulting orthonormal vectors become the set Q = { q_1 ... q_N }

therefore, we can use QR decomposition A = QR

where Q is orthonormal vectors, and R is an upper triangular matrix used to express the original columns v_k in terms of orthonormal vectors from Q

r_ik = q_i^T * v_k (transpose because q_i is a column vector)
