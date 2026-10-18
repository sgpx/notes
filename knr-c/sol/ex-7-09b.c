#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define VERSION 2
char *arr = NULL;

int v1_isupper(unsigned char x)
{
	if (x >= 'A' && x <= 'Z')
		return 1;
	else
		return 0;
}

int v2_isupper(unsigned char x)
{
	return arr[x];
}

int (*fxn)(unsigned char) = (VERSION == 1) ? v1_isupper: v2_isupper;

int init(){
	arr = calloc(300, sizeof(char));
	for(int i = 'A'; i <= 'Z'; i++)
		arr[i] = 1;
}

int testrun()
{
	for (unsigned char p = 'A'; p <= 'Z'; p++)
		fxn(p);
	for (unsigned char p = 'a'; p <= 'z'; p++)
		fxn(p);
}

int main()
{
	#if VERSION == 2
		init();
	#endif
	
	for (long i = 0; i < 100000; i++)
		testrun();
	return 0;
}
