# derive the sigmoid derivative sigma'(x) = sigma(x)(1-sigma(x)) from first principles.

f(x) = sigma(x) = 1/(1+e^-x)

df/dx = -((1+e^-x)^-2)*(-e^-x)

= e^-x/(1+e^-x)^2

= [ (1+e^-x) - 1 ] / (1+e^-x)^2

= 1/(1+e^-x) - 1/(1+e^-x)^2

= f(x) - f(x)^2

= f(x) * [1 - f(x)]

= sigma(x) * (1 - sigma(x))
