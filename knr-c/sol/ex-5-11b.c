#include <stdio.h>
#include <stdlib.h>

void entab(char s[], char t[], int argc, char *argv[]){
	int tsc = 1;
	int ts = tsc < argc ? atoi(argv[tsc]) : 8;
	int cs = 0, ct = 0;
	int wsc = 0;

	while(s[cs] != '\0'){
		char c = s[cs];
		printf("ts : %d\n", ts);
		if(ts == 0) {
			printf("wsc : %d\n", wsc);

			if(tsc+1 < argc) {
				++tsc;
				ts = tsc < argc ? atoi(argv[tsc]) : 8;
			}
			else ts = 8;
			if(wsc){
				t[ct++] = '\t';
				wsc = 0;
			}
		}

		if(c == '.'){
			wsc += 1;
			cs++;
			ts--;
		}
		else {
			if(wsc){
				for(int u=0; u<wsc; u++)
					t[ct++] = '.';
				wsc = 0;
			}
			t[ct++] = s[cs++];
			ts--;
		}
	}

	t[ct] = '\0';
}

int main(int argc, char *argv[]){
	char s[100] = "a..b....ca.......ca.....b.c";
	char  t[100];
	entab(s, t, argc, argv);
	printf("s:\n%s\nt:\n%s\n", s, t);
	return 0;
}
