#include <stdio.h>

main()
{
	unsigned int x = 2;
	while(x < 100)
	{
		printf("%u\n",x);
		x = x << 1;
	}	
}


// output
// 2
// 8
// 32


// output
// 2
// 4
// 8
// 16
// 32
// 64
