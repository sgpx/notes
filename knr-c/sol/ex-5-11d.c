#include <stdio.h>
#include <stdlib.h>
#define CHAR_TAB '*'
#define CHAR_SPACE '.'

void detab(char s[], char t[], int argc, char *argv[]){
	int cs = 0, ct = 0, tn = 1;
	int ts = tn < argc ? atoi(argv[tn]) : 8;

	while(s[cs] != '\0'){
		printf("cs : %d, s[cs] : '%c'\n", cs, s[cs]);
		printf("ts : %d, ct : %d\n", ts, ct);
		if(s[cs] == '\t'){
			while(ct < ts){
				t[ct++] = '.';
				printf("ct %d ts %d\n", ct, ts);
			}
			tn++;
			int tso = ts;

			if(tn < argc){
				printf("%s\n", argv[tn]);
				ts = atoi(argv[tn]);
			}
			else ts = 8;
			ts += tso;
			cs++;
		}
		else {
			t[ct++] = s[cs++];
		}
	}
	t[ct++] = '\0';
}

int main(int argc, char * argv[]){
	char s[100] =
	"as\tasdfasdf\tfjewkfj\t\t\tdfsav\txdsfs", t[1000];

	detab(s, t, argc, argv);
	printf("s:\n%s\n", s);
	printf("t:\n%s\n", t);
	printf("ref:\nas......asdfasdf........fjewkfj.................dfsav...xdsfs\n");

	return 0;
}
