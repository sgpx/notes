# L1 norm

L1 norm is also known as the taxicab norm or the manhattan distance

for a vector A = 2i+3j, L1_norm(A) = |2| + |3| = 5

L1 norm is the sum of the cofficients of every directional component of a vector

# problem

Here is a challenging problem that combines the L1 norm with concepts from optimization, geometry, and piecewise linear equations.

THE PROBLEM: THE “TAXICAB LOGISTICS” OPTIMIZATION

A logistics drone needs to find a central charging pad location, represented by the coordinates (x, y) in a city layout. There are three delivery hubs at these coordinates:

- Hub A: (1, 5)
- Hub B: (4, 2)
- Hub C: (8, 10)

The drone only flies along a grid layout, so the distance from the charging pad to any hub is determined by the L1 norm of their displacement vector.

Let the displacement vectors from the charging pad to each hub be:

v_A = (x - 1)i-hat + (y - 5)j-hat  
v_B = (x - 4)i-hat + (y - 2)j-hat  
v_C = (x - 8)i-hat + (y - 10)j-hat

YOUR TASK:

Find the optimal coordinates (x, y) for the charging pad that minimize the sum of the L1 norms of all three displacement vectors. In other words, minimize the function:

F(x, y) = ||v_A||_1 + ||v_B||_1 + ||v_C||_1

What are the optimal coordinates (x, y), and what is the minimum total L1 distance?

HINT:

Because the L1 norm splits into independent x and y components:

||v||_1 = |x - x_hub| + |y - y_hub|

You can separate this problem into two independent one-dimensional problems: one minimizing the absolute errors for x, and one for y. Consider what statistical property—mean, median, or mode—minimizes the sum of absolute deviations.

v_A = |x - 1| + |y - 5| = x + y - 6

v_B = |x - 4| + |y - 2| = x + y - 6

v_C = |x - 8| + |y - 10| = x + y - 18


F(x,y) = 3x + 3y - 30 = 3(x+y-10)

let's say x+y-10 = 0 as distance cannot be negative

x+y = 10

(x,y) can be (5,5)
