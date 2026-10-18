#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void x_strncpy(char * s, char * t, int n){
	int ctr = n;
	while(ctr--){
		char c = *t;
		*s = c;
		++s;
		++t;
	}
}

void x_strncat(char * s, char * t, int n){
	int ctr = n;
	while(*s != '\0') ++s;
	while(ctr--){
		char c = *t;
		*s = c;
		++s;
		++t;
	}
	*s = '\0';
}

int x_strncmp(char * s, char * t, int n){
	int res = 0;
	while(n--){
		res += *s++ - *t++;
	}
	return res;
}

int main(){
	char s[5] = "abcd";
	char t[5] = "xyz";
	int res = x_strncmp(s, t, 3);
	printf("%d\n", res);
	return 0;
}
