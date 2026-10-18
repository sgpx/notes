import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import transforms
import os
import shutil

# Import model and dataset from ex239_train.py
from ex239_train import DogClassifierCNN, DogClassifierDataset

# Check for device
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Using device for training/loading: {device}")

# Config
data_dir = "ex239_data"
pth_path = "ex239_dog_classifier.pth"
onnx_path = "ex239_dog_classifier.onnx"
parent_onnx_path = os.path.join("..", onnx_path)
input_shape = (1, 3, 320, 320)  # Standard size of PNGs in this dataset

# Initialize model
model = DogClassifierCNN().to(device)

# Load state dict if exists, otherwise train for 1 epoch
if os.path.exists(pth_path):
    print(f"Found existing checkpoint '{pth_path}'. Loading state dict...")
    model.load_state_dict(torch.load(pth_path, map_location=device))
else:
    print(f"Checkpoint '{pth_path}' not found. Training model for 1 epoch to generate it...")
    
    # Transforms
    train_transform = transforms.Compose([
        transforms.RandomHorizontalFlip(p=0.5),
        transforms.RandomRotation(15),
        transforms.ColorJitter(brightness=0.2, contrast=0.2),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    
    # Dataset and DataLoader
    dataset = DogClassifierDataset(data_dir, transform=train_transform)
    dataloader = DataLoader(dataset, batch_size=32, shuffle=True, num_workers=0)
    
    # Loss & Optimizer
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=0.001)
    
    # Training Loop
    model.train()
    total_loss = 0.0
    correct = 0
    total = 0
    
    for batch_idx, (images, labels) in enumerate(dataloader):
        images = images.to(device)
        labels = labels.float().unsqueeze(1).to(device)
        
        # Forward pass
        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        
        # Backward pass
        loss.backward()
        optimizer.step()
        
        # Statistics
        total_loss += loss.item()
        # Since outputs are logits, threshold at 0 for sigmoid-based prediction (> 0.5 prob is > 0 logit)
        predictions = (outputs > 0.0).float()
        correct += (predictions == labels).sum().item()
        total += labels.size(0)
        
        if (batch_idx + 1) % 10 == 0:
            print(f"Batch [{batch_idx+1}/{len(dataloader)}] - Loss: {loss.item():.4f}")
            
    avg_loss = total_loss / len(dataloader)
    accuracy = correct / total
    print(f"\nCompleted 1 Epoch - Avg Loss: {avg_loss:.4f}, Accuracy: {accuracy:.4f}\n")
    
    # Save checkpoint
    torch.save(model.state_dict(), pth_path)
    print(f"Model state dict saved to '{pth_path}'")

# Export to ONNX
print("Exporting model to ONNX...")
model.eval()
model_cpu = model.to("cpu")
dummy_input = torch.randn(*input_shape).to("cpu")

try:
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
    )
    print(f"Successfully saved ONNX model to '{onnx_path}'")
    
    # Copy to parent directory
    try:
        shutil.copy2(onnx_path, parent_onnx_path)
        print(f"Copied '{onnx_path}' to '{parent_onnx_path}'")
    except Exception as e:
        print(f"Saved locally, but skipped copying to '{parent_onnx_path}': {e}")
        
except Exception as e:
    print(f"ONNX export failed: {e}")
