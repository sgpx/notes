#include <stdio.h>

void foobar(){
	static int foo = 1;
	printf("foo is %d\n", foo++);
}

int main(){
	for(int i = 0; i < 5; i++) foobar();
	return 0;
}
