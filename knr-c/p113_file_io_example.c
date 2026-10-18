#include <stdio.h>

int main(){
	FILE* fptr = fopen("a.c", "r");
	char c;
	while( (c = fgetc(fptr)) != EOF ){
		printf("%c", c);
	}
	printf("\n");
	return 0;
}
