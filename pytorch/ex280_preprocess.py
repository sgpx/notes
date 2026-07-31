import json
import dotenv
from multiprocessing import Pool
import llm


def process_item(item):
    """Process a single item and return it with embeddings."""
    title = item.get("title")

    if not title:
        print("Missing title in item:", item)
        return item

    embedding_value = llm.get_embedding("Video title: " + title)

    item["embeddings"] = {"text-embedding-3-small": embedding_value}
    return item


if __name__ == "__main__":
    dotenv.load_dotenv()

    with open("ex280_lv3.json", "r") as fr:
        a = json.load(fr)

    num_workers = 10
    chunk_size = max(1, len(a) // (num_workers * 4))

    print(f"Starting processing {len(a)} items with {num_workers} workers...")

    results = []
    with Pool(processes=num_workers) as pool:
        for processed_item in pool.imap(process_item, a, chunksize=chunk_size):
            results.append(processed_item)

    with open("ex280_lv4.json", "w") as fw:
        json.dump(results, fw, indent=2)

    print("Done!")
