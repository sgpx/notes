#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define SEP '#'
#define MAXTOKEN 100
enum { NAME, PARENS, BRACKETS };

void dcl(void);
void dirdcl(void);

int gettoken(void);
int tokentype;

char token[MAXTOKEN];
char name[MAXTOKEN];
char datatype[MAXTOKEN];
char out[MAXTOKEN];

char buf[MAXTOKEN];
int bufp = 0;

char getch(void){
	return bufp > 0 ? buf[--bufp] : getchar();
}

void ungetch(char c){
	buf[bufp++] = c;
}

void dcl(void){
	int ns = 0;
	while(gettoken() == '*') ++ns;
	dirdcl();
	for(int i=0; i<ns; i++)
		strcat(out, " pointer to");
}
void dirdcl(void){
	int type;

	if(tokentype == '('){
		dcl();
		if(tokentype != ')')
			printf("syntax error missing parenthsis\n");
	}
	else if(tokentype == NAME){
		strcpy(name, token);
	}
	else
		printf("error expected name or dcl\n");

	while((type = gettoken()) == PARENS || type == BRACKETS){
		if(type == PARENS){
			strcat(out, " function returning");
		}
		else {
			strcat(out, " array");
			strcat(out, token);
			strcat(out, " of");
		}
	}
}

int gettoken(void){
	printf("gettoken called\n");
	char c, *p = token;
	while( (c = getch()) == ' ' || c == '\t');

	if(c == '('){
		printf("c is (\n");
		if( (c=getch()) == ')' ){
			printf("token is (), tokentype : PARENS");
			strcpy(token, "()");
			return tokentype = PARENS;
		}
		else {
			printf("token is only (, tokentype : (\n");
			ungetch(c);
			return tokentype = '(';
		}
	} else if(c == '['){
		printf("c is [\n");
		*p++ = c;
		while((*p++ = getch()) != ']');
		*p = '\0';
		printf("token : '%s'\ntokentype: BRACKETS", token);
		return tokentype = BRACKETS;
	}
	else if(isalpha(c)){
		printf("%c\n", c);
		*p++ = c;
		while( isalnum(c = getch())  ){
			printf("c : '%c', token: '%s'\n", c, token);
			*p++ = c;
		}
		*p = '\0';
		ungetch(c);
		printf("token: %s\n", token);
		return tokentype = NAME;
	}
	else {
		printf("tokentype : '%c'\n", c);
		return tokentype = c;
	}
}

int main(){
	int type;
	char temp[10000];

	gettoken();

	strcpy(out, token);
	while( (type=gettoken()) != '\n'){
		if(type == PARENS || type == BRACKETS){
			strcat(out, token);
		}
		else if(type == '*'){
			sprintf(temp, "(*%s)", out);
			strcpy(out, temp);
		}
		else if(type == NAME){
			sprintf(temp, "%s %s", token, out);
			strcpy(out, temp);
		}
		else {
			printf("invalid input at %s\n", token);
		}
	}
	printf("%s\n", temp);
}
