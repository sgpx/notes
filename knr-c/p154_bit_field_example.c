#include <stdio.h>

struct {
	unsigned char f1 : 1;
} flags;

int main() {
	//flags.f1 |= 01;
	flags.f1 ^= 01;
	printf("%d\n", flags.f1);
	return 0;
}
