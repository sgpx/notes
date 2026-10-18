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

## ✅ Step-by-Step Solution

### Task 1: Scalar Multiplication

**Goal:** Calculate $W_{1}' = 2 \cdot W_1$

To do this, multiply every element in $W_1$ by 2:

$$W_{1}' = 2 \cdot \begin{pmatrix} 3 & 1 \\ 0 & 2 \end{pmatrix} = \begin{pmatrix} 2 \times 3 & 2 \times 1 \\ 2 \times 0 & 2 \times 2 \end{pmatrix}$$

$$\mathbf{W_{1}' = \begin{pmatrix} 6 & 2 \\ 0 & 4 \end{pmatrix}}$$

---

### Task 2: Matrix Addition

**Goal:** Calculate $W_{total} = W_{1}' + W_2$

Add the corresponding elements of the two matrices calculated above:

$$W_{total} = \begin{pmatrix} 6 & 2 \\ 0 & 4 \end{pmatrix} + \begin{pmatrix} 1 & 5 \\ 2 & 4 \end{pmatrix}$$

$$W_{total} = \begin{pmatrix} 6+1 & 2+5 \\ 0+2 & 4+4 \end{pmatrix}$$

$$\mathbf{W_{total} = \begin{pmatrix} 7 & 7 \\ 2 & 8 \end{pmatrix}}$$

---

## 💡 Deep Learning Interpretation

**What does this mean in a neural network context?**

1.  **Scalar Multiplication ($W_{1}'$):** This represents **adjusting the influence** of the first layer's learned features. By multiplying by $c=2$, we are effectively doubling the importance or magnitude of the weights associated with the first layer.
2.  **Matrix Addition ($W_{total}$):** This represents **combining** the learned parameters of two different computational layers. $W_{total}$ is a new weight matrix that incorporates the influence of both the scaled Layer 1 and the original Layer 2 into a single combined representation.
