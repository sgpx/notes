/*

implement thrust::transform_reduce to compute the dot product of two large vectors, utilizing nvprof to compare its speed against a standard kernel.

**Example Syntax**  

```cpp
#include <thrust/transform_reduce.h>
#include <thrust/sequence.h>
#include <iostream>

int main() {
    thrust::device_vector<int> d{3,1,4,1,5};               // input data
    int result = thrust::transform_reduce(                // reduce & output
        d.begin(), d.end(),                            // range
        [] __device__ (int x) { return x * x; },        // transform functor
        thrust::identity<int>(),                        // identity of reduction
        thrust::plus<int>());                           // reduction operator
    std::cout << "sum of squares = " << result << '\n';
}
```

*/

#include <cuda_runtime.h>
#include <iostream>
#include <thrust/transform_reduce.h>
#include <thrust/device_vector.h>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

__global__ void dot_product_kernel(const float* A, const float* B, float* partial, int N) {
	extern __shared__ float sdata[];

	unsigned int local = threadIdx.x;
	unsigned int tid = (blockIdx.x * blockDim.x) + local;

	sdata[local] = (tid < N) ? (A[tid] * B[tid]) : 0.0f;

	__syncthreads();

	for(unsigned int s = blockDim.x/2; s > 0 ; s >>= 1) {
		if(local < s) {
			sdata[local] += sdata[local + s];
		}
		__syncthreads();
	}

	if(local == 0) {
		partial[blockIdx.x] = sdata[0];
	}

}


int main() {
	int N = 2000000;
	int num_threads = 256;
	int num_blocks = GET_NUM_BLOCKS(N, num_threads);
	float *h_A, *h_B, *h_C, *d_A, *d_B, *d_C;
	h_A = (float*)malloc(sizeof(float)*N);
	h_B = (float*)malloc(sizeof(float)*N);
	h_C = (float*)malloc(sizeof(float)*N);
	cudaMalloc(&d_A, sizeof(float)*N);
	cudaMalloc(&d_B, sizeof(float)*N);
	cudaMalloc(&d_C, sizeof(float)*N);
	for(int i = 0; i < N; i++) {
		h_A[i] = 1.5f;
		h_B[i] = 3.2f;
		h_C[i] = 0.0f;
	}
	cudaMemcpy(d_A, h_A, sizeof(float)*N, cudaMemcpyHostToDevice);
	cudaMemcpy(d_B, h_B, sizeof(float)*N, cudaMemcpyHostToDevice);
	dot_product_kernel<<<num_blocks, num_threads, num_threads*sizeof(float)>>>(d_A, d_B, d_C, N);
	cudaDeviceSynchronize();
	float dot_kernel = thrust::reduce(
	    thrust::device_pointer_cast(d_C),
	    thrust::device_pointer_cast(d_C) + num_blocks,
	    0.0f,
	    thrust::plus<float>()
	);
	cudaMemcpy(h_C, d_C, sizeof(float)*num_blocks, cudaMemcpyDeviceToHost); // only num_blocks floats need to copied back since each block was reduce to 1 float
	thrust::device_vector<float> a(N);
	thrust::device_vector<float> b(N);
	thrust::fill(a.begin(), a.end(), 1.5f);
	thrust::fill(b.begin(), b.end(), 3.2f);
	auto z_1 = thrust::make_zip_iterator(thrust::make_tuple(a.begin(), b.begin()));
	auto z_2 = thrust::make_zip_iterator(thrust::make_tuple(a.end(), b.end()));
	float dot_thrust = thrust::transform_reduce(z_1, z_2, [] __device__ (thrust::tuple<float, float> t) { return thrust::get<0>(t) * thrust::get<1>(t) ; }, 0.0f, thrust::plus<float>() );
	std::cout << "dot_kernel: " << dot_kernel << std::endl;
	std::cout << "dot_thrust: " << dot_thrust << std::endl;
	cudaFree(d_A);
	cudaFree(d_B);
	cudaFree(d_C);
	free(h_A);
	free(h_B);
	free(h_C);
	return 0;
}

