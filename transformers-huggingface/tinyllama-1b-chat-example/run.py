import transformers
tokenizer = transformers.LlamaTokenizer("tokenizer.model")
model = transformers.LlamaForCausalLM.from_pretrained(".")
input_text = "what is pytorch?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids, max_length=50, num_return_sequences=1, do_sample=True)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
