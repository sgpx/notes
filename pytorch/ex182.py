import torch
import os
import shutil
from torchvision import transforms
from PIL import Image

# Collect image paths and labels
data = []
for i in range(1, 5):
    for j in os.listdir(f"l{i}"):
        img_path = os.path.join(f"l{i}", j)
        data.append((img_path, i - 1))


class mydataclass(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data
        self.transform = transforms.Compose(
            [
                transforms.RandomHorizontalFlip(),  # optional but useful
                transforms.RandomRotation(10),  # optional
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.5] * 3, std=[0.5] * 3),
            ]
        )

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        img_path, label = self.data[index]
        image = Image.open(img_path).convert("RGB")

        # Keep aspect ratio
        image.thumbnail((224, 224), Image.Resampling.LANCZOS)

        # Pad to 224x224
        padded = Image.new("RGB", (224, 224), (255, 255, 255))
        offset = ((224 - image.width) // 2, (224 - image.height) // 2)
        padded.paste(image, offset)

        image = self.transform(padded)
        return image, label


class FNN(torch.nn.Module):
    def __init__(self):
        super().__init__()

        # Better feature extractor
        self.conv1 = torch.nn.Conv2d(3, 32, 3, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(32)

        self.conv2 = torch.nn.Conv2d(32, 64, 3, padding=1)
        self.bn2 = torch.nn.BatchNorm2d(64)

        self.conv3 = torch.nn.Conv2d(64, 4, 3, padding=1)
        self.bn3 = torch.nn.BatchNorm2d(4)

        self.pool = torch.nn.MaxPool2d(2, 2)
        self.relu = torch.nn.ReLU(inplace=True)

        # Efficient head
        self.gap = torch.nn.AdaptiveAvgPool2d((1, 1))
        self.fc = torch.nn.Linear(4, 4)

    def forward(self, x):
        x = self.relu(self.bn1(self.conv1(x)))
        x = self.pool(x)

        x = self.relu(self.bn2(self.conv2(x)))
        x = self.pool(x)

        x = self.relu(self.bn3(self.conv3(x)))

        x = self.gap(x)

        x = torch.flatten(x, start_dim=1)

        x = self.fc(x)
        return x


device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")

dataset = mydataclass(data)
loader = torch.utils.data.DataLoader(dataset, shuffle=True, batch_size=16)

model = FNN().to(device)

# Lower LR for stability
optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)

criterion = torch.nn.CrossEntropyLoss()


NUM_EPOCHS = 1

for epoch in range(NUM_EPOCHS):
    model.train()
    total_loss = 0

    for x_batch, y_batch in loader:
        x_batch = x_batch.to(device)
        y_batch = y_batch.to(device)

        optimizer.zero_grad()
        y_hat = model(x_batch)

        loss = criterion(y_hat, y_batch)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(loader)
    print(f"Epoch {epoch+1:02d} | Avg Loss: {avg_loss:.4f}")


# Save model
torch.save(model.state_dict(), "model.pth")

model.eval()  # Always set to eval mode before exporting!
model_cpu = model.to("cpu")
dummy_input = torch.randn(1, 3, 224, 224).to("cpu")

try:
    onnx_path = "model.onnx"
    onnx_external_data_path = f"{onnx_path}.data"
    parent_onnx_path = os.path.join("..", onnx_path)

    torch.onnx.export(
        model_cpu,
        dummy_input,
        onnx_path,
        export_params=True,
        opset_version=18,
        external_data=False,
        do_constant_folding=True,
        input_names=["image"],
        output_names=["output"]
        # Notice: dynamic_axes has been removed entirely!
    )

    if os.path.exists(onnx_external_data_path):
        os.remove(onnx_external_data_path)

    try:
        shutil.copy2(onnx_path, parent_onnx_path)
        print(f"Copied {onnx_path} to {parent_onnx_path}")
    except PermissionError:
        print(f"Saved {onnx_path} locally (skipped copying to {parent_onnx_path})")

    print("Model saved as model.pth and model.onnx")
except Exception as e:
    print(f"ONNX export failed: {e}")
