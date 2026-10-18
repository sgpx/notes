#include <stdio.h>

int main(int argc, char * argv[]){

	printf("argc : %d\n", argc);
	for(char ** ptr = argv; ptr < (argv + argc); ptr++)
		printf("argv[%ld] = '%s'\n", ptr-argv, *ptr);
}
