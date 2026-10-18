#include <stdio.h>
#include <string.h>
main()
{
	int wl[10];
	memset(wl,0,sizeof(wl));
	int wstate = 0;
	int wc = 0;
	char c;
	c = getchar();
	while( c != EOF )
	{
		if(c == ' ' || c == '\n' || c == '\t')
		{
			++wl[wc];
			wc = 0;
			wstate = 0;
		}
		else
		{
			wstate = 1;
		}
		if(wstate == 1)
		{
			++wc;
		}
		c = getchar();
	}
	int upper_limit = 0;
	for(int i=1; i<10; i++)
	{
		upper_limit = upper_limit < wl[i] ? wl[i] : upper_limit;
		printf("%d %d\n",i,wl[i]);
	}
	printf("max: %d\n",upper_limit);
	int y = upper_limit;
	while(y > -1)
	{
		printf("%02d ",y);
		for(int i=1; i<10; i++)
		{
			if(y == 0)
			{
				printf(" %d ",i);
				continue;
			}
			int curr = wl[i];
			if(curr >= y)
			{
				printf(" * ");
			}
			else
			{
				printf(" . ");
			}
		}
		printf("\n");
		--y;
	}
}
