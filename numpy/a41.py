# Write a NumPy program to manually compute the derivative of the Sigmoid function f(x)=σ(x)(1−σ(x)) on an array of 10 random floats. Add a numerical finite-difference gradient check and assert that it matches the analytical sigmoid derivative.
"""

y = sigmoid(x) = 1/(1+e^-x)

dy/dx = d/dx((1+e^-x)^-1)

let u = 1+e^-x

therefore dy/dx = du^-1/du * du/dx

= (-1*(1+e^-x)^-2)*(-e^-x)
= e^-x/(1+e^-x)^2

if let v = -x

-(de^v/dv) = -e^v = -e^-x

d(e^-x)/dx = -e^-x

analytical gradient

f(x) = 1/(1+e^-x)

when lim : h->0, df/dx = f(x+h)-f(x-h)/(x+h)-(x-h) = f(x+h)-f(x-h)/2h
"""


import numpy as np

X = np.random.rand(10,1)
print(X)
sigmoid = lambda x : 1/(1+np.exp(-x))

#f = lambda x : sigmoid(x) * (1 - sigmoid(x))

df_dx = lambda x : np.exp(-x) / (1 + np.exp(-x))**2

grad = df_dx(X)

print(grad)

h = 1e-5

f_plus_h = sigmoid(X + h)
f_minus_h = sigmoid(X - h)

num_grad = (f_plus_h - f_minus_h) / (2*h)

print(np.allclose(num_grad, grad))
assert np.allclose(num_grad, grad)
