#include <stdio.h>

int main()
{
	unsigned int x = 32;
	while(x >= 1)
	{
		printf("x = %u\n",x);
		x = x >> 1;
	}
	return 0;
}


// output
// x = 32
// x = 16
// x = 8
// x = 4
// x = 2
// x = 1
