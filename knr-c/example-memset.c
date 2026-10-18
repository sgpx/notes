#include <stdio.h>
#include <string.h>
main()
{
	char wl[100];
	memset(wl,'a',sizeof(wl));
	for(int i=0; i<100;i++)
	{
		printf("i: %d c: %c, ",i,wl[i]);
	}
}


