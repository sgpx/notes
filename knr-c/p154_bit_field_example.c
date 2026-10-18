#include <stdio.h>

struct {
	unsigned char left : 1;
	unsigned char right : 1;
} flags;

int main() {
	//flags.left |= 01;
	flags.left &= 01;
	flags.right |= 01;
	printf("%d\n", flags.left);
	printf("%d\n", flags.right);
	return 0;
}
