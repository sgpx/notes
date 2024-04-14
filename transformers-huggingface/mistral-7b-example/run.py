import transformers as t
tokenizer = t.AutoTokenizer.from_pretrained(".")
# streamer = t.TextStreamer(tokenizer=tokenizer)
model = t.MistralForCausalLM.from_pretrained(".")
# print([i for i in dir(t) if "mistral" in i.lower()])
input_text = "what is pytorch?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids, max_length=50, num_return_sequences=1, do_sample=True)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
