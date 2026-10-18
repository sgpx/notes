import copy
import os
import random
import shutil

import torch
from PIL import Image
from torchvision import transforms

NUM_EPOCHS = 100
BATCH_SIZE = 16
VALIDATION_SPLIT = 0.2
NUM_FOLDS = 5
SEED = 42


def build_samples():
    samples = []
    for class_index in range(1, 5):
        class_dir = f"l{class_index}"
        for filename in os.listdir(class_dir):
            image_path = os.path.join(class_dir, filename)
            samples.append((image_path, class_index - 1))
    return samples


class ImageDataset(torch.utils.data.Dataset):
    def __init__(self, samples, augment=False):
        self.samples = samples
        self.transform = transforms.Compose(
            [
                *((
                    transforms.RandomHorizontalFlip(),
                    transforms.RandomRotation(10),
                ) if augment else ()),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.5] * 3, std=[0.5] * 3),
            ]
        )

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        image_path, label = self.samples[index]
        image = Image.open(image_path).convert("RGB")
        image.thumbnail((448, 448), Image.Resampling.LANCZOS)

        padded = Image.new("RGB", (448, 448), (255, 255, 255))
        offset = ((448 - image.width) // 2, (448 - image.height) // 2)
        padded.paste(image, offset)

        return self.transform(padded), label


class FNN(torch.nn.Module):
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
        return self.fc(x)


def split_samples(samples, validation_split, seed):
    shuffled_samples = samples[:]
    random.Random(seed).shuffle(shuffled_samples)

    validation_count = max(1, int(len(shuffled_samples) * validation_split))
    validation_samples = shuffled_samples[:validation_count]
    training_samples = shuffled_samples[validation_count:]

    if not training_samples:
        raise ValueError("Not enough samples to create a training split.")

    return training_samples, validation_samples


def build_folds(samples, num_folds, seed):
    shuffled_samples = samples[:]
    random.Random(seed).shuffle(shuffled_samples)

    fold_sizes = [len(shuffled_samples) // num_folds] * num_folds
    for index in range(len(shuffled_samples) % num_folds):
        fold_sizes[index] += 1

    folds = []
    start = 0
    for fold_size in fold_sizes:
        end = start + fold_size
        folds.append(shuffled_samples[start:end])
        start = end
    return folds


def create_data_loader(samples, augment, shuffle):
    dataset = ImageDataset(samples, augment=augment)
    return torch.utils.data.DataLoader(
        dataset,
        batch_size=BATCH_SIZE,
        shuffle=shuffle,
    )


def create_model(device):
    model = FNN().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.0005)
    return model, optimizer


def run_epoch(model, loader, criterion, device, optimizer=None):
    is_training = optimizer is not None
    model.train(mode=is_training)
    total_loss = 0.0

    for x_batch, y_batch in loader:
        x_batch = x_batch.to(device)
        y_batch = y_batch.to(device)

        if is_training:
            optimizer.zero_grad()

        with torch.set_grad_enabled(is_training):
            predictions = model(x_batch)
            loss = criterion(predictions, y_batch)

            if is_training:
                loss.backward()
                optimizer.step()

        total_loss += loss.item()

    return total_loss / len(loader)


def assess_learning_status(training_loss, validation_loss):
    loss_gap = validation_loss - training_loss
    relative_gap = loss_gap / max(training_loss, 1e-8)

    if training_loss > 1.0 and validation_loss > 1.0:
        return "underfitting"
    if relative_gap > 0.2:
        return "overfitting"
    return "learning properly"


def train_model(training_samples, validation_samples, device, prefix, verbose):
    training_loader = create_data_loader(training_samples, augment=True, shuffle=True)
    validation_loader = create_data_loader(validation_samples, augment=False, shuffle=False)

    model, optimizer = create_model(device)
    criterion = torch.nn.CrossEntropyLoss()

    best_state = copy.deepcopy(model.state_dict())
    best_validation_loss = float("inf")
    final_training_loss = None
    final_validation_loss = None

    for epoch in range(NUM_EPOCHS):
        print("epoch", epoch)
        training_loss = run_epoch(model, training_loader, criterion, device, optimizer)
        validation_loss = run_epoch(model, validation_loader, criterion, device)
        status = assess_learning_status(training_loss, validation_loss)

        if validation_loss < best_validation_loss:
            best_validation_loss = validation_loss
            best_state = copy.deepcopy(model.state_dict())

        final_training_loss = training_loss
        final_validation_loss = validation_loss

        if verbose:
            print(
                f"{prefix} Epoch {epoch + 1:03d} | "
                f"Training loss: {training_loss:.4f} | "
                f"Validation loss: {validation_loss:.4f} | "
                f"Status: {status}"
            )

    model.load_state_dict(best_state)
    return model, final_training_loss, final_validation_loss


def run_cross_validation(training_samples, device):
    if len(training_samples) < 2:
        print("Cross-validation skipped: need at least 2 training samples.")
        return

    fold_count = min(NUM_FOLDS, len(training_samples))
    folds = build_folds(training_samples, fold_count, SEED)

    print(f"Running {fold_count}-fold cross-validation on the training split...")
    fold_training_losses = []
    fold_validation_losses = []

    for fold_index in range(fold_count):
        validation_samples = folds[fold_index]
        fold_training_samples = [
            sample
            for current_index, fold in enumerate(folds)
            if current_index != fold_index
            for sample in fold
        ]

        model, training_loss, validation_loss = train_model(
            fold_training_samples,
            validation_samples,
            device,
            prefix=f"Fold {fold_index + 1}/{fold_count}",
            verbose=False,
        )

        del model

        fold_training_losses.append(training_loss)
        fold_validation_losses.append(validation_loss)

        print(
            f"Fold {fold_index + 1}/{fold_count} | "
            f"Training loss: {training_loss:.4f} | "
            f"Validation loss: {validation_loss:.4f} | "
            f"Status: {assess_learning_status(training_loss, validation_loss)}"
        )

    average_training_loss = sum(fold_training_losses) / len(fold_training_losses)
    average_validation_loss = sum(fold_validation_losses) / len(fold_validation_losses)
    print(
        f"Cross-validation average | "
        f"Training loss: {average_training_loss:.4f} | "
        f"Validation loss: {average_validation_loss:.4f} | "
        f"Status: {assess_learning_status(average_training_loss, average_validation_loss)}"
    )


device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
all_samples = build_samples()
training_samples, validation_samples = split_samples(all_samples, VALIDATION_SPLIT, SEED)

print(
    f"Total samples: {len(all_samples)} | "
    f"Training samples: {len(training_samples)} | "
    f"Validation samples: {len(validation_samples)}"
)

run_cross_validation(training_samples, device)

print("\nTraining final model with a 20% holdout validation split...")
model, training_loss, validation_loss = train_model(
    training_samples,
    validation_samples,
    device,
    prefix="Final",
    verbose=True,
)

print(
    f"Final summary | Training loss: {training_loss:.4f} | "
    f"Validation loss: {validation_loss:.4f} | "
    f"Status: {assess_learning_status(training_loss, validation_loss)}"
)

torch.save(model.state_dict(), "model.pth")

model.eval()
model_cpu = model.to("cpu")
dummy_input = torch.randn(1, 3, 448, 448).to("cpu")

try:
    onnx_path = "model.onnx"
    onnx_external_data_path = f"{onnx_path}.data"
    parent_onnx_path = os.path.join("..", onnx_path)

    torch.onnx.export(
        model_cpu,
        dummy_input,
        onnx_path,
        export_params=True,
        opset_version=11,
        external_data=False,
        do_constant_folding=True,
        input_names=["image"],
        output_names=["output"],
    )

    if os.path.exists(onnx_external_data_path):
        os.remove(onnx_external_data_path)

    try:
        shutil.copy2(onnx_path, parent_onnx_path)
        print(f"Copied {onnx_path} to {parent_onnx_path}")
    except PermissionError:
        print(f"Saved {onnx_path} locally (skipped copying to {parent_onnx_path})")

    print("Model saved as model.pth and model.onnx")
except Exception as error:
    print(f"ONNX export failed: {error}")
