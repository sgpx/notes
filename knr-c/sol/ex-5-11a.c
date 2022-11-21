#include <stdio.h>
#include <stdlib.h>

void detab(char s[], char t[], int argc, char *argv[]){
	int ct = 0, cs = 0;

	for(int i = 1; i < argc && s[cs] != '\0'; i++){
		int ts = atoi(argv[i]);
		printf("ts : %d\n", ts);
		while(ts > 0){
			printf("=====\n");
			printf("ts : %d\n", ts);
			printf("cs : %d, ct : %d\n", cs, ct);
			printf("s[cs = %d] = '%c'\n", cs, s[cs]);
			printf("t:\n%s\n", t);
			if(s[cs] == '\0') break;
			else if(s[cs] != '\t')
				t[ct++] = s[cs++];
			else {
				printf("ns : %d\n", ts);
				for(int j = 0; j < ts; j++){
					t[ct++] = '*';
				}
				ts = 0;
				cs++;
			}
			ts--;
		}
	}

	t[ct] = '\0';
	printf("s:\n%s\n", s);
	printf("t:\n%s\n", t);
}

int main(int argc, char * argv[]){
	char s[100] =
	"as\tasdfasdf\tfjewkfj\t\t\tdfsav\txdsfs", t[1000];

	detab(s, t, argc, argv);
	printf("%s\n", s);
	printf("as......asdfasdf........fjewkfj.................dfsav...xdsfs\n");

	return 0;
}
