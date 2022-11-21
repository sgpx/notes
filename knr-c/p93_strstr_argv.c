#include <stdio.h>
#include <string.h>

int x_getline(char *s){
	char * p = s;
	while((*s++ = getchar()) != '\n');
	*(--s) = '\0';
	return s - p;
}

int main(int argc, char * argv[]){

	printf("argc : %d\n", argc);
	char * p1 = *(argv+1), line[1024];
	printf("p1 : %s\n", p1);

	while(x_getline(line) > 0)
		if(strstr(line, p1) != NULL)
			printf("found : %s\n", line);
}
