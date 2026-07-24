# partial derivatives vs ordinary derivatives

---------------------------------------------
partial derivative    | ordinary derivative
---------------------------------------------
two or more variables | has only one variable
f(x,y)                | f(x)
---------------------------------------------
uses the curly d      | uses the standard d
(del)                 |
---------------------------------------------
changes only one var, | changes one variable
the rest are frozen   | 
---------------------------------------------
slope of a curve      | slope of a surface
in 2D                 | along one grid
---------------------------------------------

# examples

z = f(x,y) = x^2 + y^2 + 2xy

del_z/del_x = del_(x^2)/del_x + del_(y^2)/del_x + del_(2xy)/del_x

y is treated as a constant

del_z/del_x = 2x + 0 + 2y = 2x + 2y
