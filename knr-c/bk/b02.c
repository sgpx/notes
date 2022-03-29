#include <stdio.h>

main()
{
	int f,c;
	int l,u,step;

	l = 0;
	u = 300;
	step = 20;

	f = l;
	while(f <= u){
		c = 5*(f-32)/9;
		printf("%d %d\n",f,c);
		f = f + step;
	}
	return 0;
}
