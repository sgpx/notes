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

songs = ["Dear You - Higurashi no Naku Koro Ni", "Prince - When Doves Cry","They Don't Care About Us","MJ The Bad Tour","You Shook Me All Night Long", "Forrest Gump", "Prince - 1999","Social Distortion | Story of My Life", "Prince and the Revolution - Let's Go Crazy","No Celebrity Could Stay Serious Around Prince!", "The Cure - Trust"]

for song_title in songs:
    emb = llm.get_embedding(f"Media title: {song_title}")
    emb = torch.tensor(emb, dtype=torch.float32).to("mps")

    Y_pred = model(emb)
    #print("Media title:", song_title)
    #print("Embedding:", emb[:10])
    #print("Y_pred:", Y_pred)
    probability = torch.sigmoid(Y_pred).item()
    #print(f"Probability: {probability:.4f}")
    prediction = 1 if probability >= 0.5 else 0
    #print(f"Predicted Class: {prediction}")
    print(f"{song_title} : {'IS_MUSIC' if prediction else 'NOT_MUSIC'}")
