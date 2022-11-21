#include <stdio.h>

int main(){
	char * lx[2];
	lx[0] = "foo bar baz";
	lx[1] = "abcd efgh";

	printf("'%s'\n'%s'\n", lx[0], lx[1]);
}
