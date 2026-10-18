/*

Given two input vectors A and B of size N, compute the output vector C such that:

    C[i] = A[i] + B[i] for all i in [0, N-1]

*/

#include <cuda_runtime.h>
#include <iostream>
#define GET_NUM_BLOCKS(N, T) ((N + T - 1) / T)

__global__ void sum_kern(int *A, int *B, int *C, int N) {
	int i = threadIdx.x + (blockIdx.x * blockDim.x);
	if(i < N) { C[i] = A[i] + B[i]; }
	// __syncthreads();
}

int main() {
	int N = 1024;
	const int bytes = sizeof(int) * N;
	const int num_blocks = GET_NUM_BLOCKS(N, 256);

	int *h_A, *h_B, *h_C, *d_A, *d_B, *d_C;
	h_A = (int*)malloc(bytes);
	h_B = (int*)malloc(bytes);
	h_C = (int*)malloc(bytes);
	for(int i = 0; i < N ; i++ ) {
		h_A[i] = (int)std::rand();
		h_B[i] = (int)std::rand();
	} 
	cudaMalloc((void**)&d_A, bytes);
	cudaMalloc((void**)&d_B, bytes);
	cudaMalloc((void**)&d_C, bytes);
	cudaMemcpy(d_A, h_A, bytes, cudaMemcpyHostToDevice);
	cudaMemcpy(d_B, h_B, bytes, cudaMemcpyHostToDevice); 
	sum_kern<<<num_blocks, 256>>>(d_A, d_B, d_C, N);
	cudaMemcpy(h_C, d_C, bytes, cudaMemcpyDeviceToHost);
	for(int i = 0; i < N; i++) { std::cout << h_A[i] << "+" << h_B[i] << "=" << h_C[i] << std::endl ; }
	cudaFree(d_A);
	cudaFree(d_B);
	cudaFree(d_C);
	free(h_A);
	free(h_B);
	free(h_C);
	return 0;
}


