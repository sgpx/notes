~~Problem 1 — Your first tensor and some basic operations~~
Goal: Create a tensor, inspect its properties, and do a few simple operations.
What to do
- Create a 3x2 tensor with numbers 1 through 6.
- Print its shape, dtype, and device.
- Multiply the tensor by 2, sum all elements, and take the maximum value.
Hints
- Use torch.arange and .reshape or .view to shape it.
- Use .shape, .dtype, and .device to inspect.
What to submit
- The printed shape, dtype, device, the result of the sum, and the max value.

~~Problem 2 — Autograd: simple gradients~~
Goal: Learn how PyTorch computes gradients with autograd.
What to do
- Create a tensor x with requires_grad=True, for example x = torch.tensor([1.0, -2.0, 3.0], requires_grad=True).
- Define y = x.pow(2) + 3*x (element-wise operations).
- Compute a scalar loss as y.sum(), then call loss.backward().
- Print x.grad to see dy/dx for each element.
Hints
- Remember to call .sum() before backward so you have a scalar loss.
- Gradients are for dy/dx w.r.t x.
What to submit
- The values in x.grad.

~~Problem 3 — Clearing gradients and a tiny function~~
Goal: Practice reusing gradients by zeroing and computing again.
What to do
- Use the same x from Problem 2 (or redefine it) with requires_grad=True.
- Define z = x * x + 2*x + 1, and compute loss_z = z.sum(), then backward and print x.grad.
- Now reset gradients with x.grad.zero_(), redefine z2 = x * x * x (x cubed) and compute loss_z2 = z2.sum(), backward, and print x.grad again.
Hints
- You can reuse the same x or redefine; zeroing is important if you want to do multiple backward passes in one run.
What to submit
- Gradients after the first backward pass, and after the second backward pass (separate prints).

~~Problem 4 — A tiny linear regression by hand (no nn.Module)~~
Goal: Do a simple learning task with manual parameters using autograd.
What to do
- Create a tiny dataset X of shape (3, 2) and y of shape (3,).
  Example:
  X = [[1.0, 2.0],
       [2.0, 0.5],
       [3.0, 1.0]]
  y = [5.0, 4.0, 6.0]
- Initialize W with shape (2,) and b with shape (1,), both with requires_grad=True.
- Forward: y_hat = X.matmul(W) + b
- Loss: mean squared error between y_hat and y
- Backprop: loss.backward()
- Update: with torch.no_grad(), do W -= lr * W.grad and b -= lr * b.grad, then zero the gradients.
- Repeat for a few iterations (e.g., 50) with a small learning rate (e.g., 0.01).
Hints
- Use X.matmul(W) for matrix-vector multiplication; shapes matter.
- After updating, call W.grad.zero_() and b.grad.zero_().
What to submit
- Final loss after training and the learned W and b values.

Problem 5 — Mini-batch training with DataLoader
Goal: Learn how to use a DataLoader to feed data in batches.
What to do
- Create a small dataset (8 samples) for a simple linear problem:
  X and y as in Problem 4 but with more samples, e.g. a simple linear relation y = 1.5*x0 + -2.0*x1 + 0.5
- Use torch.utils.data.TensorDataset and torch.utils.data.DataLoader with batch_size=2.
- Use the same manual update rule as Problem 4, but update parameters after each batch.
- Train for a few epochs (e.g., 3) and print the loss every epoch.
Hints
- Build dataset like: dataset = TensorDataset(X, y); loader = DataLoader(dataset, batch_size=2, shuffle=True)
- In the batch loop, compute loss on the batch, backward, and update.
What to submit
- The loss printed after each epoch and a couple of example predicted vs. true values.

