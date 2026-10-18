#include <stdio.h>

void reverse(char s[], int i, int len){
	if(i < len/2){
		reverse(s, i+1, len);
		char tmp = s[i];
		int target = len - 1 - i;
		s[i] = s[target];
		s[target] = tmp;
	}
	else return;
}

int main(){
	char s[10] = "abcdefg";
	printf("s: '%s'\n", s);

	reverse(s, 0, 7);
	printf("s: '%s'\n", s);

	return 0;
}
