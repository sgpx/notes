#include <stdio.h>

void escape(char s[], char t[]){
	int cs = 0, ct = 0;
	while(s[cs] != '\0'){
		switch(s[cs]){
			case '\n':
				t[ct] = '\\';
				t[ct+1] = 'n';
				ct += 2;
				break;

			case '\t':
				t[ct] = '\\';
				t[ct+1] = 't';
				ct += 2;
				break;

			default:
				t[ct] = s[cs];
				++ct;
				break;

		}
		++cs;
	}
}

int main(){
	char s[10] = "lmao\nlol";
	char t[10];
	escape(s,t);
	printf("%s\n", t);
}
