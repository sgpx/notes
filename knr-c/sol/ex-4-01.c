#include <stdio.h>

void xgetline(char s[]){
	char c = getchar();
	int i = 0;
	while( c != '\n' ){ s[i++] = c; c = getchar(); }
	s[i] = '\0';
}

int strindex(char s[], char t[]){
	int res = -1;
	for(int i = 0; s[i] != '\0'; i++) {
		int k = i;
		int match = 1;
		for(int j = 0; t[j] != '\0'; j++) {
			if(s[k++] != t[j]){ match = 0; break; }
		}
		if (match) res = i;
	}
	return res;
}

int main(){
	char t[5] = "ould";
	char s[100];

	for(int i = 0; i < 5; i++) {
		xgetline(s);
		int chk = strindex(s, t);
		printf("s: %s\n", s);
		printf("check: %d\n", chk);
	}

	return 0;
}
