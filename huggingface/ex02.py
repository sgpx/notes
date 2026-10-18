import os

# Disable automatic offloading and allow memory fragmentation
os.environ['ACCELERATE_ALLOW_OFFLOADING'] = "0"
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"
os.environ['PYTORCH_CUDA_ALLOC_CONF'] = "expandable_segments:True"

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device = torch.device("cuda")

# Move model to GPU directly upon loading (avoid conflicts with offloading)
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1", device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

prompt = "My favourite condiment is"

model_inputs = tokenizer([prompt], return_tensors="pt") #.to(device)

# Reduce batch size to manage memory usage
generated_ids = model.generate(**model_inputs, max_new_tokens=20, do_sample=True)
print(tokenizer.batch_decode(generated_ids)[0])
