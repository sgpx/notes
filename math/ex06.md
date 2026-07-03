Q.

#### Step 1: Define the Input Data Matrix ($X$)

This matrix represents the input features from a batch of data.
$$X = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$$
(This matrix is $2 \times 3$, meaning 2 rows and 3 columns.)

#### Step 2: Define the Weight Matrix ($W$)

This matrix represents the learned weights of the layer. For the multiplication to be valid, the number of columns in $X$ must equal the number of rows in $W$.
$$W = \begin{pmatrix} 10 & 20 \\ 30 & 40 \\ 50 & 60 \end{pmatrix}$$
(This matrix is $3 \times 2$, meaning 3 rows and 2 columns.)

---

### ❓ The Challenge

**Task:** You need to perform a specific operation: calculating the transpose of the Weight Matrix ($W^T$) and then multiplying the Input Matrix ($X$) by this transposed matrix ($X \cdot W^T$).

**Find the result of the following:**
$$X \cdot W^T$$

---

## answer

A = X.W^T

X = 1 2 3
    4 5 6

W = 10 20
    30 40
    50 60


W^T = 10 30 50
      20 40 60



X.W^T is not possible because 2x3 and 2x3 order matrices are not multiplicable, r1xc1 and r2xc2 matrices can only be multiplied if c1==r2