Problem 6 — Build a tiny two-layer network by hand
Goal: Implement a small neural network with one hidden layer without using nn.Module.
What to do
- Create a network that maps input features of size 2 to a hidden layer of size 3, then to a single output.
- Parameters required: W1 (2x3), b1 (3,), W2 (3x1), b2 (1,), all with requires_grad=True.
- Define forward: hidden = ReLU(X @ W1 + b1); y_hat = hidden @ W2 + b2
- Use MSE loss on a small dataset (like Problem 4) and train with SGD (as in previous problems).
- Train for a few hundred steps and print final loss.
Hints
- Implement ReLU as torch.clamp or max(0, x) element-wise.
- Use with torch.no_grad() for parameter updates.
What to submit
- Final loss and the learned parameters W1, b1, W2, b2.

Problem 7 — A small network using nn.Module and nn.Sequential
Goal: Learn to use PyTorch’s higher-level APIs.
What to do
- Define a network using torch.nn.Sequential: a hidden layer with 4 units, ReLU, and an output layer of size 1.
- Create a tiny dataset (as in Problem 4 or 5) and use a DataLoader.
- Use an optimizer (e.g., torch.optim.SGD) and a loss function (nn.MSELoss).
- Train for a few epochs; print the loss every epoch.
Hints
- Example skeleton: net = nn.Sequential(nn.Linear(2, 4), nn.ReLU(), nn.Linear(4, 1))
- Use loss_fn = nn.MSELoss() and optimizer = torch.optim.SGD(net.parameters(), lr=0.01)
What to submit
- Final loss and the network’s parameters after training.

Problem 8 — Saving and loading a model
Goal: Persist a trained model and load it back.
What to do
- Train a small model as in Problem 7 or 6 for a couple of epochs.
- Save its state_dict to a file (e.g., "model.pth").
- Create a new instance of the same model class or a matching nn.Sequential, and load the state_dict.
- Do a quick forward pass with new input to verify it works.
Hints
- Use torch.save(model.state_dict(), "model.pth") and model.load_state_dict(torch.load("model.pth"))
What to submit
- The saved file name and a short snippet showing the loaded model producing an output.

Problem 9 — Move to device when available
Goal: Learn how to use CUDA if available and fall back to CPU otherwise.
What to do
- Check if CUDA is available: device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
- Move your model and a batch of data to that device and perform a forward pass.
- Print the device being used and ensure the outputs are on the same device.
Hints
- Use parameters like: model.to(device); inputs = inputs.to(device); outputs = model(inputs)
What to submit
- The device chosen (string) and a short snippet showing a forward pass on that device.



Nice repo — you already have lots of good building blocks (small MLP examples, CIFAR conv net, text pipeline, many tensor-shape examples). Here are three concrete PyTorch projects you can complete this week, each tied to files already in the repo and with a short plan, milestones, and success criteria.

Project 1 — Build a reliable CIFAR10 training pipeline (improve a05.py)
- Why: a05.py already contains a full ConvNet and dataloaders; finishing it gives you hands-on experience with GPU/MPS training, checkpointing, metrics and augmentation.
- Goals
  - Fix/improve device handling and training loop robustness (use torch.device everywhere, avoid passing device as string).
  - Add proper train/validation loops, early stopping or best-checkpoint saving, learning-rate scheduler, and TensorBoard logging.
  - Make training reproducible (seed + deterministic flags) and add simple CLI args for epochs / batch-size.
- Steps (suggested)
  1. Convert device_id = "mps" to actual device objects (torch.device).
  2. Add model.train()/model.eval() correctly and separate train/validate loops (per-epoch validation accuracy).
  3. Save best checkpoint (torch.save dict with epoch/state_dict/optimizer).
  4. Add torchvision augmentations already partly present; try more (Cutout/RandomErasing optional).
  5. Add TensorBoard or simple CSV logging for losses/accuracy.
  6. Run smaller number of epochs locally, verify training works on CPU and MPS.
- Files to edit: a05.py
- Time estimate: 2–3 days
- Success criteria: training runs end-to-end, checkpoint is saved, validation accuracy is logged and improves; reproducible short run works on your machine.

