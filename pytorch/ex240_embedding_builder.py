import os
import sqlite3
import torch
import clip
from PIL import Image
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import cpu_count

# --- Configuration ---
IMAGES_DIR = './frames/'
DB_PATH = 'embeddings.db'
MODEL_NAME = 'ViT-L/14'
BATCH_SIZE = 64  # Increased for C7g performance
# Use 4 physical/logical cores
NUM_WORKERS = cpu_count() 

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute('CREATE TABLE IF NOT EXISTS embeddings (path TEXT PRIMARY KEY, vector BLOB)')
    conn.commit()
    return conn

def get_processed_files(conn):
    cursor = conn.execute('SELECT path FROM embeddings')
    return set(row[0] for row in cursor.fetchall())

def load_and_preprocess(path, preprocess_func):
    """Worker function for ThreadPoolExecutor."""
    try:
        with Image.open(path) as img:
            processed = preprocess_func(img.convert('RGB'))
        return path, processed
    except Exception:
        return path, None

def main():
    conn = init_db()
    processed = get_processed_files(conn)
    
    device = "cpu"
    model, preprocess = clip.load(MODEL_NAME, device=device)
    # Allow PyTorch to use all available cores for matrix ops
    torch.set_num_threads(NUM_WORKERS)

    all_files = [os.path.join(IMAGES_DIR, f) for f in os.listdir(IMAGES_DIR) 
                 if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    pending_files = [f for f in all_files if f not in processed]
    
    # Use ThreadPoolExecutor for IO-bound image loading/decoding
    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as executor:
        for i in range(0, len(pending_files), BATCH_SIZE):
            batch_paths = pending_files[i : i + BATCH_SIZE]
            
            # Parallel IO
            futures = [executor.submit(load_and_preprocess, p, preprocess) for p in batch_paths]
            results = [f.result() for f in futures]
            
            valid_images = [r[1] for r in results if r[1] is not None]
            valid_paths = [r[0] for r in results if r[1] is not None]

            if not valid_images: continue

            # Batch Inference
            with torch.no_grad():
                image_input = torch.stack(valid_images).to(device)
                embeddings = model.encode_image(image_input).numpy()

            # Batch Save
            conn.executemany('INSERT OR REPLACE INTO embeddings VALUES (?, ?)', 
                             [(p, e.tobytes()) for p, e in zip(valid_paths, embeddings)])
            conn.commit()
            print(f"Processed {min(i + BATCH_SIZE, len(pending_files))} / {len(pending_files)}")

    conn.close()

if __name__ == '__main__':
    main()
