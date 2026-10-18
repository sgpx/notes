#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAXOP 100
#define NUMBER '0'
#define MAXVAL 100
#define ZEND 'z'
#define BUFSIZE 100

int sp = 0;
double val[MAXVAL];

char buf[BUFSIZE];
int bufp = 0;

int getch(void){
	return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(char c){
	//printf("ungetch c : %c %d\n", c, c);

	if(bufp >= BUFSIZE) printf("error: too many characters\n");
	else buf[bufp++] = c;
}

void push(double f){
	if(sp < MAXVAL) val[sp++] = f;
	else printf("error: stack full, sp : %d\n", sp);
}

double pop(void){
	if(sp > 0) return val[--sp];
	else printf("stack empty\n");
	return 0;
}

int getop(char s[]){
	int i = 0;
	char c = getch();
	while( c == ' ' || c == '\t' ){
		c = getch();
	}

	if( !isdigit(c) && c != '.' ) return c;

	while(isdigit(c)){
		s[i++] = c;
		c = getch();
	}

	s[i] = '\0';
	if( c != ZEND ) ungetch(c);
	return NUMBER;
}

int main(){
	int type;
	double op2;
	char s[MAXOP];

	while( (type = getop(s)) != ZEND ) {
		switch(type) {
			case NUMBER:
				push(atof(s));
				break;

			case '+':
				push(pop() + pop());
				break;

			case '-':
				op2 = pop();
				push(pop() - op2);
				break;

			case '*':
				push(pop() * pop());
				break;

			case '/':
				op2 = pop();
				if(op2 != 0) push(pop() / op2);
				else printf("zero division error\n");
				break;
			case '\n':
				printf("%f\n", pop());
				break;
			case '%':
				op2 = pop();
				push((int) pop() % (int) op2);
				break;
			default:
				printf("unknown operator\n");
				break;
		}
	}
}