Project 2 — End-to-end text classifier with inference CLI (finish and harden ex38_train.py + ex39_infer.py)
- Why: you already have a nearly complete pipeline connecting Mongo + CountVectorizer, training, saving artifacts, and an inference script. Finish it into a robust E2E example you can reuse.
- Goals
  - Make training script robust and runnable without Mongo (support local CSV fallback or small demo dataset).
  - Fix any missing imports (os is referenced but not imported), add argument parsing for paths / vocab size / epochs.
  - Improve preprocessing (optionally swap CountVectorizer → TfidfVectorizer or a simple tokenizer), add class weighting if imbalance, and produce a saved model + vectorizer.
  - Create an inference CLI (ex39_infer.py) that loads vectorizer and model, exposes a function and simple CLI to classify a text sample.
  - Add unit tests or simple example inputs and an example saved artifact.
- Steps
  1. Add import os and guard the Mongo section with a flag — allow loading a sample CSV for quick testing.
  2. Wrap training loop in main() and add argparse for MODEL_SAVE_PATH, VECTORIZER_SAVE_PATH, EPOCHS.
  3. Add validation metrics (precision/recall) and print per-epoch.
  4. Implement ex39_infer.py CLI that reads a sample text from stdin or file and prints predicted label + confidences.
- Files to edit: ex38_train.py, ex39_infer.py (and add small demo data)
- Time estimate: 2–3 days
- Success criteria: you can train locally with demo data producing product_classifier.pth and vectorizer.pkl, and run the inference script to classify text.

Project 3 — Tensor-shape cookbook + small model workbook (convert many exN to a learning notebook)
- Why: the repo has many small files demonstrating view/reshape/squeeze/flatten/permute. Package these into a single learning notebook or test suite so you internalize tensor manipulation and layer usage.
- Goals
  - Create a Jupyter notebook "tensor_recipes.ipynb" that groups examples: unsqueeze/squeeze, view/reshape, transpose/permute, flatten, indexing and broadcasting, device/dtypes.
  - For each concept add a short explanation, runnable examples (pull code from ex* files), and one or two short exercises with expected answers.
  - Add a second section: quick model recipes. Re-use ex30 (Iris), ex35 (SmallNet training on synthetic data) and ex53/ex55 (regression / function approximation) — make them small, reproducible, and runnable in the notebook.
  - Add a final short demo: TorchScript export of a small trained model and reload for inference.
- Steps
  1. Collect representative example files (ex92, ex152, ex129, ex35, ex53, ex55, ex30).
  2. Create the notebook with sections and runnable cells.
  3. Add small unit tests (assert tensor shapes) or exercises where readers fill in missing operations.
  4. Add a cell to export a trained SmallNet to TorchScript and run it.
- Files to use: many exNN.py files (pick ~10 representative ones). Create new notebook and small data files if needed.
- Time estimate: 1–2 days
- Success criteria: notebook runs start-to-finish on your machine, exercises check shapes automatically, and TorchScript export/load works.

Priorities / schedule suggestion for one week
- Day 1–2: Project 1 (CIFAR pipeline) — get a working end-to-end training run and checkpointing.
- Day 3–4: Project 2 (Text classifier) — complete training & inference CLI, ensure fallback demo data works.
- Day 5–7: Project 3 (Notebook + small models) — consolidate learning, add TorchScript export.

Stretch goals (if you finish early)
- Convert CIFAR training to PyTorch Lightning for cleaner code and easier experimentation.
- Add unit tests for tensor-shape exercises (use pytest).
- Experiment with mixed precision (torch.cuda.amp) or use bfloat16 on MPS for speed/testing.
- Dockerize an inference script and show a minimal REST API (Flask/FastAPI) serving the text classifier.

If you want, I can:
- produce a checklist and starter patch for a05.py (device fixes + checkpoint saving), or
- create the inference CLI template for ex39_infer.py, or
- assemble the tensor-shape notebook with the selected examples.

Which of the three do you want to start with?
