#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define NUMBER '0'

char buffer[100];
int bufp = 0;

void ungetch(char c){
	buffer[bufp++] = c;
}

char getch(){
	if(bufp) return buffer[--bufp];
	else return getchar();
}



char getop(char *s){
	int i, c;
	char *p = s;
	while( ( c = getch() ) == ' ');
	//*(s+1) = '\0';
	if(!isdigit(c) && c != '.') return c;

	i = 0;

	while(isdigit(c) || c == '.'){
		*(s+i) = c;
		++i;
		c = getch();
	}
	*(s+i) = '\0';

	ungetch(c);

	return NUMBER;

}

int main(){
	char s[100], type;
	while((type = getop(s)) != 'z' && type != '\n'){

		if(type == NUMBER) printf("s : %s\n", s);
		else printf("type : '%c'\n", type);;
	}
}
