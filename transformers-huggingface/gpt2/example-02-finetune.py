from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
from torch import device
from torch.utils.data import Dataset
import torch

class CustomDataset(Dataset):
    def __init__(self, num_samples=1000):
        self.num_samples = num_samples
        self.samples = []
        
        for _ in range(num_samples):
            text = "This is a sample text for PyTorch dataset"
            label = torch.randint(0, 2, (1,)).item()
            self.samples.append((text, label))
    
    def __len__(self):
        return self.num_samples
    
    def __getitem__(self, idx):
        text, label = self.samples[idx]
        return text, label

dataset = CustomDataset(num_samples=5)

mps = device("mps") # apple metal performance shaders

from datasets import load_dataset
dataset = load_dataset("text")

model = GPT2LMHeadModel.from_pretrained('gpt2-large')
model = model.to(mps)
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    use_mps_device=True
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    tokenizer=tokenizer,
)

print("starting training..")
trainer.train()
model.save_pretrained('./finetuned_model')
