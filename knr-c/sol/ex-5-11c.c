#include <stdio.h>
#include <stdlib.h>
#define CHAR_TAB '\t'
#define CHAR_SPACE ' '

//#define CHAR_TAB '*'
//#define CHAR_SPACE '.'

void entab(char s[], char t[], int argc, char *argv[]){
	int list_ctr = 1;
	int ts = list_ctr < argc ? atoi(argv[list_ctr]) : 8;

	int cs = 0, ct = 0, wsc = 0;
	while(s[cs] != '\0'){
		printf("%c %d %d %d %d\n", s[cs], cs, ct, wsc, ts);
		if(cs == ts) {
			if(wsc > 0){
				t[ct++] = CHAR_TAB;
				wsc = 0;
			}

			++list_ctr;
			if(list_ctr < argc)
				ts = atoi(argv[list_ctr]);
			else
				ts += 8;
		}
		if(s[cs] == CHAR_SPACE){
			wsc++;
			cs++;
		}
		else {
			if(wsc > 0){
				for(int u=0; u<wsc; u++)
					t[ct++] = CHAR_SPACE;
				wsc = 0;
			}
			t[ct++] = s[cs++];
		}
	}
	t[ct] = '\0';
	printf("s:\n%s\nt:\n%s\n", s, t);
}

int main(int argc, char *argv[]){
	//char s[100] = "a..b....ca......x.......df";
	char s[100] = "a  b    ca      x       df";
	char t[100];
	entab(s, t, argc, argv);
}
