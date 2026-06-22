import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, Dataset
from torchvision import transforms
from PIL import Image
import glob
import os

# Check for cuda availability
device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.mps.is_available() else "cpu")
print(f"Using device: {device}")

# ============================================================================
# DATASET CLASS
# ============================================================================

class DogClassifierDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.transform = transform
        self.images = []
        self.labels = []
        
        # Load dog images (label = 1)
        dog_images = glob.glob(os.path.join(root_dir, "dog-*.png"))
        for img_path in dog_images:
            self.images.append(img_path)
            self.labels.append(1)
        
        # Load non-dog images (label = 0)
        non_dog_images = glob.glob(os.path.join(root_dir, "non-*.png"))
        for img_path in non_dog_images:
            self.images.append(img_path)
            self.labels.append(0)
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        img_path = self.images[idx]
        label = self.labels[idx]
        
        # Load image
        image = Image.open(img_path).convert('RGB')
        
        if self.transform:
            image = self.transform(image)
        
        return image, label

# ============================================================================
# CNN MODEL
# ============================================================================

class DogClassifierCNN(nn.Module):
    def __init__(self):
        super(DogClassifierCNN, self).__init__()
        
        # Block 1
        self.conv1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.bn1 = nn.BatchNorm2d(32)
        self.relu1 = nn.ReLU(inplace=True)
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # Block 2
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.bn2 = nn.BatchNorm2d(64)
        self.relu2 = nn.ReLU(inplace=True)
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # Block 3
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.bn3 = nn.BatchNorm2d(128)
        self.relu3 = nn.ReLU(inplace=True)
        self.pool3 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # Block 4
        self.conv4 = nn.Conv2d(128, 256, kernel_size=3, padding=1)
        self.bn4 = nn.BatchNorm2d(256)
        self.relu4 = nn.ReLU(inplace=True)
        self.pool4 = nn.MaxPool2d(kernel_size=2, stride=2)
        
        # Adaptive pooling to handle any input size
        self.adaptive_pool = nn.AdaptiveAvgPool2d((1, 1))
        
        # Fully connected layers
        self.fc1 = nn.Linear(256, 128)
        self.dropout1 = nn.Dropout(0.5)
        self.fc2 = nn.Linear(128, 64)
        self.dropout2 = nn.Dropout(0.5)
        self.fc3 = nn.Linear(64, 1)
        
    def forward(self, x):
        # Block 1
        x = self.conv1(x)
        x = self.bn1(x)
        x = self.relu1(x)
        x = self.pool1(x)
        
        # Block 2
        x = self.conv2(x)
        x = self.bn2(x)
        x = self.relu2(x)
        x = self.pool2(x)
        
        # Block 3
        x = self.conv3(x)
        x = self.bn3(x)
        x = self.relu3(x)
        x = self.pool3(x)
        
        # Block 4
        x = self.conv4(x)
        x = self.bn4(x)
        x = self.relu4(x)
        x = self.pool4(x)
        
        # Global average pooling
        x = self.adaptive_pool(x)
        x = x.view(x.size(0), -1)
        
        # Fully connected layers
        x = self.fc1(x)
        x = self.dropout1(x)
        x = self.fc2(x)
        x = self.dropout2(x)
        x = self.fc3(x)
        
        return x

# ============================================================================
# TRAINING SETUP
# ============================================================================

def train_model(data_dir, num_epochs=20, batch_size=32, learning_rate=0.001):
    """Train the dog classifier model."""
    
    # Data augmentation and normalization
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
    
    val_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    
    # Create dataset and dataloader
    dataset = DogClassifierDataset(data_dir, transform=train_transform)
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=0)
    
    print(f"Total images: {len(dataset)}")
    print(f"Dog images: {sum(dataset.labels)}")
    print(f"Non-dog images: {len(dataset.labels) - sum(dataset.labels)}")
    
    # Initialize model
    model = DogClassifierCNN().to(device)
    
    # Loss function and optimizer
    criterion = nn.BCEWithLogitsLoss()
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    scheduler = optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='min', factor=0.5, patience=3
    )
    
    # Training loop
    model.train()
    for epoch in range(num_epochs):
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
            predictions = (outputs > 0.5).float()
            correct += (predictions == labels).sum().item()
            total += labels.size(0)
            
            if (batch_idx + 1) % 10 == 0:
                print(f"Epoch [{epoch+1}/{num_epochs}], Batch [{batch_idx+1}], "
                      f"Loss: {loss.item():.4f}")
        
        # End of epoch statistics
        avg_loss = total_loss / len(dataloader)
        accuracy = correct / total
        print(f"\nEpoch [{epoch+1}/{num_epochs}] - Avg Loss: {avg_loss:.4f}, "
              f"Accuracy: {accuracy:.4f}\n")
        
        scheduler.step(avg_loss)
    
    return model

# ============================================================================
# INFERENCE
# ============================================================================

def predict_image(model, image_path, device=device):
    """Predict if an image contains a dog."""
    
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])
    
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)
    
    model.eval()
    with torch.no_grad():
        output = model(image)
        probability = torch.sigmoid(output).item()
    
    is_dog = probability > 0.5
    return is_dog, probability

# ============================================================================
# USAGE EXAMPLE
# ============================================================================

if __name__ == "__main__":
    # Train the model
    data_dir = "ex239_data"
    model = train_model(data_dir, num_epochs=20, batch_size=32, learning_rate=0.001)
    
    # Save the model
    torch.save(model.state_dict(), "dog_classifier.pth")
    print("Model saved as dog_classifier.pth")
    
    # Test on a sample image
    # test_image_path = "ex239_data/dog-sample.png"
    # is_dog, probability = predict_image(model, test_image_path)
    # print(f"Is dog: {is_dog}, Probability: {probability:.4f}")
