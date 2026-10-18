#include <stdio.h>

main()
{
	unsigned int x = 11;
	unsigned int y = ~x;
	unsigned int z = y | ~0;
	unsigned int p = ~0;
	printf("%u %u %u %u\n",x,y,z,p);

}


// output
// 10 -11


// output
// 10 4294967285


// output
// 10 4294967285 


// output
// 10 4294967285 4294967295


// output
// 10 4294967285 4294967295 4294967295


// output
// 11 4294967284 4294967295 4294967295
