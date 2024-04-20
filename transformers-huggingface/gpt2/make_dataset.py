from datasets import Dataset
import pandas as pd

df = pd.read_csv('a.csv')
try:
    df = pd.read_csv('a.csv')
except pd.errors.ParserError:
    print("Error reading CSV file. Please check the data format.")
    exit()
train_data = df.sample(frac=0.8, random_state=42)
test_data = df.drop(train_data.index)

train_dict = {"question": train_data["question"].tolist(), "answer": train_data["answer"].tolist()}
test_dict = {"question": test_data["question"].tolist(), "answer": test_data["answer"].tolist()}

train_dataset = Dataset.from_dict(train_dict)
test_dataset = Dataset.from_dict(test_dict)

train_dataset.save_to_disk("./tr1.dataset")
test_dataset.save_to_disk("./ts1.dataset")