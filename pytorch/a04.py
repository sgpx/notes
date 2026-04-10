import pandas as pd

# Load data
data = pd.read_csv("a04.csv")
X = data[["X1", "X2", "X3"]]
y = data["Y"]
print(X, y)
# Add intercept term (β₀)
X["Intercept"] = 1

# Initialize coefficients (β₀, β₁, β₂, β₃)
beta = [0, 0, 0, 0]
learning_rate = 0.01
iterations = 20

# Gradient Descent
for _ in range(iterations):
    y_pred = X.dot(beta)
    error = y - y_pred
    gradients = -X.T.dot(error) / len(y)
    beta -= learning_rate * gradients
    print("beta", beta)

print("Final coefficients:", beta)
