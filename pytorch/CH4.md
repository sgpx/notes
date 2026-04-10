Here are 100 practice problems designed to build muscle memory for PyTorch dimension manipulation. I have categorized them by operation type.

**Instructions:**

* Assume `import torch` has been run.
* Assume `x` is the input tensor defined in the problem.
* Determine the **shape** of the resulting tensor after the operation.

---

### Part 1: Squeeze & Unsqueeze

*Focus: Removing and adding dimensions of size 1.*

1. ~~`x = torch.zeros(1, 5, 10)`; Result of `x.squeeze(0)`?~~
2. ~~`x = torch.zeros(1, 5, 10)`; Result of `x.squeeze()`?~~
3. ~~`x = torch.zeros(3, 1, 4)`; Result of `x.squeeze(1)`?~~
4. ~~`x = torch.zeros(1, 1, 5)`; Result of `x.squeeze()`?~~
5. ~~`x = torch.zeros(10, 1)`; Result of `x.squeeze(0)`? (Trick question: does dim 0 have size 1?)~~
6. ~~`x = torch.zeros(5, 5)`; Result of `x.unsqueeze(0)`?~~
7. ~~`x = torch.zeros(5, 5)`; Result of `x.unsqueeze(1)`?~~
8. ~~`x = torch.zeros(5, 5)`; Result of `x.unsqueeze(-1)`?~~
9. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.unsqueeze(2)`?~~
10. ~~`x = torch.zeros(1, 2, 1, 3)`; Result of `x.squeeze()`?~~
11. ~~`x = torch.zeros(1, 2, 1, 3)`; Result of `x.squeeze(0)`?~~
12. ~~`x = torch.zeros(1, 2, 1, 3)`; Result of `x.squeeze(2)`?~~
13. ~~`x = torch.zeros(7)`; Result of `x.unsqueeze(0)`?~~
14. ~~`x = torch.zeros(7)`; Result of `x.unsqueeze(1)`?~~
15. ~~`x = torch.zeros(3, 1, 2)`; Result of `x.squeeze(2)`? (Can you squeeze a dim of size 2?)~~
16. ~~`x = torch.zeros(1)`; Result of `x.squeeze()`?~~
17. ~~`x = torch.zeros(1)`; Result of `x.unsqueeze(0)`?~~
18. ~~`x = torch.zeros(4, 4, 1)`; Result of `x.squeeze(-1)`?~~
19. ~~`x = torch.zeros(2, 2)`; Result of `x.unsqueeze(0).unsqueeze(0)`?~~
20. ~~`x = torch.zeros(1, 1, 1, 1)`; Result of `x.squeeze()`?~~

### Part 2: View & Reshape

*Focus: Changing the shape while preserving the total number of elements.*

21. ~~`x = torch.zeros(4, 5)`; Result of `x.view(20)`?~~
22. ~~`x = torch.zeros(4, 5)`; Result of `x.view(2, 10)`?~~
23. ~~`x = torch.zeros(4, 5)`; Result of `x.view(5, 4)`?~~
24. ~~`x = torch.zeros(4, 5)`; Result of `x.view(-1)`?~~
25. ~~`x = torch.zeros(4, 5)`; Result of `x.view(2, -1)`?~~
26. ~~`x = torch.zeros(4, 5)`; Result of `x.view(-1, 2)`?~~
27. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.view(6, 4)`?~~
28. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.view(2, 12)`?~~
29. ~~`x = torch.zeros(1, 10)`; Result of `x.view(10)`?~~
30. ~~`x = torch.zeros(1, 10)`; Result of `x.view(10, 1)`?~~
31. ~~`x = torch.zeros(2, 2, 2)`; Result of `x.view(8)`?~~
32. ~~`x = torch.zeros(10, 2)`; Result of `x.view(5, 4)`?~~
33. ~~`x = torch.zeros(12)`; Result of `x.view(3, 2, 2)`?~~
34. ~~`x = torch.zeros(12)`; Result of `x.view(3, -1, 2)`?~~
35. ~~`x = torch.zeros(100)`; Result of `x.view(1, 10, 10)`?~~
36. ~~`x = torch.zeros(100)`; Result of `x.view(10, 1, 10)`?~~
37. ~~`x = torch.zeros(3, 20)`; Result of `x.view(3, 4, 5)`?~~
38. ~~`x = torch.zeros(2, 5)`; Result of `x.reshape(5, 2)`?~~
39. ~~`x = torch.zeros(2, 5)`; Result of `x.reshape(10)`?~~
40. ~~`x = torch.zeros(1, 1)`; Result of `x.view(1)`?~~

### Part 3: Flatten

*Focus: Collapsing dimensions into a single dimension (often for fully connected layers).*

41. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.flatten()`?~~
42. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.flatten(start_dim=0)`?~~
43. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.flatten(start_dim=1)`?~~
44. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.flatten(start_dim=2)`?~~
45. ~~`x = torch.zeros(10, 3, 28, 28)`; Result of `x.flatten(start_dim=1)`? (Common CNN pattern)~~
46. ~~`x = torch.zeros(5, 1, 1)`; Result of `x.flatten()`?~~
47. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.flatten(0, 1)`? (Flatten dims 0 and 1 only)~~
48. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.flatten(1, 2)`?~~
49. ~~`x = torch.zeros(1, 10)`; Result of `x.flatten()`?~~
50. ~~`x = torch.zeros(8, 8, 3)`; Result of `x.flatten(0, -1)`?~~
51. ~~`x = torch.zeros(2, 2, 2, 2)`; Result of `x.flatten(2, 3)`?~~
52. ~~`x = torch.zeros(2, 2, 2, 2)`; Result of `x.flatten(0, 2)`?~~
53. ~~`x = torch.zeros(5)`; Result of `x.flatten()`?~~
54. ~~`x = torch.zeros(1, 5)`; Result of `x.flatten(0)`?~~
55. ~~`x = torch.zeros(3, 1, 3)`; Result of `x.flatten(1)`?~~
56. ~~`x = torch.zeros(10, 20, 30)`; Result of `x.flatten(start_dim=0, end_dim=1)`?~~
57. ~~`x = torch.zeros(10, 20, 30)`; Result of `x.flatten(start_dim=1, end_dim=2)`?~~
58. ~~`x = torch.zeros(2, 3, 4, 5)`; Result of `x.flatten(1, -1)`?~~
59. ~~`x = torch.zeros(1, 1, 1)`; Result of `x.flatten()`?~~
60. ~~`x = torch.zeros(6, 4)`; Result of `x.flatten(0, 0)`? (Trick: flattening one dim)~~

### Part 4: Transpose & Permute

*Focus: Swapping dimensions.*

61. ~~`x = torch.zeros(2, 3)`; Result of `x.transpose(0, 1)`?~~
62. ~~`x = torch.zeros(2, 3)`; Result of `x.T`?~~
63. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.transpose(0, 1)`?~~
64. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.transpose(1, 2)`?~~
65. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.permute(0, 2, 1)`?~~
66. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.permute(2, 0, 1)`?~~
67. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.permute(2, 1, 0)`?~~
68. ~~`x = torch.zeros(1, 5, 1)`; Result of `x.transpose(0, 2)`?~~
69. ~~`x = torch.zeros(10, 20, 3)`; Result of `x.permute(0, 2, 1)`?~~
70. ~~`x = torch.zeros(5, 5)`; Result of `x.transpose(1, 0)`?~~
71. ~~`x = torch.zeros(1, 2, 3, 4)`; Result of `x.permute(0, 3, 1, 2)`?~~
72. ~~`x = torch.zeros(2, 3, 4)`; Result of `x.transpose(0, 2)`?~~
73. ~~`x = torch.zeros(1, 2, 1)`; Result of `x.permute(1, 0, 2)`?~~
74. ~~`x = torch.zeros(3, 4, 5)`; Result of `x.permute(0, 1, 2)`?~~
75. ~~`x = torch.zeros(3, 2)`; Result of `x.transpose(-1, -2)`?~~
76. ~~`x = torch.zeros(2, 3, 4, 5)`; Result of `x.transpose(1, 3)`?~~
77. ~~`x = torch.zeros(1, 2, 3)`; Result of `x.permute(2, 0, 1)`?~~
78. ~~`x = torch.zeros(5, 1)`; Result of `x.T`?~~
79. ~~`x = torch.zeros(4, 4)`; Result of `x.permute(1, 0)`?~~
80. ~~`x = torch.zeros(2, 1, 2)`; Result of `x.transpose(0, 1)`?~~

