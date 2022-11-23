#include <stdio.h>

int xstrlen(char * s){
	char * p = s;
	while(*p != '\0') ++p;
	return p - s;
}

int main(){
	printf("%d\n", xstrlen("heyy"));
	return 0;
}
