activation functions are added to create non-linearity so that the NN can learn complex relations in training data

if there is no activation function, it just becomes

Y1 = W1*x1 + b1

Y2 = W2*x2 + b2

since x2 is just the output of the first layer y1, x2 = y1

Y2 = W2*(w1*x1 + b1) + b2

Y2 = W2*W1*x1 + W2*b1 + b2

Y = W_overall*x + B_overall

this is not very useful for learning nonlinear relations in data and causes model to fail since it is just one big linear equation

### The "Collapse" of Linear Layers

If you stack multiple linear layers (like `Linear` layers in PyTorch) without activation functions between them, **the entire network collapses into a single linear layer.**

Mathematically, a linear layer is just a matrix multiplication: $f(x) = Wx + b$.

If you have two layers, Layer 1 and Layer 2:

1. Output of Layer 1: $h = W_1 x + b_1$
2. Output of Layer 2: $y = W_2 h + b_2$

If you substitute Layer 1 into Layer 2, you get:


$$y = W_2(W_1 x + b_1) + b_2$$

$$y = (W_2 W_1) x + (W_2 b_1 + b_2)$$

If we define a new weight $W_{new} = W_2 W_1$ and a new bias $b_{new} = W_2 b_1 + b_2$, the equation becomes:


$$y = W_{new} x + b_{new}$$

Even if you stack 1,000 linear layers, the result is still just one simple linear equation. You haven't actually built a "deep" network; you've just built a very inefficient version of a simple regression model!
