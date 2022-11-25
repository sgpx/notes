#include <stdio.h>
#include <stdlib.h>

int main(){
	FILE * fptr = fopen("p001.c", "r");
	char **p = (char**)malloc(1024*1024*5);
	size_t x = 5;
	size_t * y = &x;
	while(getline(p, y, fptr) != EOF ){
		printf("%s", *p);
	}
}
