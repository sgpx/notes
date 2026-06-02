from ex226_constants import CHAR_LIM, VOCAB_SIZE
import torch.nn as nn

class FNN(nn.Module): 
    def __init__(self):
        super().__init__()
        # 44 features in, 128 hidden state (64 per direction)
        self.rnn = nn.GRU(
            input_size=VOCAB_SIZE, 
            hidden_size=64, 
            num_layers=2, 
            batch_first=True, 
            bidirectional=True
        )
        # Maps the combined bidirectional hidden states to a single logit per character
        self.classifier = nn.Linear(64 * 2, 1)

    def forward(self, x):
        # x is currently (Batch, 4096 * 44) or (Batch, CHAR_LIM * VOCAB_SIZE)
        # Reshape it to (Batch, Sequence, Features)
        x = x.view(-1, CHAR_LIM, VOCAB_SIZE)
        
        # RNN outputs (Batch, Sequence, Hidden*2)
        out, _ = self.rnn(x)
        
        # Classifier outputs (Batch, Sequence, 1)
        logits = self.classifier(out)
        
        # Squeeze to (Batch, Sequence) to match expected training shape
        return logits.squeeze(-1)
