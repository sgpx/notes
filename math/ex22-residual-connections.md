# residual connections vs vanishing gradient problem

for any approximation y = F(x) of function y = f(x), the loss function L is given by the chain rule

dL/dx = (dL/dy) * (dF(x)/dx)

F(x) is made of several layers

for example,

F(x) = W2*h + b2 = g(h)

where h = relu(W1*x + b1)

therefore

dL/dx = dL/dy * dg(h)/dh * dh/dx

eventually for many layers, L can tend to zero

# vanishing gradient problem

for a network with n layers with intermediates like h,i,j,k....

dL/dx = dL/dy * dg_1(h)/dh * dg_2(i)/di * .... * dk/dx

since each of them is passing through a nonlinear activation function like tanh or sigmoid, their magnitude is mostly [0,1)

for N layers, assuming if each term ~ 0.5 on average, then dL/dx = (0.5)^N => a*e^-N which is near zero where a is some constant

# how resnet solves vanishing gradients

resnet solves the problem by using skip connections

skip connections allow gradients to flow through multiple connections without nonlinear activations

instead of learning F(x) directly, the network learns

y = F(x) + x

therefore dL/dx = dL/dy * (1+dF(x)/dx)

the extra "1" here ensures that gradients can flow directly to earlier layers without passing through the learned function F(x), preventing vanishing gradients regardless of how many layers deep the network is.
