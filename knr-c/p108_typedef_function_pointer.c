#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef int (*mx)(void*, void*);

int main(){
	mx a = (mx)strcmp;
	printf("%d\n", a("x1", "x2"));
}
