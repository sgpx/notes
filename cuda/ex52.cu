#include <iostream>
#include <cuda_runtime.h>

int main() {
    int deviceCount = 0;
    cudaGetDeviceCount(&deviceCount);
    std::cout << "Device count at start: " << deviceCount << std::endl;
    
    // Add your code here one piece at a time
    
    return 0;
}
