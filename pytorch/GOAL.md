| Date          | Topic                        | Task                                                                                                                                                             |
|---------------|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Jan 25        | Custom Data Pipelines        | Refactor `a05.py`: Stop using `torchvision.datasets`. Write a custom `Dataset` class to load dummy images. Crucial for handling raw text later.                  |
| Jan 26        | The Embedding Layer          | Word2Vec (Simple): Create a model that takes a word index (e.g., `5`) and outputs a vector (`dim=16`). Train it to predict the *next* word. Visualize vectors.   |
| Jan 27        | Recurrent Neural Networks    | RNN from Scratch: Don't use `nn.RNN`. Write a manual loop: `h_t = tanh(W*x_t + U*h_{t-1})`. Train it to predict a sine wave.                                    |
| Jan 28        | The Vanishing Gradient       | Train your manual RNN on a long sequence. Observe how it fails to learn dependencies >10 steps away. This motivates Transformers.                                |
| Jan 29        | Attention (The Math)         | Dot Product Attention: Manual implementation. Take two vectors (Query, Key), dot product them, softmax, and multiply by Value. No training, just the math.      |
| Jan 30        | Positional Encoding          | Implement Sinusoidal Positional Encoding formula manually and add it to your Jan 26 embeddings.                                                                 |
| Jan 31        | Review                       | Clean up your repo. Create a `utils.py` for training loops to stop rewriting them.                                                                               |
| Feb 01        | Self-Attention Class         | Implement `ScaledDotProductAttention` as a `nn.Module`. Inputs: `Q, K, V`. Output: Weighted sum.                                                                |
| Feb 02        | Multi-Head Attention         | Split embeddings into `h` heads. Process in parallel. Concatenate. Allows the model to focus on different things simultaneously.                                |
| Feb 03        | LayerNorm & Residuals        | Implement "Add & Norm" block: `x + LayerNorm(Sublayer(x))`. Vital for deep networks.                                                                            |
| Feb 04        | Feed Forward Network         | The simple MLP inside every Transformer block: `Linear -> GELU -> Linear`.                                                                                      |
| Feb 05        | The Decoder Block            | Combine: `Masked Attn` -> `AddNorm` -> `FFN` -> `AddNorm`. Crucial: Implement the causal mask so it can't see the future.                                       |
| Feb 06        | NanoGPT (Assembly)           | Assemble: Embedding -> PosEncoding -> N Blocks -> Linear Head.                                                                                                  |
| Feb 07        | NanoGPT (Training)           | Train your model on "Tiny Shakespeare" (character level). Watch the loss drop.                                                                                  |
| Feb 08        | Tokenizers                   | Switch from char-level to BPE (Byte Pair Encoding) using `tiktoken` (OpenAI).                                                                                   |
| Feb 09        | Hugging Face 101             | Load `gpt2` from `transformers`. Compare its weights to your manual implementation.                                                                             |
| Feb 10        | Generation Strategies        | Implement `Temperature` and `Top-K` sampling in your generation loop.                                                                                           |
| Feb 11        | BERT (Encoder Only)          | Understand the difference between GPT (Decoder/Gen) and BERT (Encoder/Understanding). Implement "Masked LM" loss.                                               |
| Feb 12        | Vision Transformers          | Apply your exact Transformer code to image patches instead of text tokens.                                                                                      |
| Feb 13        | Fine-Tuning (LoRA)           | Use the `peft` library to fine-tune a pre-trained model without updating all weights.                                                                           |
| Feb 14-28     | Capstone Project             | Code Auto-Complete Bot: Fine-tune a small model (like TinyLlama) on your `*.py` files to mimic your coding style.                                               |

---
