# kullback leibler divergence

for any discrete random variable x being predicted,

let P(x) be the actual values probability distribution

and Q(x) be the expected values probability distribution

D_KL(P || Q) = summation(x=x_1 -> x_n)(P(x) * log_2(P(x)/Q(x))

using log_2 gives bits

using log_e gives nats

D_KL is always greater than or equal to zero

# example

if P = (0.7, 0.3)

Q = (0.6, 0.4)

D_KL = 0.7*log_2(0.7/0.6) + 0.3*log_2(0.3/0.4)

D_KL = 0.7*0.22 + 0.3*(-0.41)

D_KL = 0.154 + - 0.123

D_KL = 0.031

since P != Q, D_KL > 0
