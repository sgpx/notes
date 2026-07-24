Q. Calculate the final prediction score by performing a matrix multiplication (dot product) and adding a bias.

### The Data (The Matrices)

**1. Input Data Matrix ($X$):** This is the feature vector we are feeding into the model.
$$X = \begin{bmatrix} 2 \\ 5 \end{bmatrix}$$
(Feature 1 = 2, Feature 2 = 5)

**2. Weight Matrix ($W$):** These are the parameters the model "learned" during training.
$$W = \begin{bmatrix} 0.5 \\ 1.5 \end{bmatrix}$$
(Weight for Feature 1 = 0.5, Weight for Feature 2 = 1.5)

**3. Bias ($b$):** A simple constant added to the result.
$$b = 3.0$$

### The Task

Calculate the final prediction ($P$) using the formula:
$$P = (X \cdot W) + b$$


## answer

P = X.W + b

X = [[2],[5]]

W = [[0.5],[1.5]]

X.W = 2*0.5 + 5*1.5 = 1 + 7.5 = 8.5

P = 8.5 + 3
P = 11.5
