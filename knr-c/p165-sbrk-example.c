#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#define BRK_SZ 1024*1024

int main(){
	void * ptr = sbrk(0);
	printf("initial program break is %p\n", ptr);
	ptr = sbrk(BRK_SZ*2);
	void *p1 = malloc(10240);
	printf("allocated 1024^2 bytes\nallocated program break is now at %p\nsleeping for 20 seconds..", sbrk(0));
	sleep(20);
	ptr = sbrk(-BRK_SZ);
	printf("deallocated half of memory\nprogram break is %p\n", sbrk(0));
	sleep(20);
	free(p1);
	ptr = sbrk(-BRK_SZ);
	printf("deallocated all of memory\nprogram break is %p\n", sbrk(0));
        return 0;
}
