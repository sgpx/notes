### Exercise 1: Tensor Creation
- **Objective:** Create a 1D tensor of shape (5,) containing the numbers from 0 to 4.
- **Task:** Use the `torch.arange()` or `torch.tensor()` functions.

### Exercise 2: Basic Tensor Operations
- **Objective:** Perform element-wise addition and multiplication on two tensors.
- **Task:** Create two tensors `a` and `b`, both of shape (3, 3), initialized with values 1 and 2 respectively. Then compute the sum and product of these tensors.

### Exercise 3: Reshaping Tensors
- **Objective:** Reshape a tensor.
- **Task:** Create a tensor of shape (2, 6) filled with random numbers and reshape it to (3, 4). Print both shapes.

### Exercise 4: Basic Statistics
- **Objective:** Compute basic statistics on a tensor.
- **Task:** Create a tensor of shape (10,) with random numbers and compute its mean, median, and standard deviation.

### Exercise 5: Building a Simple Neural Network
- **Objective:** Create a simple feedforward neural network.
- **Task:** Use `torch.nn.Module` to define a network with one input layer, one hidden layer, and one output layer. Use ReLU as the activation function.

### Exercise 6: Forward Pass
- **Objective:** Perform a forward pass through the neural network from Exercise 5.
- **Task:** Create an input tensor of appropriate shape and pass it through the network you created.

### Exercise 7: Loss Calculation
- **Objective:** Compute the loss for a simple task.
- **Task:** Using the output from Exercise 6 and a target tensor (e.g., a one-hot encoded tensor), compute the mean squared error loss using `torch.nn.MSELoss()`.

### Exercise 8: Backpropagation
- **Objective:** Implement backpropagation to update model weights.
- **Task:** Continue from Exercise 7, use the computed loss to perform backpropagation (use `loss.backward()`) and update the model parameters using a simple gradient descent approach.

### Exercise 9: Working with Datasets
- **Objective:** Use a predefined dataset.
- **Task:** Load the MNIST dataset using `torchvision.datasets`. Print the shape of the first image and its corresponding label.

### Exercise 10: DataLoader
- **Objective:** Load data in batches.
- **Task:** Use a `DataLoader` to load the MNIST dataset in batches of 64. Iterate through one batch and print the shape of the images and labels.
