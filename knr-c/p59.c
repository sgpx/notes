#include <stdio.h>


int main(){
	abc:
		printf("abc\n");
		return 0;
	xyz:
		printf("xyz\n");
		return 0;

	if ( 1 == 2 ) goto xyz;
	else goto abc;
	return 0;
}

