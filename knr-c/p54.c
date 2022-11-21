#include <stdio.h>

int main()
{
	int a = 5;
	int * ptr = &a;


	*(ptr + x) = 7;
	// x = 4 gives bus error/illegal instruction
	// x = 5 gives segfault
	// check `stack smashing` and `stack frames`


	printf("a0: %d\n",*ptr);
	printf("a1: %d\n",*(ptr+x));

	return 0;
}
