#include <stdio.h>

void getline(char * s){
	char c;
	while((c = getchar()) != '\n') *s++ = c;
	*s = '\0';
}

int main(){
	char s[100];
	getline(s);
	printf("s: %s\n", s");
}
