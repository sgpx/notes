import torch

x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
learning_rate = 0.1

for i in range(3):
    # 1. Build the graph
    y = x.pow(2) + 3*x
    loss = y.sum()
    
    # 2. Calculate gradients
    loss.backward()
    print(f"Iteration {i} | x: {x.data} | grad: {x.grad}")
    
    # 3. Update x manually (using torch.no_grad so we don't track the update itself)
    with torch.no_grad():
        x -= learning_rate * x.grad
        
    # 4. Clear gradients for the next round
    x.grad.zero_()
