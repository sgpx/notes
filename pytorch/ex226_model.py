from ex226_constants import CHAR_LIM, VOCAB_SIZE
import torch.nn as nn

class FNN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(CHAR_LIM * VOCAB_SIZE, 1024)
        self.Sigmoid1 = nn.Sigmoid()
        self.fc2 = nn.Linear(1024, 512)
        self.Sigmoid2 = nn.Sigmoid()
        self.fc3 = nn.Linear(512, CHAR_LIM)

    def forward(self, x):
        x = self.fc1(x)
        x = self.Sigmoid1(x)
        x = self.fc2(x)
        x = self.Sigmoid2(x)
        x = self.fc3(x)
        return x
