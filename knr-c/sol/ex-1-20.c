#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAB_SIZE 8

void detab(char s[], char p[]){
	int cs = 0, cp = 0;
	while(s[cs] != '\0'){
		if(s[cs] == '\t'){
			int rem = TAB_SIZE - (cp % 8);
			printf("rem : %d\n", rem);
			for(int j = 0; j < rem; j++)
				p[cp++] = ' ';
				//p[cp++] = '*';
			cs++;
		}
		else {
			p[cp++] = s[cs++];
		}
	}
	p[cp++] = '\0';
}

int main(){
	char s[1024] = "abc\tewewf\tx", t[1024];
	printf("%s\n", s);
	detab(s, t);
	printf("%s\n", t);
}