### Part 5: Mixed Bag (Chained Operations)

*Focus: Combining operations, common in real models.*

81. `x = torch.zeros(1, 5, 5)`; Result of `x.squeeze(0).view(25)`?
82. `x = torch.zeros(2, 3, 4)`; Result of `x.permute(0, 2, 1).flatten(1)`?
83. `x = torch.zeros(10, 1, 28, 28)`; Result of `x.squeeze(1).flatten(1)`?
84. `x = torch.zeros(2, 5)`; Result of `x.unsqueeze(1).transpose(0, 1)`?
85. `x = torch.zeros(10)`; Result of `x.view(2, 5).T`?
86. `x = torch.zeros(2, 2, 2)`; Result of `x.view(-1).unsqueeze(0)`?
87. `x = torch.zeros(4, 3)`; Result of `x.view(3, 4).transpose(0, 1)`?
88. `x = torch.zeros(1, 2, 3)`; Result of `x.permute(0, 2, 1).squeeze(0)`?
89. `x = torch.zeros(2, 1, 5)`; Result of `x.expand(2, 3, 5)`? (Broadcasting practice)
90. `x = torch.zeros(10, 3, 32, 32)`; Result of `x.view(10, 3, -1).permute(0, 2, 1)`?
91. `x = torch.zeros(2, 5)`; Result of `x[:, None, :].shape`? (Indexing unsqueeze)
92. `x = torch.zeros(2, 5)`; Result of `x[..., None].shape`?
93. `x = torch.zeros(3, 3)`; Result of `x.view(1, 3, 3).repeat(2, 1, 1)`?
94. `x = torch.zeros(2, 3, 4)`; Result of `x.transpose(1, 2).contiguous().view(2, 12)`?
95. `x = torch.zeros(5)`; Result of `x.unsqueeze(0).unsqueeze(2)`?
96. `x = torch.zeros(1, 10, 1)`; Result of `x.squeeze().view(2, 5)`?
97. `x = torch.zeros(2, 4)`; Result of `x.view(8).view(2, 2, 2)`?
98. `x = torch.zeros(3, 1, 4, 1)`; Result of `x.squeeze().shape`? (Watch out for multiple 1s)
99. `x = torch.zeros(10, 20)`; Result of `x.t().unsqueeze(0)`?
100. `x = torch.zeros(2, 2)`; Result of `torch.cat([x, x], dim=0)`?

