#include <stdio.h>

int main(){
	char p[10] = "lol\n";
	char q[5] = "ok\n";
	char * x = p;
	printf("%s", x);
	x = &q[0];
	printf("%s", x);
}
