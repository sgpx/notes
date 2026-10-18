#include <stdio.h>
#include <string.h>
main()
{
	int csize = 27;
	int wf[csize];
	memset(wf,0,sizeof(wf));
	int wstate = 0;
	int wc = 0;
	char c;
	c = getchar();
	while( c != EOF )
	{
		if(c == ' ' || c == '\n' || c == '\t')
		{
		}
		else
		{
			++wf[c-'a'];
		}
		c = getchar();
	}
	int upper_limit = 0;
	for(int i=1; i<csize; i++)
	{
		upper_limit = upper_limit < wf[i] ? wf[i] : upper_limit;
		printf("%d %d\n",i,wf[i]);
	}
	printf("max: %d\n",upper_limit);
	return 0;
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
			int curr = wf[i];
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


// output
// 1 2
// 2 0
// 3 0
// 4 2
// 5 0
// 6 0
// 7 0
// 8 0
// 9 0
// 10 0
// 11 0
// 12 0
// 13 0
// 14 0
// 15 0
// 16 0
// 17 0
// 18 0
// 19 0
// 20 0
// 21 0
// 22 2
// 23 0
// 24 0
// 25 0
// 26 0
// max: 2


// output
