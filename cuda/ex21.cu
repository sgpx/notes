#include <cuda_runtime.h>
#include <iostream>
#define NUM_THREADS 256
#define SZ sizeof(int)

using namespace std;

__global__ void dostuff(int * d_A, int N) {
	extern __shared__ int sdata[];
	int idx = threadIdx.x + (blockIdx.x * blockDim.x);
	if(idx < N) {
		sdata[threadIdx.x] = d_A[idx];
	}
	else {
		sdata[threadIdx.x] = 0;
	}
	printf("Compilation test 1 %d %d", threadIdx.x, blockIdx.x);
	int ct = (threadIdx.x + (blockIdx.x * 256)) % N;
	printf("%d", d_A[ct]);
}

int main() {
	int N = 50000;
	int *h_A = (int*)malloc(N*SZ);
	int *d_A;
	cudaMalloc(&d_A, SZ*N);
	for(int i = 0; i < N ; i++) h_A[i] = i % 10;
	cudaMemcpy(d_A, h_A, N*SZ, cudaMemcpyHostToDevice);
	int num_blocks = (N + NUM_THREADS - 1) / NUM_THREADS;
	dostuff<<<num_blocks,256>>>(d_A, N);
	cudaMemcpy(h_A, d_A, SZ*N, cudaMemcpyDeviceToHost);
	for(int i = 0; i < N ; i++ ){ 
		// std::cout << h_A[i] << std::endl 
	};
	free(h_A);
	cudaFree(d_A);
	return 0;
}


/*

Collecting data...
Generating '/tmp/nsys-report-5e74.qdstrm'
[1/8] [========================100%] report3.nsys-rep
[2/8] [========================100%] report3.sqlite
[3/8] Executing 'nvtx_sum' stats report
SKIPPED: /content/report3.sqlite does not contain NV Tools Extension (NVTX) data.
[4/8] Executing 'osrt_sum' stats report

 Time (%)  Total Time (ns)  Num Calls    Avg (ns)      Med (ns)     Min (ns)    Max (ns)    StdDev (ns)            Name         
 --------  ---------------  ---------  ------------  ------------  ----------  -----------  ------------  ----------------------
     73.8    1,830,178,775         29  63,109,612.9  68,705,793.0       1,395  305,568,187  65,982,495.1  poll                  
     24.1      598,925,617        511   1,172,065.8      15,132.0       1,182  359,184,926  16,047,367.1  ioctl                 
      1.9       47,095,963          1  47,095,963.0  47,095,963.0  47,095,963   47,095,963           0.0  pthread_mutex_lock    
      0.1        1,787,178         29      61,626.8       9,917.0       6,196    1,274,781     233,853.2  mmap64                
      0.1        1,362,123         11     123,829.4      65,139.0      32,268      444,960     137,460.1  sem_timedwait         
      0.0          402,294         47       8,559.4       7,686.0       3,000       23,607       3,915.5  open64                
      0.0          205,793         36       5,716.5       3,771.0       1,378       24,774       5,317.3  fopen                 
      0.0          192,866         16      12,054.1       8,785.0       2,301       62,105      14,107.6  mmap                  
      0.0          151,975         14      10,855.4       5,725.0       1,828       40,681      10,735.1  write                 
      0.0          125,353          2      62,676.5      62,676.5      58,193       67,160       6,340.6  pthread_create        
      0.0           89,262          1      89,262.0      89,262.0      89,262       89,262           0.0  pthread_cond_wait     
      0.0           42,836          5       8,567.2       8,615.0       2,155       13,440       4,625.9  munmap                
      0.0           40,292         20       2,014.6       1,722.0       1,001        5,298       1,090.9  fclose                
      0.0           34,512          1      34,512.0      34,512.0      34,512       34,512           0.0  fgets                 
      0.0           30,277          6       5,046.2       5,236.5       1,506        7,356       1,943.1  open                  
      0.0           27,082         17       1,593.1       1,399.0       1,118        3,042         514.3  read                  
      0.0           22,240          1      22,240.0      22,240.0      22,240       22,240           0.0  connect               
      0.0           21,249          2      10,624.5      10,624.5       7,604       13,645       4,271.6  socket                
      0.0           19,143          1      19,143.0      19,143.0      19,143       19,143           0.0  pthread_cond_broadcast
      0.0           18,742          8       2,342.8       2,045.0       1,018        5,447       1,427.3  close                 
      0.0           16,477          3       5,492.3       6,157.0       2,545        7,775       2,677.6  pipe2                 
      0.0            4,592          2       2,296.0       2,296.0       2,179        2,413         165.5  fwrite                
      0.0            1,968          1       1,968.0       1,968.0       1,968        1,968           0.0  bind                  
      0.0            1,103          1       1,103.0       1,103.0       1,103        1,103           0.0  fcntl                 

[5/8] Executing 'cuda_api_sum' stats report

 Time (%)  Total Time (ns)  Num Calls    Avg (ns)       Med (ns)      Min (ns)      Max (ns)       StdDev (ns)             Name         
 --------  ---------------  ---------  -------------  -------------  -----------  -------------  ---------------  ----------------------
     88.4    1,416,225,024          2  708,112,512.0  708,112,512.0       96,180  1,416,128,844  1,001,286,299.1  cudaMemcpy            
     11.5      183,967,717          1  183,967,717.0  183,967,717.0  183,967,717    183,967,717              0.0  cudaMalloc            
      0.2        2,636,053          1    2,636,053.0    2,636,053.0    2,636,053      2,636,053              0.0  cudaLaunchKernel      
      0.0           52,527          1       52,527.0       52,527.0       52,527         52,527              0.0  cuLibraryLoadData     
      0.0           15,926          1       15,926.0       15,926.0       15,926         15,926              0.0  cudaFree              
      0.0            1,098          1        1,098.0        1,098.0        1,098          1,098              0.0  cuModuleGetLoadingMode
      0.0              668          1          668.0          668.0          668            668              0.0  cuLibraryGetKernel    
      0.0              285          1          285.0          285.0          285            285              0.0  cuKernelGetName       

[6/8] Executing 'cuda_gpu_kern_sum' stats report
SKIPPED: /content/report3.sqlite does not contain CUDA kernel data.
[7/8] Executing 'cuda_gpu_mem_time_sum' stats report
SKIPPED: /content/report3.sqlite does not contain GPU memory data.
[8/8] Executing 'cuda_gpu_mem_size_sum' stats report
SKIPPED: /content/report3.sqlite does not contain GPU memory data.
Generated:
	/content/report3.nsys-rep
	/content/report3.sqlite

*/
