#include <stdio.h>
#include <stdlib.h>

void entab(char s[], char t[], int argc, char *argv[]){
	int ts = 0, tw = 0, start_col = 0;
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
	ts = start_col ? start_col : 0;

	printf("ts : %d, tw : %d, start_col : %d\n", ts, tw, start_col);
	int cs = 0, ct = 0, wsc = 0;
	while(s[cs] != '\0'){
		printf("===\ncs : %d\n", cs);
		printf("s[cs] : '%c'\n", s[cs]);
		printf("wsc : %d\n", wsc);
		printf("ts : %d\n", ts);
		if(cs == ts-1){
			printf("cs : %d, ts : %d, wsc : %d\n", cs, ts, wsc);
			if(wsc > 0){
				t[ct++] = '\t';
				wsc = 0;
			}
			ts += tw;
		}
		if(s[cs] == '.'){
			wsc++;
			cs++;
		}
		else {
			if(wsc > 0){
				printf("adding dots..\nwsc : %d\n", wsc);
				for(int u=0; u<wsc; u++)
					t[ct++] = '.';
				wsc = 0;
			}
			t[ct++] = s[cs++];
		}
	}
	t[ct] = '\0';
}

int main(int argc, char *argv[]){
	//char s[100] = "as\tsf\tewq\tsfsdf\t";
	//char s[100] = "as..sf..tewq..tsfsd..t";
	char s[100] = "as.sf..ewq.sfsdf";
	char t[100];
	entab(s, t, argc, argv);
	printf("s:\n%s\nt:\n%s\n", s, t);
}
