# PyTorch/CUDA Topics to Master

## Core Tensor Operations

- [reading] Tensors and operations fundamentals
- [function] torch.tensor()
- [function] torch.zeros(), torch.ones(), torch.randn()
- [function] torch.reshape(), torch.view()
- [function] torch.transpose(), torch.permute()
- [function] torch.matmul(), torch.mm()
- [function] torch.sum(), torch.mean(), torch.std()
- [function] torch.argmax(), torch.argsort()
- [function] torch.cat(), torch.stack()

## Autograd & Gradients

- [reading] Backpropagation and automatic differentiation
- [class] torch.autograd.Function
- [function] tensor.backward()
- [function] torch.autograd.grad()
- [function] torch.no_grad()
- [function] tensor.detach()
- [function] torch.clamp(), torch.clip()

## Neural Network Layers

- [reading] Introduction to neural network layers
- [class] torch.nn.Linear
- [class] torch.nn.Conv2d
- [class] torch.nn.Conv1d
- [class] torch.nn.MaxPool2d
- [class] torch.nn.AvgPool2d
- [class] torch.nn.BatchNorm2d
- [class] torch.nn.BatchNorm1d
- [class] torch.nn.Dropout
- [class] torch.nn.ReLU
- [class] torch.nn.Sigmoid
- [class] torch.nn.Tanh
- [class] torch.nn.Softmax
- [class] torch.nn.LSTM
- [class] torch.nn.GRU
- [class] torch.nn.RNN

## Attention & Transformers

- [reading] Attention is All You Need (the transformer paper)
- [class] torch.nn.MultiheadAttention
- [class] torch.nn.TransformerEncoder
- [class] torch.nn.TransformerDecoder
- [function] torch.nn.functional.scaled_dot_product_attention

## Loss Functions

- [reading] Common loss functions and when to use them
- [class] torch.nn.MSELoss
- [class] torch.nn.CrossEntropyLoss
- [class] torch.nn.BCELoss
- [class] torch.nn.BCEWithLogitsLoss
- [class] torch.nn.L1Loss
- [class] torch.nn.SmoothL1Loss
- [class] torch.nn.KLDivLoss

## Optimizers

- [reading] Optimization algorithms (SGD, Adam, etc.)
- [class] torch.optim.SGD
- [class] torch.optim.Adam
- [class] torch.optim.AdamW
- [class] torch.optim.RMSprop
- [function] optimizer.step()
- [function] optimizer.zero_grad()
- [function] optimizer.param_groups

## Learning Rate Scheduling

- [reading] Learning rate schedules and warmup
- [class] torch.optim.lr_scheduler.StepLR
- [class] torch.optim.lr_scheduler.CosineAnnealingLR
- [class] torch.optim.lr_scheduler.LinearLR
- [class] torch.optim.lr_scheduler.ExponentialLR
- [function] scheduler.step()

## Data Loading

- [reading] Efficient data loading and batching
- [class] torch.utils.data.Dataset
- [class] torch.utils.data.DataLoader
- [function] DataLoader parameters (batch_size, shuffle, num_workers)
- [class] torch.utils.data.Sampler
- [class] torch.utils.data.DistributedSampler

## Model Building & Training

- [reading] Building and training neural networks
- [class] torch.nn.Module
- [function] model.forward()
- [function] model.train()
- [function] model.eval()
- [function] model.parameters()
- [function] torch.nn.utils.clip_grad_norm_()

## GPU & CUDA

- [reading] CUDA fundamentals and GPU programming
- [function] tensor.to('cuda')
- [function] tensor.cuda()
- [function] torch.cuda.is_available()
- [function] torch.cuda.device_count()
- [function] torch.cuda.synchronize()
- [function] torch.cuda.reset_peak_memory_stats()
- [function] torch.cuda.empty_cache()

## Mixed Precision Training

- [reading] Automatic mixed precision (AMP) and why it matters
- [class] torch.cuda.amp.autocast
- [class] torch.cuda.amp.GradScaler
- [function] scaler.scale()
- [function] scaler.step()
- [function] scaler.update()

## Model Saving & Loading

- [reading] Checkpointing and model persistence
- [function] torch.save()
- [function] torch.load()
- [function] model.state_dict()
- [function] model.load_state_dict()

## Distributed Training

- [reading] Distributed data parallel and multi-GPU training
- [class] torch.nn.DataParallel
- [class] torch.nn.parallel.DistributedDataParallel
- [function] torch.distributed.init_process_group()
- [function] torch.distributed.barrier()

## Quantization & Optimization

- [reading] Model quantization and inference optimization
- [function] torch.quantization.quantize_dynamic()
- [function] torch.quantization.prepare()
- [function] torch.quantization.convert()
- [class] torch.quantization.QConfig

## Model Export

- [reading] Exporting models for production
- [function] torch.onnx.export()
- [function] torch.jit.script()
- [function] torch.jit.trace()

## Functional API

- [reading] torch.nn.functional (F) module for flexibility
- [function] torch.nn.functional.conv2d()
- [function] torch.nn.functional.linear()
- [function] torch.nn.functional.relu()
- [function] torch.nn.functional.softmax()
- [function] torch.nn.functional.dropout()
- [function] torch.nn.functional.batch_norm()
- [function] torch.nn.functional.embedding()
- [function] torch.nn.functional.pad()

## Advanced Topics

- [reading] Custom autograd functions and debugging
- [reading] Memory efficient training techniques
- [reading] Profiling and benchmarking PyTorch code
- [function] torch.profiler.profile()
- [function] torch.utils.checkpoint.checkpoint()
- [class] torch.jit.ScriptModule
- [function] torch.compile() (PyTorch 2.0+)

---

**Start here:** Master the first 3 sections (tensor ops, autograd, basic layers). Then pick a project and learn the rest by using them.
