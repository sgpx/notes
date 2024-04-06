# transformers

```
pip3 install transformers
```

# may require pytorch

```
pip3 install torch sentencepiece
```

# tinyllama example

```
import transformers
tokenizer = transformers.LlamaTokenizer("tokenizer.model")
model = transformers.LlamaForCausalLM.from_pretrained(".")
input_text = "what is pytorch?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids, max_length=50, num_return_sequences=1, do_sample=True)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
```

# gpt2 example

from transformers import GPT2Tokenizer, GPT2LMHeadModel

```
tokenizer = GPT2Tokenizer.from_pretrained("tokenizer.model")
model = GPT2LMHeadModel.from_pretrained(".")
input_text = "what is a car?"
input_ids = tokenizer.encode(input_text, return_tensors="pt")
output = model.generate(input_ids, max_length=50, num_return_sequences=1, do_sample=True)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
print(generated_text)
```

# ref

https://huggingface.co/learn/nlp-course/chapter1/1

