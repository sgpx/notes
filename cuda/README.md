## CUDA

# grids, threads, warps, kernel, group, etc

A kernel is the program.

A grid is the whole set of workers running that program.

A block is one team (subset of the grid).

A warp is a mini-squad inside a block.

A thread is one individual worker.

### What is the purpose of cudaEventCreate in CUDA, and why must an event be created before you record or synchronize on it?

cuda events work like a stopwatch. they record events happening on the GPU and are used to measure elapsed time between events

| Step | What We Do | Why |
|------|-----------|-----|
| **Create** | `cudaEventCreate(&event)` | Build the stopwatch/checkpoint |
| **Record** | `cudaEventRecord(event)` | Mark a moment in time on the GPU |
| **Synchronize** | `cudaEventSynchronize(event)` | Make the CPU wait until that moment arrives |
| **Measure** | `cudaEventElapsedTime()` | Calculate time between two events |
| **Destroy** | `cudaEventDestroy(event)` | Clean up and free memory |


### Q: In CUDA, what does atomicInc do to the value at a given address, and how does its "limit" parameter affect when the value wraps?

**A:** atomicInc(addr, limit) is a thread safe increment operation that behaves like a (*addr) = (*addr >= limit) ? 0 : (*addr + 1)

it is used to increment numbers stored in memory upto a specificed limit when many threads are trying to access it at the same time

> Mostly correct. atomicInc atomically increments the 32-bit value at address and wraps it to 0 when the current value is >= limit (so the allowed values cycle 0..limit). Two missing/details: (1) it returns the old value (so full semantics are: old = *addr; *addr = (old >= limit) ? 0 : old + 1; return old;), and (2) it operates on unsigned 32-bit values. Mentioning those makes the answer complete.

---

### Q: What does the cudaMemcpyHostToDevice flag indicate, and why would you use it when transferring data in a CUDA program?

**A:** it indicates the direction of the data transfer in cudaMemcpy or cudaMemcpyAsync, telling the computer that the data needs to be transferred from the CPU to the GPU

---

### Q: What does the CUDA intrinsic __logf compute, and how does it differ from the standard logf in terms of precision and performance?

**A:** __logf is a primitive natural logarithm calculation function in CUDA that maps directly to GPU directives. it is not IEEE754 compliant unlike logf. it is used in contexts where slight losses can be tolerated in favor of high calculation speeds.

> Mostly correct. __logf is a CUDA single-precision (float) intrinsic that computes the natural logarithm using a fast, lower-precision approximation (often implemented as a device/hardware intrinsic) and is intended for speed over strict IEEE-754 accuracy. Improvements: explicitly say it is for float, note that error bounds and special-case handling (NaN/Inf, denormals, rounding) can differ from the standard logf and can vary by GPU/compute capability, and recommend consulting the CUDA docs or using the full-precision logf when IEEE-compliant results are required.

---

### Q: In CUDA, what does the `__global__` qualifier indicate about a function’s execution location and how it is launched from the host, and how does that differ from a `__device__` function?

**A:** the `__global__` keyword indicates the function is executed on the GPU

it is invoked using the triple angle bracket syntax mykernel<<<grid, block>>>(args);

it differs from the device function in the sense that it is an entry point called from the CPU and can only return void

whereas `__device__` functions can only be called by other device functions or global functions, but not from the host. unlike global functions, device functions can return values

> Your answer is essentially correct: global marks a kernel that executes on the GPU and is launched from host code with the <<<grid, block>>> launch syntax (you can also supply optional shared-mem and stream parameters: <<<grid, block, sharedMem, stream>>>). global kernels are host-callable entry points and must have void return type. device functions run on the device and can only be called from device-side code (other device or global functions) and may return values. Minor caveats you might mention: with CUDA dynamic parallelism a device can launch global kernels (on capable hardware), and functions can be annotated host device to be callable from both sides.

---

### Q: In CUDA, what is make_int3 and what purpose does it serve compared to simply using an int3 type directly?

**A:** make_int3 is a helper function that creates a three dimensional integer vector

we can also use the int3 data type directly like `int3 foo; foo.x = 1;` but make_int3 improves readability

> Partially correct. make_int3 is a small helper/constructor function that returns an int3 with its x,y,z components set (e.g. make_int3(1,2,3)). It’s more than just "readability": it provides a concise, safe way to initialize all components at once (and is often used for portability/compatibility in device/host code) versus manually assigning members one-by-one. You could also use aggregate initialization (int3 a = {1,2,3}) in many contexts, but make_int3 is the idiomatic convenience function in CUDA.

---

