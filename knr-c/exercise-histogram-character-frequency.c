#include <stdio.h>
#include <string.h>
main()
{
	int csize = 26;
	int wf[csize];
	memset(wf,0,sizeof(wf));
	char c = getchar();
	while( c != EOF )
	{
		if( c >= 'a' && c <= 'z' )
		{
			++wf[c-'a'];
		}
		c = getchar();
	}
	int wf_max = 0;
	for(int i=0; i<csize; i++)
	{
		wf_max = wf_max < wf[i] ? wf[i] : wf_max;
		printf("%d %c %d\n",i,i+'a',wf[i]);
	}
	printf("%d\n",wf_max);
	int y = wf_max;
	while(y > 0)
	{
		printf("%02d ",y);
		for(int i=0; i < csize; i++)
		{
			if(wf[i] >= y)
			{
				printf(" * ");
			}
			else
			{
				printf("   ");
			}
			
		}
		printf("\n");
		--y;
	}
	printf("   ");
	for(int i=0; i < csize; i++)
	{
		printf(" %c ",'a'+i);
	}
	printf("\n");
}
