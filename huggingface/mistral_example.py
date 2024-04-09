import os
os.environ['ACCELERATE_ALLOW_OFFLOADING'] = "0"
os.environ['CUDA_LAUNCH_BLOCKING'] = "1"

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

device = torch.device("cuda")
model = AutoModelForCausalLM.from_pretrained("mistralai/Mistral-7B-v0.1", device_map="cuda")
tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-v0.1")

prompt = "My favourite condiment is"

model_inputs = tokenizer([prompt], return_tensors="pt").to("cuda")
model.to(device)

generated_ids = model.generate(**model_inputs, max_new_tokens=30, do_sample=True)
print(tokenizer.batch_decode(generated_ids)[0])
