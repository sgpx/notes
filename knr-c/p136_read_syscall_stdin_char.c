#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
	char c;
	read(0, &c, 1);
	printf("'%c' (%d)\n", c, c);
	return 0;
}
