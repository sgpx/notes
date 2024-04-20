from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from datasets import Dataset
import torch

tokenizer = GPT2Tokenizer.from_pretrained("gpt2-large")
tokenizer.add_special_tokens({'pad_token': '[PAD]'})
model = GPT2LMHeadModel.from_pretrained("gpt2-large")

training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=10_000,
    save_total_limit=2,
    use_mps_device=True,
    remove_unused_columns=False
)

dx = Dataset.from_csv("a.csv")

# Tokenize all the text data
tokenized_texts = []
for text in dx['text']:
    tokenized_text = tokenizer(text, padding='max_length', truncation=True, max_length=512, return_tensors="pt")
    tokenized_texts.append(tokenized_text)

# Create a new Dataset with the tokenized input_ids
tokenized_dataset = Dataset.from_dict({"input_ids": torch.cat([text['input_ids'] for text in tokenized_texts], dim=0),
                                       "attention_mask": torch.cat([text['attention_mask'] for text in tokenized_texts], dim=0)})

trainer = Trainer(
    model=model,
    tokenizer=tokenizer,
    args=training_args,
    train_dataset=tokenized_dataset,
)

trainer.train()

model.save_pretrained("./mymodel")