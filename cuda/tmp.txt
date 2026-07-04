This problem is designed for a beginner learning CUDA C++ that needs to understand how to query the physical properties of the GPU hardware.

## 💡 The Learning Problem: GPU Information Retrieval

**Goal:** Write a CUDA C++ program that successfully queries and prints the name and total memory of the first available NVIDIA GPU device on the system using the `cudaGetDeviceProperties` function.

---

### 🎯 Problem Statement

You are tasked with writing a simple CUDA application that identifies the key physical characteristics of your graphics card. You must use the `cudaGetDeviceProperties` function to retrieve the device's name and total memory.

### 🛠️ Required Steps

1. **Initialization:** Initialize the CUDA runtime environment.
2. **Device Count:** Determine how many CUDA devices are available.
3. **Selection:** Select the index of the first GPU device (index 0).
4. **Query:** Call `cudaGetDeviceProperties` using the selected index.
5. **Extraction & Output:** Extract the device name and total memory from the returned properties and print them to the console in a clear, readable format.
6. **Error Handling:** Include basic error checking to ensure the function calls succeed.

### 💻 Starter Code Skeleton

```cpp
#include <iostream>
#include <cuda_runtime.h>

int main() {
    // 1. Check for CUDA errors immediately
    cudaError_t err = cudaGetLastError();
    if (err != cudaSuccess) {
        std::cerr << "CUDA initialization failed: " << cudaGetErrorString(err) << std::endl;
        return 1;
    }

    // 2. Get the number of devices
    int deviceCount = 0;
    cudaGetDeviceCount(&deviceCount);

    if (deviceCount == 0) {
        std::cerr << "Error: No CUDA devices found!" << std::endl;
        return 1;
    }

    // 3. Select the first device
    int deviceId = 0;

    // 4. Declare the properties structure
    cudaDeviceProp deviceProp;

    // 5. Call cudaGetDeviceProperties
    cudaError_t errGetProps = cudaGetDeviceProperties(&deviceProp, deviceId);

    if (errGetProps != cudaSuccess) {
        std::cerr << "Error getting device properties for device " << deviceId << ": " << cudaGetErrorString(errGetProps) << std::endl;
        return 1;
    }

    // 6. Extract and Print the required information
    std::cout << "===========================================" << std::endl;
    std::cout << "Successfully queried device properties." << std::endl;
    std::cout << "-------------------------------------------" << std::endl;
    
    // Access the data using the properties struct members
    std::cout << "Device Index: " << deviceId << std::endl;
    std::cout << "Device Name: " << deviceProp.name << std::endl;
    std::cout << "Total Memory (Bytes): " << deviceProp.totalMemory << std::endl;
    std::cout << "===========================================" << std::endl;

    return 0;
}
```

### ✅ Expected Output Example

(The actual output will depend on your specific hardware.)

```
===========================================
Successfully queried device properties.
-------------------------------------------
Device Index: 0
Device Name: NVIDIA GeForce RTX 4090
Total Memory (Bytes): 24576000000
===========================================
```

### 🧠 Learning Takeaways

1. **Device Enumeration:** You learn the standard way to figure out how many GPUs are present using `cudaGetDeviceCount`.
2. **Property Structure:** You understand that complex hardware data is returned in a structured format (`cudaDeviceProp`) rather than simple raw pointers.
3. **Error Checking is Crucial:** You learn the necessity of checking the `cudaError_t` return value after *every* CUDA API call to ensure the operation was successful.
4. **Hardware Interaction:** This is the foundational step for any application that needs to manage or identify specific hardware resources in CUDA.
