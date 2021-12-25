#include <stdio.h>

int main()
{
	char a = 'a';
	char * pa = &a;
	printf("%c\n",*pa);
	size_t del = sizeof(a);
	char * pb = (char *)(pa + del);
	*pb = 'b';
	printf("%c\n",*pa);
	printf("%c\n",*(pb));
}
