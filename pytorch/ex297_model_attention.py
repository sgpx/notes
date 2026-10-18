import torch.nn as nn

class SimpleNN(nn.Module):
    def __init__(self, embedding_dim=1536, num_heads=8, dropout_rate=0.3):
        super().__init__()
        
        self.embedding_projection = nn.Linear(embedding_dim, 256)
        
        # Self-attention to weight embedding dimensions
        self.attention = nn.MultiheadAttention(
            embed_dim=256,
            num_heads=num_heads,
            dropout=dropout_rate,
            batch_first=True
        )
        
        self.fc_layers = nn.Sequential(
            nn.Linear(256, 128),
            nn.BatchNorm1d(128),
            nn.ReLU(),
            nn.Dropout(dropout_rate),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)
        )
    
    def forward(self, embedding):
        # embedding shape: (batch_size, 512)
        x = self.embedding_projection(embedding)  # (batch_size, 256)
        x = x.unsqueeze(1)  # (batch_size, 1, 256) for attention
        
        # Self-attention
        attn_out, _ = self.attention(x, x, x)  # (batch_size, 1, 256)
        x = attn_out.squeeze(1)  # (batch_size, 256)
        
        return self.fc_layers(x)

