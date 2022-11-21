#include <stdio.h>

int escape(char s[], char t[]){
	int cs = 0, ct = 0;
	while(s[cs] != '\0'){
		if(s[cs] == '\n' || s[cs] == '\t') {
			t[ct] = '\\';
			t[ct+1] = s[cs] == '\n' ? 'n' : 't'; 
			ct += 2;
			++cs;
		}
		else{ t[ct++] = s[cs++]; }
	}
}

int main(){
	char s[10] = "lmao\tlol";
	char t[10];
	escape(s,t);
	printf("%s\n", t);
}
