"""
id,exercise_name,topic,subject,chapter_number,chapter
3,Visualize linear transformations on a 2D basis,Linear maps,Math Foundations,1,Linear Algebra

# Problem 3: Visualize Linear Transformations on a 2D Basis

## Objective

Create a visualization system that demonstrates how 2×2 transformation matrices reshape the 2D coordinate system by tracking the movement of basis vectors and the underlying grid.

## Background

A **linear transformation** in 2D can be represented by a 2×2 matrix. The columns of this matrix encode critical information: they represent where the standard basis vectors **e₁ = [1, 0]** and **e₂ = [0, 1]** are mapped after transformation.

For a transformation matrix **M**:
```
M = [[a, b],
     [c, d]]
```

- The first column **[a, c]** is where e₁ lands: **M · e₁**
- The second column **[b, d]** is where e₂ lands: **M · e₂**

This simple fact allows us to understand *any* linear transformation: if we know where the basis vectors go, we know where every other vector goes (by linearity).

## Requirements

### Part 1: Core Implementation

1. **Create a `LinearTransformation` class** that:
   - Accepts a 2×2 matrix in its constructor
   - Has a method to apply the transformation to any 2D vector
   - Validates that the matrix is 2×2

2. **Implement visualization that shows**:
   - **Original state**: The standard basis vectors e₁ (red) and e₂ (blue) as arrows from the origin
   - **Transformed state**: The same basis vectors after applying the transformation matrix
   - **Side-by-side comparison**: Original on the left, transformed on the right
   - **Grid overlay** (optional but encouraged): Show how a regular grid of points transforms under the matrix

3. **Display information**:
   - The transformation matrix values
   - Labels for basis vectors in both states
   - Consistent axis ranges and aspect ratios for meaningful comparison

### Part 2: Test Cases

Create visualizations for at least **four different transformation types**:

1. **Rotation**: A matrix that rotates vectors by 45° (or another angle)
   - Example: rotation by θ degrees uses the form `[[cos(θ), -sin(θ)], [sin(θ), cos(θ)]]`

2. **Scaling**: A matrix that stretches or shrinks vectors along each axis differently
   - Example: `[[2, 0], [0, 0.5]]` (stretch x by 2, compress y by half)

3. **Shearing**: A matrix that tilts one axis while keeping the other fixed
   - Example: `[[1, 0.5], [0, 1]]` (shear along x-axis)

4. **Singular transformation**: A matrix with determinant = 0 that collapses the space
   - Example: `[[1, 2], [2, 4]]` (all vectors map to a line)

### Part 3: Analysis (Conceptual)

For each test case, your code or comments should explain:

- **What happens to the basis vectors?** Do they rotate, stretch, flip, or collapse?
- **What does the determinant tell us?** (It's the scaling factor for area)
- **Is the transformation invertible?** (Can we undo it?)
- **What geometric property is preserved or changed?** (Angles? Lengths? Area?)

## Constraints & Design Notes

- Use pure Python with NumPy for matrix operations and Matplotlib for visualization
- Each transformation should be clearly labeled with its matrix and type
- Basis vectors should be distinguished by color and label (e₁ vs. e₂)
- Code should be modular and reusable—you should be able to pass any 2×2 matrix and get a visualization

## Expected Output

Running your code should produce clear, side-by-side visualizations where you can immediately see:
- How the red arrow (e₁) moves
- How the blue arrow (e₂) moves
- Whether the space gets stretched, rotated, sheared, or collapsed
- The transformation matrix that produced these changes

## Extensions (Optional)

- Animate the transformation from original to final state
- Visualize how a unit circle transforms into an ellipse
- Show the effect on an arbitrary vector (e.g., [1, 1])
- Display the inverse transformation (if it exists)
- Handle 3D transformations (advanced)

---

This problem teaches you the **geometric intuition** behind linear algebra: that matrices aren't just numbers, but *visual deformations of space itself*.
"""


