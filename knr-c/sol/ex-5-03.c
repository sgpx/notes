#include <stdio.h>

void x_strcat(char * s, char * t){
	while(*s != '\0') ++s;
	while(*t != '\0') *s++ = *t++;
	*s = '\0';
}

int main(){
	char s[15] = "foobar";
	char t[5] = "baz";
	x_strcat(s, t);

	printf("%s\n", s);

	return 0;

}
