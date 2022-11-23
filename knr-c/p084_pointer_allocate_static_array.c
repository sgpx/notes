#include <stdio.h>
#define ALLOCSIZE 1000

static char allocbuf[ALLOCSIZE];
static char * allocp = allocbuf;

char *alloc(int n){
	if(allocbuf + ALLOCSIZE - allocp >= n){
			allocp += n;
		return allocp - n;
	}
	else
		return 0;
}

int main(){
	char * ptr ;
	ptr = alloc(1001);
	printf("%p\n", ptr);

	ptr = alloc(1000);
	printf("%p\n", ptr);

	*ptr = 'b';
	*(ptr+1) = 'a';
	*(ptr+2) = '\0';
	printf("*ptr : '%s'\n", ptr);
	return 0;
}
