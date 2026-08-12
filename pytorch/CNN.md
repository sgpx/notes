# CNN

# kernel

a NxN grid filter that passes N pixels of a square grid to the neural network layer to get a singular output O for a matrix of KxK with padding=P (the number of pixels skipped at the ends)

the kernel strides (walks across) the whole KxK matrix and returns MxM outputs

where M = 1 + { (K-N+2P)/S }

0 1 2 3 4 5
- - - - - -

- - -
  - - - 
    - - -
      - - -

input=6, grid=3, stride=1, fmap=4
input=5, grid=3, stride=1, fmap=3
input=4, grid=3, stride=1, fmap=2
input=6, grid=3, stride=2, fmap=2

where stride=1

# feature map

if a KxK matrix has a MxM output after the kernel, the result is called a feature map

# max pool 2d

takes the max value from a NxN grid to perform downsampling or feature reduction to reduce the computational load on the neural network


