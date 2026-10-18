# matrix differentiation

for this program,

import torch
a = torch.tensor([[1,2],[3,4]], requires_grad=True)
b = torch.tensor([[4,5],[6,7]])
c = (a@b).sum()
c.backward()
print(a.grad)

the mathematical interpretation is

a 

=

a11 a12
a21 a22

b 

=

b11 b12
b21 b22

c = a x b

=

(a11*b11)+(a12*b21) (a11*b12)+(a12*b22)
(a21*b11)+(a22*b21) (a21*b12)+(a22*b22)

let c_s = sum(c_ij) = a11*b11 + a12+b21 + ... + a22*b22

when we do dc_s/da, 

`a` is a matrix made of a11, a12, a21, a22 and `c` is a scalar which is a function of all of a11, a12, a21, a22

therefore we must differentiate independently for all elements in a, and the resultant will also be a matrix consisting of `dc_s/da_ij`. since a12, a21, a22 are constant w.r.t. a11 and vice versa, other irreleated terms derivatives will become zero

dc_s/da11 = b11 + b12

dc_s/da12 = b21 + b22

dc_s/da21 = b11 + b12

dc_s/da22 = b21 + b22

therefore

dc_s/da 

=

(b11 + b12) (b21 + b22)
(b11 + b12) (b21 + b22)

=

4+5 6+7
4+5 6+7

=

9 13
9 13
