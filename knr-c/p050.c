#include <stdio.h>

int xyz()
{
	static int x = 1;
	printf("%d\n",++x);
}

main()
{
	xyz();
	xyz();
}


// output
// 23


// output
// 2
// 3


// output
// 2
// 3
