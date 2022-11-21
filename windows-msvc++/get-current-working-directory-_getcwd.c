#include <direct.h>
#include <stdio.h>

int main()
{
	int maxlen = 1024;
	char * xyz = "";
	_getcwd(xyz,maxlen);
	printf("%s\n",xyz);
	return 0;
}
