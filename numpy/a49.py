import numpy as np

x = np.arange(5)
y = np.arange(5)
print(x,y)
X, Y = np.meshgrid(x, y)
print(X, Y)
print(X.ravel(), Y.ravel())
