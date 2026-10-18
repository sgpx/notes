from transformers import GPT2LMHeadModel, GPT2Tokenizer

model = GPT2LMHeadModel.from_pretrained('gpt2-large')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')

input_tensors = tokenizer.encode("where did the sorrow go", return_tensors="pt")

generated_text_ids = model.generate(input_tensors, max_length=1000)
generated_text = tokenizer.decode(generated_text_ids[0], skip_special_tokens=True)
print(generated_text)