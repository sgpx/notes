#include <stdio.h>

struct stc {
	int x;
};

int main(){
	struct stc a;
	a.x = 1;
	struct stc * b = &a;
	printf("%d\n", b->x);
}
