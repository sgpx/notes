#include <stdio.h>

int inside_comment = 0;
int inside_string = 0;

int main() {
	char c;
	while ((c = getchar()) != EOF) {
		if(c == '"'){
			if(inside_comment == 0){
				inside_string = !inside_string;
				putchar(c);
				continue;
			}
		}

		if(inside_string == 0 && inside_comment == 0 && c == '/'){
			c = getchar();
			if(c == '*'){
				if(inside_string == 0) {
					inside_comment = 1;
					continue;
				}
			}
			else {
				putchar('/');
				putchar(c);
				continue;
			}
		}

		if(inside_string == 0 && inside_comment == 1 && c == '*'){
			c = getchar();
			if(c == '/'){
				if(inside_string == 0) {
					inside_comment = 0;
					continue;
				}
			}
			else {
				putchar('*');
				putchar(c);
				continue;
			}
		}
		if(inside_comment == 0)
			putchar(c);
	}
}
