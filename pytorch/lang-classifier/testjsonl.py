import json
import subprocess
import tempfile
import os

# -----------------------
# Run inference script on a temp file
# -----------------------
def predict_with_infer(text: str):
    with tempfile.NamedTemporaryFile(mode="w", delete=False, suffix=".txt", encoding="utf-8") as f:
        f.write(text)
        temp_path = f.name

    try:
        result = subprocess.check_output(["py","infer.py", temp_path], text=True)
        print(result)
        return "NON-PYTHON" if "NON-PYTHON" in result else "PYTHON"

    finally:
        os.remove(temp_path)


# -----------------------
# Evaluate dataset
# -----------------------
correct = 0
total = 0

tp = fp = tn = fn = 0

with open("test.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        item = json.loads(line)

        label = item["label"]
        text = item["text"]

        pred = predict_with_infer(text)
        print("actual: ", label)
        total += 1
        is_correct = (pred == label)

        if is_correct:
            correct += 1

        # confusion matrix logic
        if label == "PYTHON" and pred == "PYTHON":
            tp += 1
        elif label == "PYTHON" and pred == "NON-PYTHON":
            fn += 1
        elif label == "NON-PYTHON" and pred == "NON-PYTHON":
            tn += 1
        elif label == "NON-PYTHON" and pred == "PYTHON":
            fp += 1

        print(f"{total:03d} | true={label} | pred={pred} | {'✓' if is_correct else '✗'}")


# -----------------------
# Results
# -----------------------
print("\n===== RESULTS =====")
print("Total:", total)
print("Accuracy:", correct / total if total else 0)

print("\nConfusion Matrix:")
print("TP:", tp, "FP:", fp)
print("FN:", fn, "TN:", tn)