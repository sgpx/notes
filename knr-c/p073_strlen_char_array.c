#include <stdio.h>

int getlength(char * s){
	int n;
	for(n = 0; *s != '\0'; s++) n++;

	return n;
}

int main(){
	char a[4] = { 'a', 'b', 'c', '\0' };
	int x =	getlength(&a[0]);

	printf("length is %d\n", x);

	return 0;
}
