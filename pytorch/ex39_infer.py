import torch
import pickle
import json

class SimpleClassifier(torch.nn.Module):
    def __init__(self, num_inputs, num_classes):
        super().__init__()
        self.network = torch.nn.Sequential(
            torch.nn.Linear(num_inputs, 128),
            torch.nn.ReLU(),
            torch.nn.Dropout(0.3),
            torch.nn.Linear(128, 64),
            torch.nn.ReLU(),
            torch.nn.Linear(64, num_classes)
        )
    def forward(self, x):
        return self.network(x)

# --- LOAD SAVED ARTIFACTS ---
LABEL_OPTS = ["A","B","C"]
MAX_VOCAB_SIZE = 4000 

# Load Vectorizer
with open("vectorizer.pkl", "rb") as f:
    loaded_vectorizer = pickle.load(f)

# Load Model
model = SimpleClassifier(num_inputs=MAX_VOCAB_SIZE, num_classes=len(LABEL_OPTS))
model.load_state_dict(torch.load("product_classifier.pth"))
model.eval() # Important! Sets model to evaluation mode

def get_neural_label(content_heuristic):
    # 1. Prepare text
    if not isinstance(content_heuristic, str):
        content_heuristic = json.dumps(content_heuristic)
    
    # 2. Vectorize (Text -> Numbers)
    # Note: use transform(), NOT fit_transform()
    input_vector = loaded_vectorizer.transform([content_heuristic]).toarray()
    input_tensor = torch.tensor(input_vector, dtype=torch.float32)
    
    # 3. Predict
    with torch.no_grad():
        output = model(input_tensor)
        predicted_id = torch.argmax(output).item()
        
    return LABEL_OPTS[predicted_id]

ai_label = get_neural_label(i.get("my_label"))
