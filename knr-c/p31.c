#include <stdio.h>

int times_two(int x)
{
	x = x * 2;
	printf("times_two x: %d\n",x);
}

main()
{
	int x = 1;
	times_two(x);
	printf("x is %d\n",x);

}


// output
// times_two x: 2
// x is 1
