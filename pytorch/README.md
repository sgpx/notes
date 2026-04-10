# learnable values 

In your code the main “error” is not a Python crash, but several logical and conceptual issues that make it not a proper linear‑regression training loop:
1. Initializing data and labels with requires_grad=True

You wrote:

python
x = torch.randint(..., requires_grad=True, ...)
y = torch.randint(..., requires_grad=True, ...)

    x and y should be the data, not learnable parameters.

    They should not have requires_grad=True; only W and b should be learnable.

    If you leave them with requires_grad, PyTorch will try to compute gradients w.r.t. the inputs/labels, which is not what you want here.

# x.grad.zero_()  

zeroes gradients

# flatten()

flattens a tensor into a one dimensional tensor without copying data similar to view() and reshape()

flatten(x) defaults to flatten(x, end_dim=-1)

torch.flatten(input, start_dim=0, end_dim=-1)





# zeros

```
>>> import torch
>>> torch.zeros(3)
tensor([0., 0., 0.])
>>> torch.zeros(3,1)
tensor([[0.],
        [0.],
        [0.]])
>>> torch.zeros(3,1,2)
tensor([[[0., 0.]],

        [[0., 0.]],

        [[0., 0.]]])
```

# unsqueeze()

```
import torch

x = torch.zeros(2,3,4)
y = x.unsqueeze(2) # adds singleton dimension at dim=2

print(x, x.shape)
print(y, y.shape)


tensor([[[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]],

        [[0., 0., 0., 0.],
         [0., 0., 0., 0.],
         [0., 0., 0., 0.]]]) torch.Size([2, 3, 4])
tensor([[[[0., 0., 0., 0.]],

         [[0., 0., 0., 0.]],

         [[0., 0., 0., 0.]]],


        [[[0., 0., 0., 0.]],

         [[0., 0., 0., 0.]],

         [[0., 0., 0., 0.]]]]) torch.Size([2, 3, 1, 4])
```



# squeeze()

tensor.squeeze(dimension) removes a dimension from the tensor if and only if that dimension size is equal to 1

squeeze() without a parameter removes all singleton dimensions (size 1).

```
>>> import torch
>>> a = torch.zeros(1,5,10)
>>> a
tensor([[[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]])
>>> a.squeeze(0)
tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
>>> a
tensor([[[0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
         [0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]])
>>> b = a.squeeze(0)
>>> b.shape
torch.Size([5, 10])
>>> a.shape
torch.Size([1, 5, 10])
```

e.g. torch.zeros(3,1,4).squeeze(1) removes the singleton dimension 1 from tensor

# tensor.requires_grad_()

turns on tensor.requires_grad_() in place

```
import torch
a = torch.tensor([1,2,3], dtype=torch.float64)
print(a.requires_grad)
print(a.requires_grad_())
print(a.requires_grad)
```

# broadcasting

B is added to both rows of A

```python 
import torch

a = torch.tensor([[1,2],[3,4]])
b = torch.tensor([4,5])

print(a)
print(b)
print(a + b)
```

# torch.tensor.squeeze(dim=None) and torch.tensor.unsqueeze()

tensors use squeeze() to remove dimensions of size 1

# torch.tensor.flatten()

flatten specializes in flattening data into a 1D tensor

tensor.flatten(1,2) flattens dimensions 1 and 2 (0-indexed) of tensor a into a single dimension,


# torch.tensor.view()

attempts to reshape the tensor without copying data

it requires the data to be contiguous

data size must be compatible with view dimensions, otherwise 

```python
>>> a
tensor([[[1, 2],
         [3, 4]],

        [[5, 6],
         [7, 8]]])
>>> a.view(4,2)
tensor([[1, 2],
        [3, 4],
        [5, 6],
        [7, 8]])
>>> a.view(2,4)
tensor([[1, 2, 3, 4],
        [5, 6, 7, 8]])
```

```python
import torch

a = torch.zeros(12)
b = a.view(3,-1,2) # infers automatically for dim=1

print(a, a.shape)
print(b, b.shape)
```


# reshape()

reshape is similar to view but it creates a clone silently if data is not continuous or incompatible

