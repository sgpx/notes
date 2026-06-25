import torch


# y = f(u,v,w) = 3*u**3 + 2*v**2 - 5*w + K

device = torch.device("cuda" if torch.cuda.is_available() else ("mps" if torch.mps.is_available() else "cpu"))
#device = "cpu"
print("using", device)

SAMPLE_SIZE = 10000
NUM_EPOCHS = 1000

u = torch.randint(size=(SAMPLE_SIZE,), low=0, high=100, dtype=torch.float32, device=device)
v = torch.randint(size=(SAMPLE_SIZE,), low=0, high=100, dtype=torch.float32, device=device)
w = torch.randint(size=(SAMPLE_SIZE,), low=0, high=100, dtype=torch.float32, device=device)

K = 15

y_true = (3*u**3) + (2*v**2) - (5*w) + K

class FNN(torch.nn.Module):
	def __init__(self):
		super().__init__()
		self.fc1 = torch.nn.Linear(3,256)
		self.fc2 = torch.nn.Linear(256,200)
		self.fc3 = torch.nn.Linear(200,128)
		self.fc4 = torch.nn.Linear(128,1)
		self.LeakyReLU = torch.nn.LeakyReLU()

	def forward(self, x):
		x = self.fc1(x)
		x = self.LeakyReLU(x)
		x = self.fc2(x)
		x = self.LeakyReLU(x)
		x = self.fc3(x)
		x = self.LeakyReLU(x)
		x = self.fc4(x)
		return x


X_true = torch.vstack([u,v,w]).T
X = X_true
X_mean = X.mean(0, keepdim=True)
X_std = X.std(0, keepdim=True) + 1e-8
Xn = (X - X_mean)/X_std


y = y_true
y_mean = y_true.mean(0, keepdim=True)
y_std = y_true.std(0, keepdim=True) + 1e-8
yn = (y - y_mean)/y_std

model = FNN().to(device)
mse = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

for epoch in range(NUM_EPOCHS):
	y_pred = model(Xn).squeeze()
	optimizer.zero_grad()
	loss = mse(yn.squeeze(), y_pred.squeeze())
	print(epoch, "loss", loss)
	loss.backward()
	optimizer.step()

model.eval()


PRED_SAMPLE_SIZE = 2

u2 = torch.randint(low=0, high=100, size=(PRED_SAMPLE_SIZE,), dtype=torch.float32, device=device)
v2 = torch.randint(low=0, high=100, size=(PRED_SAMPLE_SIZE,), dtype=torch.float32, device=device)
w2 = torch.randint(low=0, high=100, size=(PRED_SAMPLE_SIZE,), dtype=torch.float32, device=device)

X_new = torch.vstack([u2, v2, w2]).T  # (N, 3)
print("X_new", X_new)

X_new_norm = (X_new - X_mean) / X_std
print("X_new_norm", X_new_norm)

with torch.no_grad():
    y_pred_norm = model(X_new_norm).squeeze()

# 2. Rescale the output back to the original range
y_pred_denorm = (y_pred_norm * y_std) + y_mean

# 3. Now compare
y_true = (3*u2**3) + (2*v2**2) - (5*w2) + K

print("y_true", y_true)
print("y_pred_denorm", y_pred_denorm)
exit(0)
err = y_pred_denorm - y_true
max_abs_err = err.abs().max().item()
mse_err = torch.mean(err**2).item()

print("max_abs_err:", max_abs_err, "mse_err:", mse_err)
