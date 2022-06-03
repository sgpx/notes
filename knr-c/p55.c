#include <stdio.h>

int fx(int x)
{
	x = x + 1;
}

main()
{
	int i = 5;
	i = fx(i);
	printf("%d\n",i);
}
