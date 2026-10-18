# Gradient Descent in Pure Python

# Define the cost function J(theta) = theta^2
def cost_function(theta):
    return theta**2

# Define the gradient of the cost function: dJ/dtheta = 2*theta
def gradient(theta):
    return 2 * theta

# Gradient Descent Function
def gradient_descent(starting_theta, learning_rate, num_iterations):
    theta = starting_theta  # Initialize theta
    for i in range(num_iterations):
        grad = gradient(theta)  # Compute gradient
        theta = theta - learning_rate * grad  # Update theta
        cost = cost_function(theta)  # Compute cost
        print(f"Iteration {i+1}: theta = {theta:.4f}, cost = {cost:.4f}")
    return theta

# Parameters
starting_theta = 3.0  # Initial value of theta
learning_rate = 0.1   # Step size (eta)
num_iterations = 5   # Number of iterations

# Run Gradient Descent
final_theta = gradient_descent(starting_theta, learning_rate, num_iterations)

print(f"\nFinal value of theta: {final_theta:.4f}")
