#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
	//will give an error in valgrind
	//char **x = (char **)malloc(5);
	char **x = (char **)malloc(1024*1024);
	char *p = (char *)malloc(1024);
	strcpy(p, "foobar");
	*x = p;
	printf("%s\n", *x);
	free(x);
	free(p);
}
