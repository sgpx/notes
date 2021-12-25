#include <stdio.h>

int main()
{
	char a[10] = "123456789";
	printf("%s\n",a);

	char null_character = '\0';
	a[5] = null_character;
	printf("%s\n",a);

	return 0;
}
