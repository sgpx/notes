This problem is designed to be simple, directly applicable to the foundational math of neural networks (weights and biases), and focuses purely on matrix arithmetic.

---

## 🧠 The Deep Learning Math Challenge: Layer Transformation

### Scenario: The Simple Network Layer

Imagine you are building a very simple, two-layer neural network. The performance of this network depends entirely on how we manipulate the weight matrices assigned to each layer.

In this problem, we will use **Matrix Addition** (combining layer information) and **Scalar Multiplication** (adjusting the influence of a layer).

### The Data (The Matrices)

We have two weight matrices, $W_1$ and $W_2$, which represent the learned parameters for Layer 1 and Layer 2, respectively.

$$W_1 = \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix}$$

$$W_2 = \begin{pmatrix} 1 & 5 \\ 2 & 4 \end{pmatrix}$$

### The Transformation (The Scalar)

We need to apply a scaling factor (a scalar) to the weights of Layer 1. Let the scalar be $c = 2$.

---

### The Tasks (The Deep Learning Math)

Solve the following problems:

**Task 1: Scalar Multiplication (Adjusting Layer 1)**
Calculate the new weights for Layer 1 ($W_{1}'$) by multiplying every element in $W_1$ by the scalar $c=2$.

$$W_{1}' = c \cdot W_1$$

**Task 2: Matrix Addition (Combining Layers)**
Calculate the combined weight matrix ($W_{total}$) by adding the adjusted Layer 1 weights ($W_{1}'$) and the original Layer 2 weights ($W_2$).

$$W_{total} = W_{1}' + W_2$$

---

## Answer

W_1 

=

3 1
0 2


W_2

=

1 5
2 4

W_total = c * W_1 + W_2

= 2 * W_1 + W_2

= 6 2 + 1 5
  0 4   2 4

= 7 7
  2 8
