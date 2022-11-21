#include <stdio.h>

main()
{
	double nc;
	for(nc = 0; getchar() != 'x'; ++nc)
	{
		printf("%.0f\n",nc);
	}
}
