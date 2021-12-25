#include <stdio.h>

int main(int argc, char *argv[])
{
	int arg_ctr = 0;
	while(arg_ctr < argc)
	{
		char * fx = argv[arg_ctr];
		char c = * fx;
		int ctr = 0;
		printf("\n");
		while(c != '\0')
		{
			printf("%c",c);
			++ctr;
			c = *(fx+ctr);
		}
		printf("\n");
		printf("%d-th argument is %s",arg_ctr,fx);
		++arg_ctr;
	}
	return 0;
}
