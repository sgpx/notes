#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

#define MAXOP 100
#define NUMBER '0'
#define MAXVAL 100
#define BUFSIZE 100

int sp = 0;
double val[MAXVAL];

char buf[BUFSIZE];
int bufp = 0;

int getch(void){
	return (bufp > 0) ? buf[--bufp] : getchar();
}

void ungetch(int c){
	if(bufp >= BUFSIZE)
		printf("ungetch: too many characters\n");
	else
		buf[bufp++] = c;
}

int getop(char s[]){
	int i = 0;
	char c = getch();
	printf("c: '%c' (%d)\n---\n", c, c);
	while(c == ' ') c = getch();
	while(c != '\n' && c != ' ' && c != '\0') {
		printf("c : '%c'\n", c);

		if(isdigit(c) || c == '.') s[i++] = c;
		else return c;

		c = getch();
	}
	s[i] = '\0';
	return NUMBER;
}

void push(double f){
	printf("===\n");
	printf("push f: %f\nsp: %d\n", f, sp);
	printf("===\n");

	if(sp < MAXVAL) val[sp++] = f;
	else printf("error: stack full, can't push %g\n", f);
}

double pop(){
	printf("===\n");
	printf("pop sp : %d\nval[sp] : %f\n", sp-1, val[sp-1]);
	printf("===\n");

	if(sp > 0) return val[--sp];
	else printf("error: stack empty\n");

	return 0;
}

int xmain(){
	char s[20];
	char type = getop(s);
	while(type != 'z' ){
		type = getop(s);
		printf("type : '%c'\n", type);
		printf("s : '%s'\n", s);
	}
	return 0;
}

void print_stack(void){
	for(int i = 0; i < 10; i++) printf("val[%d] = %f\n", i, val[i]);
}

int main(){
	int type;
	double op2;
	char s[MAXOP];

	while( (type = getop(s)) != 'z' ){
		printf("type : %c\n", type);
		printf("s : %s\n", s);
		switch(type){
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
				printf("\t%.8g\n", pop());
				break;
			case '%':
				op2 = pop();
				push((int)pop() % (int)op2);
				break;
			default:
				printf("unknown command\n");
				break;
		}
	}
	printf("res: %f\n", val[0]);

	print_stack();

	return 0;
}
