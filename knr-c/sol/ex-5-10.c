#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char * opstack[100];
int opctr = 0;

char * pop(void){
	if(opctr > 0)
		return opstack[--opctr];
	else
		return 0;
}

void push(char * s){
	printf("pushing '%s'...\n", s);
	char * dup = (char*)malloc(100);
	strcpy(dup, s);
	opstack[opctr++] = dup;
}

void rv(void){
	printf("rv: '%s'\n", opstack[opctr-1]);
}

int isnumber(char *s){
	char * p = s;
	if(*p == '-' || *p == '+') ++p;
	while( *p != '\0' ){
		char c = *p;
		if(c <= '0' && c >= '9' && c != '.')
			return 0;
		++p;
	}
	return 1;
}

int main(int argc, char *argv[]){
	//printf("argc : %d\n", argc);
	if(argc <= 1) return 1;

	char ** ptr = argv + 1;
	for(int i = 1; i < argc; i++){
		printf("input: %s\n", argv[i]);
		char *s = argv[i];
		char s1 = *s;
		if(strlen(s) == 1 && s1 == '+'){
			char *p1 = pop();
			char *p2 = pop();
			double res = atof(p1) + atof(p2);
			char *p3 = (char*)malloc(100);
			gcvt(res, 6, p3);
			push(p3);
		}
		else if(strlen(s) == 1 && s1 == '-'){
			char *p1 = pop();
			char *p2 = pop();
			double res = atof(p2) - atof(p1);
			char *p3 = (char*)malloc(100);
			gcvt(res, 6, p3);
			push(p3);
		}
		else if(strlen(s) == 1 && s1 == 'x'){
			char *p1 = pop();
			char *p2 = pop();
			double res = atof(p1) * atof(p2);
			char *p3 = (char*)malloc(100);
			gcvt(res, 6, p3);
			push(p3);
		}
		else if(strlen(s) == 1 && s1 == '/'){
			char *p1 = pop();
			char *p2 = pop();
			double res = atof(p2) / atof(p1);
			char *p3 = (char*)malloc(100);
			gcvt(res, 6, p3);
			push(p3);
		}
		else if(strlen(s) == 1 && s1 == '%'){
			char *p1 = pop();
			char *p2 = pop();
			double res = (int) atof(p2) % (int) atof(p1);
			char *p3 = (char*)malloc(100);
			gcvt(res, 6, p3);
			push(p3);
		}

		else if(isnumber(s)) push(s);
	}
}
