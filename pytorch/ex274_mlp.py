import json
import argparse
import datetime
import random
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader

# ==========================================
# 0. Device Selection
# ==========================================
def get_device():
    if torch.cuda.is_available():
        return torch.device("mps")
    elif torch.cuda.is_available():
        return torch.device("cuda")
    if hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
        return torch.device("mps")
    return torch.device("cpu")

# ==========================================
# 1. Model Definition
# ==========================================
class TrackRecommenderMLP(nn.Module):
    def __init__(self, track_emb_dim=1536, time_emb_dim=8, day_emb_dim=8, hidden_dim=256):
        super().__init__()
        # Embeddings for Time (0-3) and Day (0-6)
        self.time_embedding = nn.Embedding(num_embeddings=4, embedding_dim=time_emb_dim)
        self.day_embedding = nn.Embedding(num_embeddings=7, embedding_dim=day_emb_dim)
        
        # Concat: track_emb + time_emb + day_emb
        input_dim = track_emb_dim + time_emb_dim + day_emb_dim
        
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.dropout = nn.Dropout(0.2)
        self.fc2 = nn.Linear(hidden_dim, track_emb_dim)
        
    def forward(self, recent_tracks_emb, time_idx, day_idx):
        t_emb = self.time_embedding(time_idx)
        d_emb = self.day_embedding(day_idx)
        
        x = torch.cat([recent_tracks_emb, t_emb, d_emb], dim=-1)
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        predicted_emb = self.fc2(x)
        
        return predicted_emb

# ==========================================
# 2. Data Parsing & Dataset Configuration
# ==========================================
def parse_timestamp(ts_str):
    """Converts ISO timestamp to time_idx (0-3) and day_idx (0-6)."""
    # Replace Z for older python version compatibility
    dt = datetime.datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
    time_idx = dt.hour // 6  # 0: 0-5, 1: 6-11, 2: 12-17, 3: 18-23
    day_idx = dt.weekday()   # 0: Mon ... 6: Sun
    return dt, time_idx, day_idx

class ListeningHistoryDataset(Dataset):
    def __init__(self, data_file, window_size=3):
        with open(data_file, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
            
        self.samples = []
        self.window_size = window_size
        
        # Filter and extract sequential data
        valid_tracks = []
        for item in raw_data:
            if "embeddings" in item and "text-embedding-3-small" in item["embeddings"]:
                emb = item["embeddings"]["text-embedding-3-small"]
                dt, t_idx, d_idx = parse_timestamp(item["timestamp"])
                valid_tracks.append({
                    "title": item.get("title", "Unknown"),
                    "emb": torch.tensor(emb, dtype=torch.float32),
                    "time_idx": t_idx,
                    "day_idx": d_idx,
                    "datetime": dt
                })
        
        # Create context windows
        # Step T: Context (Mean of last N tracks), Time (of target), Day (of target)
        # Step T+1: Target track embedding
        for i in range(self.window_size, len(valid_tracks)):
            history = valid_tracks[i - self.window_size : i]
            target = valid_tracks[i]
            
            # Pseudo-sequence: average of recent embeddings
            history_embs = torch.stack([t["emb"] for t in history])
            mean_history_emb = torch.mean(history_embs, dim=0)
            
            self.samples.append({
                "history_emb": mean_history_emb,
                "time_idx": torch.tensor(target["time_idx"], dtype=torch.long),
                "day_idx": torch.tensor(target["day_idx"], dtype=torch.long),
                "target_emb": target["emb"]
            })
            
        # Determine embedding dimension dynamically from first sample
        self.emb_dim = self.samples[0]["target_emb"].shape[0] if self.samples else 1536

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        return self.samples[idx]

# ==========================================
# 3. Training Logic
# ==========================================
def train_model(data_file="out.json", epochs=30, batch_size=32):
    print("Loading data and creating sequences...")
    dataset = ListeningHistoryDataset(data_file)
    device = get_device()
    print(f"Using device: {device}")
    dataloader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=True,
        pin_memory=(device.type == "cuda"),
    )
    
    model = TrackRecommenderMLP(track_emb_dim=dataset.emb_dim).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
    
    # CosineEmbeddingLoss expects targets of 1 (maximize similarity)
    criterion = nn.CosineEmbeddingLoss()
    
    print("Starting training...")
    model.train()
    for epoch in range(epochs):
        total_loss = 0.0
        for batch in dataloader:
            history_emb = batch["history_emb"].to(device, non_blocking=True)
            time_idx = batch["time_idx"].to(device, non_blocking=True)
            day_idx = batch["day_idx"].to(device, non_blocking=True)
            target_emb = batch["target_emb"].to(device, non_blocking=True)
            
            optimizer.zero_grad()
            predicted_emb = model(history_emb, time_idx, day_idx)
            
            target_sim = torch.ones(history_emb.size(0), device=device)
            loss = criterion(predicted_emb, target_emb, target_sim)
            
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            
        print(f"Epoch {epoch+1}/{epochs} | Loss: {total_loss/len(dataloader):.4f}")
        
    torch.save(model.state_dict(), "model.pth")
    print("Model saved to model.pth")

