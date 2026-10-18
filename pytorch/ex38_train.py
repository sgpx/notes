import pymongo
import json
import pickle  # To save the vectorizer
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
import dotenv

# Load environment variables
dotenv.load_dotenv()

# --- CONFIGURATION ---
BATCH_SIZE = 64
LEARNING_RATE = 0.001
EPOCHS = 10
MAX_VOCAB_SIZE = 4000  # Keep top 4000 words. Increase if you have enough RAM.
MODEL_SAVE_PATH = "product_classifier.pth"
VECTORIZER_SAVE_PATH = "vectorizer.pkl"
LABEL_OPTS = ["A","B","C"]
label_to_id = {name: i for i, name in enumerate(LABEL_OPTS)}

# --- 1. CONNECT & FETCH DATA ---
print("Connecting to MongoDB...")
conn = pymongo.MongoClient(os.getenv("MONGODB_ATLAS_URI"))
col = conn["mydb"]["mycol"]

print("Fetching data (this might take a moment)...")
# We only fetch the fields we need to save RAM
# query matches items where my_label exists and is in our known list
query = {"my_label": {"$in": LABEL_OPTS}}
projection = {"target_var": 1, "my_label": 1}

cursor = col.find(query, projection)

texts = []
labels = []

for doc in cursor:
    content = doc.get("target_var", "")
    label_str = doc.get("my_label")
    
    # SAFETY: Ensure content is a string (if it's a dict/json in mongo, stringify it)
    if not isinstance(content, str):
        content = json.dumps(content)
    
    texts.append(content)
    labels.append(label_to_id[label_str])

print(f"Loaded {len(texts)} examples.")

# --- 2. PREPROCESSING (Text -> Numbers) ---
print("Vectorizing text...")
# This converts sentences into "Bag of Words" vectors
vectorizer = CountVectorizer(max_features=MAX_VOCAB_SIZE, stop_words='english')
X_numpy = vectorizer.fit_transform(texts).toarray()
y_numpy = np.array(labels)

# Convert to PyTorch Tensors
X_tensor = torch.tensor(X_numpy, dtype=torch.float32)
y_tensor = torch.tensor(y_numpy, dtype=torch.long)

# Split into Training (80%) and Validation (20%) sets
# It is crucial to hold back data to check if the model is actually learning or just memorizing
X_train, X_val, y_train, y_val = train_test_split(X_tensor, y_tensor, test_size=0.2, random_state=42)

# Create DataLoaders (Handles batching)
train_dataset = TensorDataset(X_train, y_train)
train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

val_dataset = TensorDataset(X_val, y_val)
val_loader = DataLoader(val_dataset, batch_size=BATCH_SIZE)

# --- 3. DEFINE MODEL ---
class SimpleClassifier(nn.Module):
    def __init__(self, num_inputs, num_classes):
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(num_inputs, 128),
            nn.ReLU(),
            nn.Dropout(0.3), # Prevents overfitting by randomly turning off neurons
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, num_classes)
        )
    
    def forward(self, x):
        return self.network(x)

# --- 4. SETUP DEVICE & TRAINING ---
# Check for Apple Silicon (MPS) or NVIDIA (CUDA)

if torch.backends.mps.is_available():
    device = torch.device("mps")
elif torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")

print(f"Training on device: {device}")

model = SimpleClassifier(num_inputs=MAX_VOCAB_SIZE, num_classes=len(LABEL_OPTS))
model.to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=LEARNING_RATE)

# --- 5. TRAINING LOOP ---
for epoch in range(EPOCHS):
    model.train() # Set mode to training
    total_loss = 0
    
    for batch_X, batch_y in train_loader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)
        
        optimizer.zero_grad()           # Reset gradients
        outputs = model(batch_X)        # Forward pass
        loss = criterion(outputs, batch_y) # Calculate loss
        loss.backward()                 # Backward pass
        optimizer.step()                # Update weights
        
        total_loss += loss.item()
    
    # Validation step (Check accuracy on data it hasn't seen)
    model.eval() # Set mode to evaluation
    correct = 0
    total = 0
    with torch.no_grad():
        for val_X, val_y in val_loader:
            val_X, val_y = val_X.to(device), val_y.to(device)
            outputs = model(val_X)
            _, predicted = torch.max(outputs.data, 1)
            total += val_y.size(0)
            correct += (predicted == val_y).sum().item()
            
    val_acc = 100 * correct / total
    print(f"Epoch [{epoch+1}/{EPOCHS}] | Loss: {total_loss/len(train_loader):.4f} | Val Accuracy: {val_acc:.2f}%")

# --- 6. SAVE ARTIFACTS ---
print("Saving model and vectorizer...")
torch.save(model.state_dict(), MODEL_SAVE_PATH)
with open(VECTORIZER_SAVE_PATH, "wb") as f:
    pickle.dump(vectorizer, f)

print("Done! You can now use these files for inference.")
