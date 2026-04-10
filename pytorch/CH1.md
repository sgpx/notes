To generate **PyTorch learning tasks for a ___ reward** for the "torch test repo" *based on your learning history*, let's identify the **scope and progression** in your files:

## **Your Learning History Based on Source Files**
- **Basic tensor operations and manipulation** (`ex01.py`, `ex02.py`, `ex03.py`, ...): addition, reshaping, transposing, indexing, datatype, mean/std, etc.
- **Device handling** (CPU, GPU, Metal) (`ex04.py`, `ex19.py`)
- **Simple neural networks** (`a02.py`, `ex29.py`, `ex30.py`, `ex32.py`, `ex33.py`): building, forward pass, loss calculation, training loop
- **Gradient Descent by hand** (`a04.py`, `a03.py`)
- **Case studies with real/dummy datasets** (Iris, synthetic data, `ex35.py`)
- **Model saving/loading** (`ex27.py`, `ex28.py`)
- **Visualization / Model graph** (`ex31.py`, plotting in regression)
- **Torch Dataset, DataLoader** (`ex35.py`)
- **Some small mistakes in code - giving room for improvements**
- **No custom layer, advanced autograd, or debugging tasks yet**

---

## **Tasks for Claiming a ___ Reward**

Below are tasks with a learning and deliverables focus, that **fit your history while helping you progress**, are concrete and can be considered worthy of a small reward (especially for someone at your current level).

---

### **Foundational Model & Data Tasks**

1. **Fix a bug and train a small neural network on a real dataset**
   - Fix the bug in `ex32.py` (uninitialized `loss` before `loss = ...`)
   - Train successfully on random (or toy) data and print initial and final loss.
   - **Deliverable**: Fixed script, *before/after loss printout*, screenshot, and explanation of the bug.

2. **Implement training and evaluation splits**
   - For an existing demo (e.g., the Iris dataset in `ex30.py`), split the dataset into train/test parts.
   - Train on the train set, then evaluate and print accuracy on the test set (not just on the train data).
   - **Deliverable**: Code + screenshots of test/train accuracy.

---

### **Deeper PyTorch Work**

3. **Write a custom activation function**  
   - Create a new `nn.Module` for a custom activation (e.g., Swish, LeakyReLU with custom slope).
   - Integrate it in a copy of a simple network (like from `ex30.py` or `ex33.py`), train, and compare its loss curve to the vanilla ReLU.
   - **Deliverable**: Code for the custom activation, plot/loss comparison, short writeup.

4. **Add support for training on GPU**  
   - Update one of your demos (e.g., `ex30.py` or `ex35.py`) to auto-detect and run on GPU (CUDA/MPS) if available, fallback to CPU if not.
   - Print which device is being used. Time the training loop (before/after in seconds) for both CPU and GPU (if you have them).
   - **Deliverable**: Updated script, screenshot of output on your machine.

---

### **Model Saving/Loading**

5. **Train a model, save it, load it, and use it for inference**  
   - For a simple regression or classification task, train a model, save its state dict, load it in a fresh script, and use it to predict on new data.
   - **Deliverable**: Code for save/load, output showing saved/loaded model works.

---

### **Bonus: Visualization/Autograd**

6. **Visualize computational graph of a custom function**
   - Like in `ex31.py`, for a function you define (not just a trivial polynomial, maybe use small neural network output), use `torchviz.make_dot`.
   - **Deliverable**: Generated graph image, the python code/jupyter notebook producing it.

---

## **Why These Tasks?**

- They **bridge what you've already done** and take you to the next step (customization, debugging, device management, best practices).
- **Useful in “real work”/portfolio/learning**: not just "toy" but with some depth.
- **Require non-trivial effort** (debugging, researching custom activation, devices).
- Each task is **self-contained**, show-casable, easy to verify for a mentor.
- Collectively, these are a solid "next learning milestone" for ___ in a course/summer intern setting.

---

## **How to Claim? Sample Format**
For each task, submit:
- The new/modified script(s)
- Output snippets/screenshots
- Short explanation of what you did and what you learned (2-3 sentences each)

---

## **Summary Table**

| Task # | Task                                                                                                    | Deliverable                                            |
|--------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------|
|   1    | Fix & train simple NN (`ex32.py` bug), report loss before/after                                        | Code, screenshots, explanation                         |
|   2    | Train-test split on Iris or dummy, eval accuracy on both                                               | Code + outputs                                         |
|   3    | Implement and use a custom activation                                                                  | Code, comparison chart, description                    |
|   4    | Move code to GPU if available, print training time                                                     | Code, output screenshot                                |
|   5    | Save/load PyTorch model, show inference                                                                | Code, output                                           |
|   6    | Visualize computational graph for your own function/model                                              | Code, generated image                                  |


---

If you submit any **3-4 of these** well, it **justifies a ___ reward** at your learning stage.  
Let me know if you want step-by-steps or solution code for any!
