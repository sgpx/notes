#include <stdio.h>

int main()
{
	int x = 1;
	int * y = &x;
	printf("%p\n",y);
	printf("%d\n",*y);
}


// output
// -553233172


// output
// %r
// 1


// output
// 0x7fff960955dc
// 1


// output
// 0x7ffc8e87d1ac
// 1


// output
// 0x7ffd11aa6b8c
// 1


// output
// 0x7ffefb90bf4c
// 1
