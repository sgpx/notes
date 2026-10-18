# Moore-Penrose pseudoinverse 

for any MxN matrix A, the moore-penrose pseudoinverse A_pinv is a matrix that has special properties

- A*A_pinv*A = A
- A_pinv*A*A_pinv = A
- (A*A_pinv)^T = A*A_pinv
- A*A_pinv is symmetric
- (A_pinv*A)^T = A_pinv*A
- A_pinv*A is symmetric


A = U*Sigma*V^T

Sigma_R is formed by replacing all non-zero values with their reciprocals in Sigma

A_pinv = V*Sigma_R*U^T

# ----


**Moore-Penrose Pseudoinverse**  
A⁺ is a special matrix that generalizes the idea of an inverse to *any* matrix—even non-square or singular ones. It works when a true inverse doesn’t exist and finds the *best approximate solution* to linear problems.

---

**Core Idea**  
Regular inverses only work for square, non-singular matrices. Pseudoinverses work for:  
- Tall matrices (more rows than columns)  
- Wide matrices (more columns than rows)  
- Singular matrices (no true inverse)  
It is the *only* matrix that behaves as close to an inverse as mathematically possible.

---

**Key Properties**  
A⁺ (the pseudoinverse of A) is the *unique* matrix satisfying **all four** of these:  
1. **AA⁺A = A**  
2. **A⁺AA⁺ = A⁺**  
3. **(AA⁺)ᵀ = AA⁺** (AA⁺ is symmetric)  
4. **(A⁺A)ᵀ = A⁺A** (A⁺A is symmetric)  
These ensure A⁺ acts like a "best-fit" inverse.

---

**How It’s Calculated**  

*For Full-Rank Matrices:*  
- **Tall (m×n, m > n)**: A⁺ = (AᵀA)⁻¹Aᵀ  
- **Wide (m×n, m < n)**: A⁺ = Aᵀ(AAᵀ)⁻¹  

*For Any Matrix (General Case):*  
- Compute **SVD**: A = UΣVᵀ  
- Take reciprocals of **non-zero singular values** in Σ to make Σ⁺  
- Then: **A⁺ = VΣ⁺Uᵀ**  

---

**Practical Uses**  

*Solving Least-Squares Problems*  
- For overdetermined systems (more equations than unknowns): **x = A⁺b** gives the solution with the *smallest error*.  

*Minimum-Norm Solutions*  
- For underdetermined systems (more unknowns than equations): A⁺ picks the solution with the *smallest magnitude*.  

*Fields That Use It*  
- Linear regression (even with correlated predictors)  
- Image deblurring/denoising  
- Control systems design  
- Recommender systems (matrix completion)  

---

**Simple Example**  
Take this 3×2 matrix:  
A = [[1, 0], [1, 1], [1, 2]]  
You can’t solve Ax = b *exactly* for arbitrary b (e.g., [1, 2, 3]ᵀ). But **x = A⁺b** gives the *best approximate solution* in the least-squares sense.  

---

**Why It Matters**  
A⁺ is powerful because it:  
1. **Always exists and is unique** (unlike true inverses)  
2. **Solves problems with no perfect solution**  
3. **Unifies multiple cases**:  
   - Works like an inverse when one exists  
   - Gives least-squares solutions for overdetermined systems  
   - Gives minimum-norm solutions for underdetermined systems  
4. **Avoids failure** in ill-posed or messy real-world data  

It’s a foundational tool for data science, engineering, and anywhere linear systems need solving.  

---  
*This reformatting follows ADHD-friendly principles: short chunks, bullet points, explicit explanations, no LaTeX, and plain text only.*

