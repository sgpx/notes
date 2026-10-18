# Domain: Computer Vision / Core Neural Architecture

## Task
Build and train a Deep Convolutional Neural Network from scratch to classify the CIFAR-10 dataset.

---

## Why this is the next step
The current repository relies entirely on `nn.Linear` layers (fully connected). While effective for simple vectors, these layers fail to capture spatial hierarchies in data.  
This project introduces:
- 2D Convolutions
- Pooling
- Normalization

---

## Project Specifications (Requirements)

To justify the complexity and reward, the solution must meet the following **strict technical requirements**:

### 1. Data Pipeline & Augmentation
- Do **not** use the Iris dataset or dummy data (as seen in `ex30.py` and `ex35.py`).  
- Use **CIFAR-10** (10 classes, RGB images).
  
**Implement Data Augmentation using `torchvision.transforms`. Include:**
- `RandomHorizontalFlip`
- `RandomCrop` (with padding)
- `Normalize` (using CIFAR-10 mean and std)

### 2. Custom Model Architecture (`nn.Module`)
- You **cannot** use a pre-trained model (like ResNet18).  
- Define a class `CIFARNet(nn.Module)`.

**Architecture Requirements:**
- Include **at least 3 Convolutional Blocks**.
- **Block Structure**:
  - `nn.Conv2d` (Convolution)
  - `nn.BatchNorm2d` (Batch Normalization — a new concept not in the original repo)
  - `nn.ReLU` (Activation)
  - `nn.MaxPool2d` (Downsampling)
- The **final layers** must be fully connected (`nn.Linear`) with `nn.Dropout` to prevent overfitting.

### 3. Advanced Training Loop
- Use **SGD with Momentum** (not just vanilla SGD as in `ex30.py`).
- Implement **a Learning Rate Scheduler** (e.g., `torch.optim.lr_scheduler.StepLR` or `ReduceLROnPlateau`) to decay the learning rate during training.
- The script must **track** both:
  - **Training Loss**
  - **Validation Accuracy** (per epoch)
- **Save the Best Model**:
  - Implement logic to save the model state (`.pth`) **only when validation accuracy improves**.