| Aspect          | `view()`                          | `reshape()`                       |
|-----------------|-----------------------------------|-----------------------------------|
| Memory sharing | Always view, no copy             | View if possible, else copy
| Contiguity     | Must be contiguous               | Handles non-contiguous  
| Error handling | Fails on incompatibility         | Never fails 
| Predictability | Strict, known view               | Unpredictable (view or copy)  

# torch dimensions

scalar: torch.tensor([]) -> dimension 0 (length 0)
1d tensor: torch.tensor([5]) -> dimension 0 (length 1)
2d tensor: torch.tensor([3,4])  -> dimension 0 (length 2)
2d matrix: torch.tensor([[1,2],[3,4]]) -> dimension 0 (length 2), dimension 1 (length 2)

```
>>> a = torch.tensor([[1,2],[3,4]])
>>> a
tensor([[1, 2],
        [3, 4]])
>>> a.shape
torch.Size([2, 2])
>>> a = torch.tensor([[[1,2],[3,4]],[[5,6],[7,8]]])
>>> a.shape
torch.Size([2, 2, 2])
>>> a.shape[0]
2
>>> a.shape[2]
2
```

# torch.randn()

picks outputs from a normal distribution (mean = 0, stdev = 1)

```python
import torch

x = torch.randn(1, 100)
print(x)

print(torch.mean(x)) # will be very close to zero
print(torch.std(x)) # will be very close to one
```

# optim.SGD vs optim.Adam

SGD uses a simple fixed learning rate to adjust weights based on gradient

adam adapts learning rate per parameter using momentum and variance estimates for faster

# `@` operator

does matrix multiplication in pytorch

# model.eval()

sets pytorch model to eval mode

in eval mode, some layers like dropout and batchNorm behavior changes for consistent inference results

randomness is disabled

model.train() sets model back to training mode

# CIFAR 10

dataset of 32x32 RGB images

there are 3 channels (red, blue, green)

10 possible categories

# channels

data that stores info about the color of each pixel in an image

for a 4x4 RGB image

R | G | B | pos
-------------
255 | 0 | 0 | (0,1)


# CNN

since making an MLP based simple linear NN is too costly for larger images due to the huge amounts of neurons required, we use a CNN

a CNN runs a computation over a square group of adjacent pixels and returns one single value for the whole group called a feature

this computation zone is slid across the image in strides

example, for a 32x32 image, we could run a kernel of size 2x2 and slide it across the whole image (skipping 2 pixels at a time as the stride). then we get a resultant feature map of 16x16

this is the formula

output = 1+((input-kernel_size)/stride)

then we run the kernel again on the 16x16 resultant and repeat the process 

we use a technique called downsampling to reduce dimensionality (e.g. by taking the max value of a feature map) until we have data we can flatten into N output neurons representing number of classification targets. this is called pooling

we often add a border of zero pixels around the image in case it does not fit cleanly into the mould

therefore output = 1+((input-kernel_size+(2*padding))/stride)

we apply a neuron activation function like relu to ensure the NN can learn nonlinear patterns

the sequence goes like this : convolutional layer -> activation -> downsampling -> repeat

the final downsampled data is handled by a linear MLP based layer to return the final classified target


# nn.Conv2d(in_channels, out_channels, kernel_size, stride, padding)

in_channels = number of channels in input image (3 for CIFAR since it is RGB)
out_channels = number of feature maps the layer can output (e.g. 32)
kernel_size = size of feature map (e.g. 3x3 i.e. (3,3))
stride = how far feature map moves at each step

# torch.rand() vs torch.randn()

rand = uniform distribution

randn = normal distribution

# tensor.item()

gives the numerical value of a tensor

works only if there is 1 value in the tensor

# torch.randint(start, end, size)

torch.randint

# mean squared error 

MSE = (summation(i=0->n)((y_real_i - y_pred_i)^2))/n

MSE is always non negative

lower MSE denotes better fit

zero MSE denotes perfect fit

# RMSE

RMSE = sqrt(MSE)

more interpretable as it matches data's units

less sensitive to outliers than MSE