/*

$ nvcc a.cu -o a.out && nsys profile --stats=true ./a.out

Generating '/tmp/nsys-report-e0bc.qdstrm'
[1/8] [========================100%] report2.nsys-rep
[2/8] [========================100%] report2.sqlite
[3/8] Executing 'nvtx_sum' stats report
SKIPPED: /content/report2.sqlite does not contain NV Tools Extension (NVTX) data.
[4/8] Executing 'osrt_sum' stats report

 Time (%)  Total Time (ns)  Num Calls    Avg (ns)     Med (ns)    Min (ns)   Max (ns)    StdDev (ns)            Name         
 --------  ---------------  ---------  ------------  -----------  --------  -----------  ------------  ----------------------
     72.2      480,100,674         13  36,930,821.1  5,525,124.0     1,774  320,800,314  87,594,085.6  poll                  
     27.0      179,767,064        497     361,704.4     17,457.0     1,265   18,079,673   1,203,199.2  ioctl                 
      0.3        2,044,948         29      70,515.4     13,906.0     8,029    1,370,649     251,329.1  mmap64                
      0.2        1,152,926         10     115,292.6     36,811.0    29,896      584,920     177,346.1  sem_timedwait         
      0.1          417,924         47       8,892.0      8,351.0     2,597       15,511       3,123.0  open64                
      0.0          212,304         36       5,897.3      3,915.0     1,191       24,435       5,339.8  fopen                 
      0.0          201,918         12      16,826.5     18,325.5     1,253       27,950       8,240.1  write                 
      0.0          185,011         14      13,215.1      8,173.5     2,155       80,389      19,722.9  mmap                  
      0.0          152,221          2      76,110.5     76,110.5    65,451       86,770      15,074.8  pthread_create        
      0.0           85,221          8      10,652.6      2,042.5     1,247       46,454      15,780.8  putc                  
      0.0           85,062          1      85,062.0     85,062.0    85,062       85,062           0.0  pthread_cond_wait     
      0.0           47,599         23       2,069.5      1,687.0     1,005        5,764       1,183.4  fclose                
      0.0           39,686          1      39,686.0     39,686.0    39,686       39,686           0.0  fgets                 
      0.0           29,721          6       4,953.5      5,343.0     1,735        7,365       2,208.3  open                  
      0.0           24,925         15       1,661.7      1,523.0     1,211        3,281         577.7  read                  
      0.0           21,485          2      10,742.5     10,742.5     8,580       12,905       3,058.2  socket                
      0.0           21,405          4       5,351.3      4,401.5     2,528       10,074       3,527.3  fwrite                
      0.0           20,708          1      20,708.0     20,708.0    20,708       20,708           0.0  pthread_cond_broadcast
      0.0           20,118          8       2,514.8      2,012.5     1,273        5,419       1,413.4  close                 
      0.0           18,924          3       6,308.0      6,769.0     4,418        7,737       1,706.8  pipe2                 
      0.0           18,646          3       6,215.3      5,875.0     3,885        8,886       2,517.8  munmap                
      0.0           11,456          1      11,456.0     11,456.0    11,456       11,456           0.0  connect               
      0.0            3,619          1       3,619.0      3,619.0     3,619        3,619           0.0  dup                   
      0.0            3,464          3       1,154.7      1,145.0     1,068        1,251          91.9  fcntl                 
      0.0            1,624          1       1,624.0      1,624.0     1,624        1,624           0.0  bind                  
      0.0            1,091          1       1,091.0      1,091.0     1,091        1,091           0.0  listen                

[5/8] Executing 'cuda_api_sum' stats report

 Time (%)  Total Time (ns)  Num Calls    Avg (ns)    Med (ns)  Min (ns)   Max (ns)     StdDev (ns)            Name         
 --------  ---------------  ---------  ------------  --------  --------  -----------  -------------  ----------------------
     99.8      190,635,803          3  63,545,267.7   4,715.0     2,263  190,628,825  110,057,589.1  cudaMalloc            
      0.1          143,828          3      47,942.7  29,337.0     3,791      110,700       55,830.2  cudaFree              
      0.0           70,812          1      70,812.0  70,812.0    70,812       70,812            0.0  cudaLaunchKernel      
      0.0           59,639          3      19,879.7  21,942.0     7,625       30,072       11,364.7  cudaMemcpy            
      0.0           39,896          1      39,896.0  39,896.0    39,896       39,896            0.0  cuLibraryLoadData     
      0.0            1,364          1       1,364.0   1,364.0     1,364        1,364            0.0  cuModuleGetLoadingMode
      0.0              471          1         471.0     471.0       471          471            0.0  cuLibraryGetKernel    
      0.0              437          1         437.0     437.0       437          437            0.0  cuKernelGetName       

[6/8] Executing 'cuda_gpu_kern_sum' stats report

 Time (%)  Total Time (ns)  Instances  Avg (ns)  Med (ns)  Min (ns)  Max (ns)  StdDev (ns)                 Name               
 --------  ---------------  ---------  --------  --------  --------  --------  -----------  ----------------------------------
    100.0            2,624          1   2,624.0   2,624.0     2,624     2,624          0.0  sum_kern(int *, int *, int *, int)

[7/8] Executing 'cuda_gpu_mem_time_sum' stats report

 Time (%)  Total Time (ns)  Count  Avg (ns)  Med (ns)  Min (ns)  Max (ns)  StdDev (ns)           Operation          
 --------  ---------------  -----  --------  --------  --------  --------  -----------  ----------------------------
     50.7            2,272      2   1,136.0   1,136.0       928     1,344        294.2  [CUDA memcpy Host-to-Device]
     49.3            2,208      1   2,208.0   2,208.0     2,208     2,208          0.0  [CUDA memcpy Device-to-Host]

[8/8] Executing 'cuda_gpu_mem_size_sum' stats report

 Total (MB)  Count  Avg (MB)  Med (MB)  Min (MB)  Max (MB)  StdDev (MB)           Operation          
 ----------  -----  --------  --------  --------  --------  -----------  ----------------------------
      0.008      2     0.004     0.004     0.004     0.004        0.000  [CUDA memcpy Host-to-Device]
      0.004      1     0.004     0.004     0.004     0.004        0.000  [CUDA memcpy Device-to-Host]

Generated:
	/content/report2.nsys-rep
	/content/report2.sqlite

*/
