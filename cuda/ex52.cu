// use parallel sum reduction to add 1,000,000 integers

#include <iostream>
#include <cuda_runtime.h>

typedef unsigned long long ull;
const int ULLSIZE = sizeof(ull);

__global__ void parallel_sum(ull *d_A, ull *d_res, int N) {
	extern __shared__ ull sdata[];
	int local = threadIdx.x;
	int tid = (blockDim.x * blockIdx.x) + local;
	sdata[local] = tid < N ? d_A[tid] : 0;
	__syncthreads();

	for(int s = blockDim.x/2; s > 0; s >>= 1)  {
		if(local < s) {
			sdata[local] += sdata[local + s];
		}
		__syncthreads();
	}
	if(local == 0) { atomicAdd(d_res, sdata[0]); }
}

int main() {
	int N = 1000000;
	int deviceCount = 0;
	int num_threads = 256;
	int num_blocks = (N + num_threads - 1) / num_threads;
	cudaGetDeviceCount(&deviceCount);
	std::cout << "Device count at start: " << deviceCount << std::endl;
	ull bytes = ULLSIZE*N ;
	ull *h_A = (ull*)malloc(bytes);
	ull *h_res = (ull*)malloc(ULLSIZE);
	for(ull i = 0; i < N; i++) {
		h_A[i] = 5 ; //std::rand() % 100;
	}	

	ull cpu_sum = 0;
	for (ull i = 0; i < N; i++) {
		h_A[i] = 5;
		cpu_sum += h_A[i];
	}

	std::cout << "CPU result: " << cpu_sum << std::endl;

	ull *d_A, *d_res;
	cudaMalloc(&d_A, bytes);
	cudaMalloc(&d_res, ULLSIZE);
	cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice);
	cudaMemset(d_res, 0, ULLSIZE);
	parallel_sum<<<num_blocks, num_threads, ULLSIZE*num_threads>>>(d_A, d_res, N);
	cudaDeviceSynchronize();

	cudaMemcpy(h_res, d_res, sizeof(ull), cudaMemcpyDeviceToHost);
	std::cout << "Result : " << *h_res << std::endl;
	cudaFree(d_A);
	cudaFree(d_res);
	free(h_A);
	free(h_res);

	return 0;
}

/*

==5887== NVPROF is profiling process 5887, command: ./a.out
Device count at start: 1
CPU result: 5000000
Result : 5000000
==5887== Profiling application: ./a.out
==5887== Profiling result:
            Type  Time(%)      Time     Calls       Avg       Min       Max  Name
 GPU activities:   95.01%  1.5489ms         1  1.5489ms  1.5489ms  1.5489ms  [CUDA memcpy HtoD]
                    4.82%  78.558us         1  78.558us  78.558us  78.558us  parallel_sum(__int64*, __int64*, int)
                    0.13%  2.1120us         1  2.1120us  2.1120us  2.1120us  [CUDA memcpy DtoH]
                    0.04%     640ns         1     640ns     640ns     640ns  [CUDA memset]
      API calls:   96.58%  173.71ms         2  86.857ms  75.295us  173.64ms  cudaMalloc
                    1.47%  2.6483ms       114  23.230us      86ns  1.4694ms  cuDeviceGetAttribute
                    0.98%  1.7714ms         2  885.71us  32.775us  1.7386ms  cudaMemcpy
                    0.63%  1.1301ms         1  1.1301ms  1.1301ms  1.1301ms  cudaLaunchKernel
                    0.27%  483.91us         2  241.96us  119.96us  363.96us  cudaFree
                    0.04%  79.206us         1  79.206us  79.206us  79.206us  cudaDeviceSynchronize
                    0.01%  12.756us         1  12.756us  12.756us  12.756us  cuDeviceGetName
                    0.01%  10.792us         1  10.792us  10.792us  10.792us  cudaMemset
                    0.00%  5.7300us         2  2.8650us     162ns  5.5680us  cuDeviceGet
                    0.00%  3.5470us         1  3.5470us  3.5470us  3.5470us  cuDeviceGetPCIBusId
                    0.00%  1.1540us         3     384ns     119ns     862ns  cuDeviceGetCount
                    0.00%     696ns         1     696ns     696ns     696ns  cudaGetDeviceCount
                    0.00%     669ns         1     669ns     669ns     669ns  cuDeviceTotalMem
                    0.00%     559ns         1     559ns     559ns     559ns  cuModuleGetLoadingMode
                    0.00%     488ns         1     488ns     488ns     488ns  cuDeviceGetUuid

*/
