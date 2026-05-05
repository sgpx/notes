import torch

import os
os.chdir("ex181data")
# 1. Redefine the model with a static AvgPool2d to bypass the ONNX down-converter bug
class FNN_Export(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 32, 3, padding=1)
        self.bn1 = torch.nn.BatchNorm2d(32)
        
        self.conv2 = torch.nn.Conv2d(32, 64, 3, padding=1)
        self.bn2 = torch.nn.BatchNorm2d(64)
        
        self.conv3 = torch.nn.Conv2d(64, 4, 3, padding=1)
        self.bn3 = torch.nn.BatchNorm2d(4)
        
        self.pool = torch.nn.MaxPool2d(2, 2)
        self.relu = torch.nn.ReLU(inplace=True)
        
        # FIX: Replaced AdaptiveAvgPool2d with static AvgPool2d(56)
        self.gap = torch.nn.AvgPool2d(56)
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

# 2. Instantiate and load the weights you already trained
model_export = FNN_Export()
model_export.load_state_dict(torch.load("model.pth", map_location="cpu", weights_only=True))
model_export.eval() # Set to evaluation mode!

# 3. Create dummy input locked to batch size 1
dummy_input = torch.randn(1, 3, 224, 224)

# 4. Export cleanly to Opset 14 without dynamic axes
try:
    torch.onnx.export(
        model_export,
        dummy_input,
        "model.onnx",
        export_params=True,
        opset_version=14,  # Stable for web
        do_constant_folding=True,
        input_names=["image"],
        output_names=["output"]
        # dynamic_axes removed: web browsers only process 1 image at a time anyway!
    )
    print("Export successful! You now have a unified model.onnx file.")
except Exception as e:
    print(f"ONNX export failed: {e}")
