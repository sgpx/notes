#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	char *p = calloc(1024, sizeof(char));
	for(int i = 0; i < 1023; i++)
		*(p+i) = ('a' + (i % 26));
	// string p is automatically NULL terminated because calloc() sets all initial values to zero
	printf("%s\n", p);
	free(p);
	return 0;
}
