
import os
import torch

dummy = torch.tensor([1,2,3])
dummy.to("cuda")

Xc = []
yc = []
python_code = []
nonpython_code = []
for i,j,k in os.walk("data"):
    for f in k:
        xpath = os.path.join(i,f)
        # print(xpath)
        ispy = "python" in xpath
        if not (os.path.exists(xpath) and os.path.isfile(xpath)): continue
        try:
            with open(xpath,"r", encoding="utf-8") as fr:
                ydat = fr.read()
            for y2 in range(0, len(ydat), 4096):
                ystr = ydat[y2:y2+4096]
                # print(len(ystr), ispy)
                diff = 4096 - len(ystr)
                ystr += (diff * " ")
                ordarr = torch.tensor([min(ord(c), 255) / 255.0 for c in ystr], device="cuda")
                Xc.append(ordarr)
                yc.append(1 if ispy else 0)
        except:
            pass

X = torch.stack(Xc).to(device="cuda")
y = torch.tensor(yc, device="cuda")


class FNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.relu = torch.nn.ReLU(inplace=True)
        self.fc1 = torch.nn.Linear(4096, 2048)
        self.fc2 = torch.nn.Linear(2048, 1024)
        self.fc3 = torch.nn.Linear(1024, 512)
        self.fc4 = torch.nn.Linear(512, 256)
        self.fc5 = torch.nn.Linear(256, 128)
        self.fc6 = torch.nn.Linear(128, 64)
        self.fc7 = torch.nn.Linear(64, 32)
        self.fc8 = torch.nn.Linear(32, 16)
        self.fc9 = torch.nn.Linear(16, 8)
        self.fc10 = torch.nn.Linear(8, 4)
        self.fc11 = torch.nn.Linear(4, 2)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)

        x = self.fc2(x)
        x = self.relu(x)

        x = self.fc3(x)
        x = self.relu(x)

        x = self.fc4(x)
        x = self.relu(x)

        x = self.fc5(x)
        x = self.relu(x)

        x = self.fc6(x)
        x = self.relu(x)

        x = self.fc7(x)
        x = self.relu(x)

        x = self.fc8(x)
        x = self.relu(x)

        x = self.fc9(x)
        x = self.relu(x)

        x = self.fc10(x)
        x = self.relu(x)

        x = self.fc11(x)

        return x


model = FNN()
model.to(device="cuda")
pos = (y == 1).sum().item()
neg = (y == 0).sum().item()

weight = torch.tensor([
    1.0,
    neg / pos
]).to("cuda")
criterion = torch.nn.CrossEntropyLoss(
    weight=weight
)
optimizer = torch.optim.Adam(model.parameters())

for epoch in range(1000):
    optimizer.zero_grad()
    y_hat = model(X)
    loss = criterion(y_hat, y.long())
    loss.backward()
    optimizer.step()
    print("epoch ", epoch, "loss", loss.item())


# torch.save(model, "model.pth")
torch.save(model.state_dict(), "model.pt")

# after training
scripted_model = torch.jit.script(model)
scripted_model.save("model_scripted.pt")