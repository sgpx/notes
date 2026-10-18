#include <stdio.h>

int main() {
	char c;
	while( (c=getchar()) != EOF){
		if(c == ' ') {
			while(c == ' ') c = getchar();
			putchar(' ');
			putchar(c);

		}
		else if(c == '\t'){
			putchar('\\');
			putchar('t');
		}
		else if(c == '\b'){
			putchar('\\');
			putchar('b');
		}
		else if(c == '\n'){
			putchar('\\');
			putchar('n');
		}
		else
			putchar(c);
	}
	return 0;
}
