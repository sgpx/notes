# llama.cpp

```
git clone https://github.com/ggeorganov/llama.cpp
cd llama.cpp
make -j6
```

# issues

warmup with two tokens in `common/common.cpp`:

https://github.com/ggerganov/llama.cpp/issues/3058

`const std::vector<llama_token> tmp = { llama_token_bos(lctx), llama_token_eos(lctx), }; `

# ggml gguf convert

```
pip3 install -r requirements.txt
python3 convert-llama-ggml-to-gguf.py --input old.bin --output new.bin
```

# ggml-metal.m `Abort Trap 6` q6 not supported on Metal

https://github.com/ggerganov/llama.cpp/issues/1697


