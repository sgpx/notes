# PyTorch Tensor Indexing: Generate 10 random points in a 2D plane and plot them on a scatterplot

import torch
import matplotlib.pyplot as plt

points = torch.rand(10,2)
X = points[:,0] # all rows, first column
Y = points[:,1] # all rows, first column

plt.scatter(X, Y)
plt.show()
