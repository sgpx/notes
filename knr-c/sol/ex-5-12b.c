#include <stdio.h>
#include <stdlib.h>

void detab(char s[], char t[], int argc, char *argv[]){
	int ts = 0, tw = 8, start_col = 8;
	for(int i = 1; i < argc; i++){
		char *s = argv[i];
		if(*s == '-'){
			s++;
			start_col = atoi(s);
		}
		else if(*s == '+'){
			tw = atoi(s);
		}
	}
	ts = start_col;
	printf("start_col : %d\n", start_col);
	printf("tw : %d\n", tw);

	int cs = 0, ct = 0;
	while(s[cs] != '\0'){
		printf("===\nct : %d\n", ct);
		printf("%s\n", t);
		if(s[cs] == '\t'){
			printf("ts : %d\n", ts);
			while(ct < ts-1){
				t[ct++] = '.';
			}
			cs++;
			ts += tw;
		}
		else {
			t[ct++] = s[cs++];
		}
	}
	t[ct] = '\0';
}

int main(int argc, char *argv[]){
	char s[100] = "as\tsf\tewq\tsfsdf\t";
	char t[100];
	detab(s, t, argc, argv);
	printf("s:\n%s\nt:\n%s\n", s, t);
}