# ==========================================
# 4. Inference Logic (With Time Decay)
# ==========================================
def infer_recommendations(data_file="out.json", window_size=3, top_k=5, randomize_context=False):
    # 1. Load the pool of all known tracks and their latest play dates
    with open(data_file, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    candidate_pool = {}
    history = []
    
    # Build candidate pool (unique tracks) and sequential history
    for item in raw_data:
        if "embeddings" in item and "text-embedding-3-small" in item["embeddings"]:
            dt, _, _ = parse_timestamp(item["timestamp"])
            emb = torch.tensor(item["embeddings"]["text-embedding-3-small"], dtype=torch.float32)
            title = item.get("title", "Unknown")
            
            # Keep track of the absolute last time the user played this track
            candidate_pool[title] = {"emb": emb, "last_played": dt}
            history.append(emb)

    if len(history) < window_size:
        print("Not enough history to generate a recommendation.")
        return

    device = get_device()
    print(f"Using device: {device}")

    # 2. Prepare Current State
    # Pseudo-sequence: average of the absolute last `window_size` tracks listened to
    recent_embs = torch.stack(history[-window_size:]).to(device)
    current_history_emb = torch.mean(recent_embs, dim=0).unsqueeze(0) # (1, D)
    
    # Current context: we assume the user wants a recommendation for right NOW,
    # unless random inference is requested.
    now = datetime.datetime.now(datetime.timezone.utc)
    if randomize_context:
        current_time_idx_value = random.randrange(4)
        current_day_idx_value = random.randrange(7)
        context_label = f"Randomized context | Day {current_day_idx_value} | Time Block {current_time_idx_value}"
    else:
        current_time_idx_value = now.hour // 6
        current_day_idx_value = now.weekday()
        context_label = f"{now.strftime('%A')}, Time Block {current_time_idx_value}"

    current_time_idx = torch.tensor([current_time_idx_value], dtype=torch.long, device=device)
    current_day_idx = torch.tensor([current_day_idx_value], dtype=torch.long, device=device)

    # 3. Load Model & Predict
    emb_dim = current_history_emb.shape[1]
    model = TrackRecommenderMLP(track_emb_dim=emb_dim).to(device)
    try:
        model.load_state_dict(torch.load("model.pth", map_location=device, weights_only=True))
    except FileNotFoundError:
        print("model.pth not found. Please run with --train first.")
        return
        
    model.eval()
    with torch.no_grad():
        predicted_emb = model(current_history_emb, current_time_idx, current_day_idx)

    # 4. Score Candidate Pool (Cosine Similarity + Time Decay)
    results = []
    for title, data in candidate_pool.items():
        # Raw cosine similarity between prediction and candidate
        raw_sim = F.cosine_similarity(predicted_emb, data["emb"].to(device).unsqueeze(0)).item()
        
        # Time Decay Penalty (Addresses the "Heyday" burnout)
        # If the user hasn't played it in a long time, we gently penalize the score
        days_since_played = (now - data["last_played"]).days
        
        # E.g., decay the score by 1% for every day since it was last played
        # Cap decay so old songs can still surface if the mood is a perfect match
        decay_factor = max(0.85, 0.99 ** days_since_played) 
        
        final_score = raw_sim * decay_factor
        results.append((title, final_score, raw_sim, days_since_played))

    def diversify_results(scored_results, cluster_similarity=0.92):
        if not scored_results:
            return []

        sorted_results = sorted(scored_results, key=lambda x: x[1], reverse=True)
        chosen_clusters = []
        cluster_centroids = []

        for item in sorted_results:
            title = item[0]
            emb = candidate_pool[title]["emb"].to(device)

            best_cluster_idx = None
            best_similarity = -1.0
            for idx, centroid in enumerate(cluster_centroids):
                similarity = F.cosine_similarity(
                    emb.unsqueeze(0), centroid.unsqueeze(0)
                ).item()
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_cluster_idx = idx

            if best_cluster_idx is not None and best_similarity >= cluster_similarity:
                chosen_clusters[best_cluster_idx].append(item)
                cluster_members = [
                    candidate_pool[cluster_item[0]]["emb"].to(device)
                    for cluster_item in chosen_clusters[best_cluster_idx]
                ]
                cluster_centroids[best_cluster_idx] = torch.mean(
                    torch.stack(cluster_members), dim=0
                )
            else:
                chosen_clusters.append([item])
                cluster_centroids.append(emb)

        representatives = []
        for cluster in chosen_clusters:
            cluster.sort(key=lambda x: x[1], reverse=True)
            representatives.append(cluster[0])

        representatives.sort(key=lambda x: x[1], reverse=True)
        return representatives[:top_k]

    # 5. Output Top K with diversity
    results = diversify_results(results, cluster_similarity=0.92)
    
    print("\n" + "="*50)
    print(f"Context: {context_label}")
    print("="*50)
    if results:
        primary = results[0]
        print("Primary pick:\n")
        title, final_score, raw_sim, days_ago = primary
        print(f"1. {title}")
        print(f"   Final Score: {final_score:.4f} (Raw: {raw_sim:.4f} | Last Played: {days_ago} days ago)\n")

    if len(results) > 1:
        print("Diverse alternates:\n")
        for i, (title, final_score, raw_sim, days_ago) in enumerate(results[1:top_k], 2):
            print(f"{i}. {title}")
            print(f"   Final Score: {final_score:.4f} (Raw: {raw_sim:.4f} | Last Played: {days_ago} days ago)\n")
    elif not results:
        print("No recommendations available.\n")

# ==========================================
# 5. Entry Point
# ==========================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Lightweight PyTorch Recommendation System")
    parser.add_argument("--train", action="store_true", help="Train the model using out.json")
    parser.add_argument("--infer", action="store_true", help="Infer next tracks based on latest history")
    parser.add_argument("--infer:random", dest="infer_random", action="store_true", help="Infer with randomized day of week and time of day")
    
    args = parser.parse_args()
    
    if args.train:
        train_model("out.json")
    elif args.infer or args.infer_random:
        infer_recommendations("out.json", randomize_context=args.infer_random)
    else:
        print("Please provide either --train or --infer. Use -h for help.")
