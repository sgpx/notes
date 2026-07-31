import dotenv
dotenv.load_dotenv()
import llm
import json
import torch
import torch.nn as nn
import torch.optim as optim

EMB_DIMS = 1536

class SimpleNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(EMB_DIMS, 3000)
        self.fc2 = nn.Linear(3000, 1000)
        self.fc3 = nn.Linear(1000, 100)
        self.fc4 = nn.Linear(100, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = self.relu(x)
        x = self.fc4(x)
        return x

model = SimpleNN().to("mps")
model.load_state_dict(torch.load("model_lv4.pt"))

model.eval()  # Set to evaluation mode

model.cpu()
dummy_input = torch.randn(1, EMB_DIMS, device="cpu")  # CPU input
torch.onnx.export(
    model,
    dummy_input,
    "ex280.onnx",
    export_params=True,
    opset_version=13,
    do_constant_folding=True,
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={
        "input": {0: "batch_size"},
        "output": {0: "batch_size"}
    }
)

print("ONNX model saved to 'ex280.onnx'")