---

### Answer Key

1. `(5, 10)`
2. `(5, 10)`
3. `(3, 4)`
4. `(5,)` (Removes all dimensions of size 1)
5. `(10, 1)` (No change; dim 0 size is 10, not 1)
6. `(1, 5, 5)`
7. `(5, 1, 5)`
8. `(5, 5, 1)`
9. `(2, 3, 1, 4)`
10. `(2, 3)` (Removes dim 0 and 2)
11. `(2, 1, 3)`
12. `(1, 2, 3)`
13. `(1, 7)`
14. `(7, 1)`
15. `(3, 1, 2)` (No change; dim 2 has size 2)
16. `()` (Scalar tensor)
17. `(1, 1)`
18. `(4, 4)`
19. `(1, 1, 2, 2)`
20. `()`
21. `(20,)`
22. `(2, 10)`
23. `(5, 4)`
24. `(20,)`
25. `(2, 10)`
26. `(10, 2)`
27. `(6, 4)`
28. `(2, 12)`
29. `(10,)`
30. `(10, 1)`
31. `(8,)`
32. `(5, 4)`
33. `(3, 2, 2)`
34. `(3, 2, 2)` (12 / (3*2) = 2)
35. `(1, 10, 10)`
36. `(10, 1, 10)`
37. `(3, 4, 5)`
38. `(5, 2)`
39. `(10,)`
40. `(1,)`
41. `(24,)`
42. `(24,)`
43. `(2, 12)`
44. `(2, 3, 4)` (No change, starts at last dim)
45. `(10, 2352)` (3 * 28 * 28 = 2352)
46. `(5,)`
47. `(6, 4)`
48. `(2, 12)`
49. `(10,)`
50. `(192,)` (8 * 8 * 3)
51. `(2, 2, 4)`
52. `(8, 2)`
53. `(5,)`
54. `(5,)`
55. `(3, 3)`
56. `(200, 30)`
57. `(10, 600)`
58. `(2, 60)`
59. `(1,)`
60. `(6, 4)` (Flattening from 0 to 0 changes nothing)
61. `(3, 2)`
62. `(3, 2)`
63. `(3, 2, 4)`
64. `(2, 4, 3)`
65. `(2, 4, 3)`
66. `(4, 2, 3)`
67. `(4, 3, 2)`
68. `(1, 5, 1)` (Swapping size 1 and size 1)
69. `(10, 3, 20)`
70. `(5, 5)`
71. `(1, 4, 2, 3)`
72. `(4, 3, 2)`
73. `(2, 1, 1)`
74. `(3, 4, 5)`
75. `(2, 3)`
76. `(2, 5, 4, 3)`
77. `(3, 1, 2)`
78. `(1, 5)`
79. `(4, 4)`
80. `(1, 2, 2)`
81. `(25,)`
82. `(2, 12)` (Permute -> (2, 4, 3) -> Flatten(1) -> (2, 12))
83. `(10, 784)`
84. `(1, 2, 5)` (Unsqueeze(1)->(2,1,5) -> Transpose(0,1)->(1,2,5))
85. `(5, 2)`
86. `(1, 8)`
87. `(4, 3)`
88. `(3, 2)`
89. `(2, 3, 5)` (Copies data along dim 1)
90. `(10, 1024, 3)` (View->(10,3,1024) -> Permute->(10,1024,3))
91. `(2, 1, 5)`
92. `(2, 5, 1)`
93. `(2, 3, 3)`
94. `(2, 12)`
95. `(1, 5, 1)`
96. `(2, 5)`
97. `(2, 2, 2)`
98. `(3, 4)`
99. `(1, 20, 10)`
100. `(4, 2)`

Would you like me to walk through the logic of any of these specifically?
