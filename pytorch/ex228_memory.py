import json
import os

FAILURE_FILE = "ex226_failures.json"

def update_failures(categories):
    stats = get_failure_stats()
    for cat in categories:
        cat = cat.lower()
        stats[cat] = stats.get(cat, 0) + 1
        
    with open(FAILURE_FILE, "w") as f:
        json.dump(stats, f)

def get_failure_stats():
    if os.path.exists(FAILURE_FILE):
        try:
            with open(FAILURE_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}
