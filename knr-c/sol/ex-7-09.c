#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int v1_isupper(unsigned char x)
{
	if (x >= 'A' && x <= 'Z')
		return 1;
	else
		return 0;
}

int v2_isupper(unsigned char x)
{
	char *arr = calloc(300, sizeof(char));
	for (int i = 65; i < 91; i++)
		arr[i] = 1;
	int res = arr[x];
	free(arr);
	return res;
}

int main()
{
	for (char p = 'A'; p <= 'Z'; p++)
		v1_isupper(p);
	for (char p = 'a'; p <= 'z'; p++)
		v1_isupper(p);
}
