#include <stdio.h>
#include <string.h>

#define BUFSIZE 1024

/*

malloc() and free() calls must occur in order to avoid data loss

*/

static char buf[BUFSIZE];
static char *ptr = buf;

char * x_malloc(int n){
	void *res = (char*)(ptr);
	ptr += n;
	return res;
}

void x_free(char *p){
	ptr = p;
}

int main(){
	char *a = x_malloc(20);
	char *b = x_malloc(20);
	strcpy(a, "lol");
	strcpy(b, "lmao");
	printf("%s\n", a);
	printf("%s\n", b);
	x_free(a);
	x_free(b);
	return 0;
}
