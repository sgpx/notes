"""
Implement and compare vanilla SGD, momentum SGD, RMSProp, and Adam optimizers on a 2‑D quadratic loss function (e.g., (L(\theta)= (x-3)**2 + (y+2)**2)). Track loss values, parameter trajectories, and final parameter locations for each optimizer. Plot the loss curves and contours of the parameter path.
"""

import torch
import torch.nn as nn
import torch.optim as optim
import matplotlib.pyplot as plt

torch.manual_seed(0)

# --- Problem: 2D quadratic loss L(x,y) = (x-3)^2 + (y+2)^2 ---
L = lambda x, y: (x - 3.0)**2 + (y + 2.0)**2

# Make separate parameter tensors for each optimizer (so runs don't interfere)
def make_params():
    # start from the same initial point for fair comparison
    x = torch.nn.Parameter(torch.randn(()))
    y = torch.nn.Parameter(torch.randn(()))
    return x, y

# Create one shared initial point
x_init, y_init = make_params()

# --- Optimizers (match your hyperparams; you can tune if desired) ---
def make_optimizers(x, y):
    opt_sgd  = optim.SGD([x, y], lr=0.1)
    opt_mom  = optim.SGD([x, y], lr=0.05, momentum=0.9)
    opt_rms  = optim.RMSprop([x, y], lr=0.01, alpha=0.99)
    opt_adam = optim.Adam([x, y], lr=0.1)
    return {
        "SGD": opt_sgd,
        "Momentum SGD": opt_mom,
        "RMSProp": opt_rms,
        "Adam": opt_adam
    }

# --- Run an optimizer and track loss/trajectory ---
def run(opt_name, steps=200):
    # reset to shared init
    x = torch.nn.Parameter(x_init.detach().clone())
    y = torch.nn.Parameter(y_init.detach().clone())
    opts = make_optimizers(x, y)
    opt = opts[opt_name]

    losses = []
    traj = []  # store (x,y) over time

    for t in range(steps):
        opt.zero_grad()
        loss = L(x, y)
        loss.backward()
        opt.step()

        losses.append(loss.item())
        traj.append((x.detach().item(), y.detach().item()))

    final = traj[-1]
    return x, y, losses, traj, final

steps = 200
results = {}
for name in ["SGD", "Momentum SGD", "RMSProp", "Adam"]:
    x_f, y_f, losses, traj, final = run(name, steps=steps)
    results[name] = {
        "losses": losses,
        "traj": traj,
        "final": final
    }

# --- Report final parameters ---
print("Initial point: ", (x_init.item(), y_init.item()))
for name, info in results.items():
    xf, yf = info["final"]
    print(f"{name:14s} final (x,y)=({xf:.6f}, {yf:.6f})  final loss={info['losses'][-1]:.6e}")

# --- Prepare grids for contour plot ---
# choose range around initialization and optimum (3, -2)
xs = [x_init.item(), 3.0]
ys = [y_init.item(), -2.0]

xmin, xmax = min(xs) - 2.0, max(xs) + 2.0
ymin, ymax = min(ys) - 2.0, max(ys) + 2.0

grid_x = torch.linspace(xmin, xmax, 200)
grid_y = torch.linspace(ymin, ymax, 200)
X, Y = torch.meshgrid(grid_x, grid_y, indexing="xy")
Z = (X - 3.0)**2 + (Y + 2.0)**2

# --- Plot loss curves ---
plt.figure(figsize=(8, 5))
for name, info in results.items():
    plt.plot(info["losses"], label=name)
plt.yscale("log")
plt.xlabel("Step")
plt.ylabel("Loss (log scale)")
plt.title("Loss curves for different optimizers")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- Plot trajectories on contours ---
plt.figure(figsize=(8, 6))
cont = plt.contour(X.numpy(), Y.numpy(), Z.numpy(), levels=30, cmap="viridis")
plt.colorbar(cont, label="Loss")

# plot each optimizer path
for name, info in results.items():
    traj = info["traj"]
    xs_path = [p[0] for p in traj]
    ys_path = [p[1] for p in traj]
    plt.plot(xs_path, ys_path, linewidth=2, label=name)
    # mark final point
    plt.scatter([xs_path[-1]], [ys_path[-1]], s=40)

# start + optimum
plt.scatter([x_init.item()], [y_init.item()], color="red", s=60, label="Start")
plt.scatter([3.0], [-2.0], color="black", s=60, marker="*", label="Optimum (3,-2)")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Parameter trajectories on loss contours")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- Optional: show final locations in a small table-like printout ---
print("\nFinal locations:")
for name, info in results.items():
    xf, yf = info["final"]
    print(f"{name:14s}: x={xf:.6f}, y={yf:.6f}")
