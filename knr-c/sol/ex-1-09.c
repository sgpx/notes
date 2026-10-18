#include <stdio.h>

int main() {
	char c;
	while( (c=getchar()) != EOF){
		if(c == ' ') {
			while(c == ' ') c = getchar();
			putchar(' ');
		}
		putchar(c);
	}
	return 0;
}
