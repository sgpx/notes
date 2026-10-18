/*
Implement size_t strip_line_comments(char *src, char *dest) to filter out // comments using a do-while loop.

Requirements:

    Traverse buffer using do { ... } while (*src != '\0');.
    Skip characters from // until newline \n or \0.
    Do not strip // if inside a string literal "...".
    Null-terminate dest and return written length.

*/

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>

void dbg(int a) {
	printf("debug : %d\n", a);
}

bool is_comment_start(char *src) {
	if(*src == '\0') return false;
	return (*src == '/' && src[1] != '\0' && src[1] == '/');
}

bool is_quote(char *src, size_t pos) {
        if(*src == '"' && pos > 0) {
                size_t tmp = 1, bk_ctr = 0;
                while(tmp <= pos && *(src-tmp) == '\\') {
                        bk_ctr += 1;
                        tmp+= 1;
                }
                return (bk_ctr % 2) == 0;
        }
        else {
                return (*src == '"');

        }
}

bool is_newline(char *src) {
	return (*src == '\n');
}

size_t strip_line_comments(char *src, char *dest) {
	if (src == NULL || dest == NULL) {
		return 0; 
	}
	if(*src == '\0') {
		*dest = '\0';
		return 0;
	}
	char *orig_dest = dest, *orig_src = (char*)src;
	bool inside_comment = false, inside_literal = false;
	size_t cpos = 0;

	do {
		cpos = (size_t)(src - orig_src) ; 

		printf("S1 :: pos : %lu , char : '%c' , inside_comment : %d , inside_literal : %d\n", (size_t)(cpos), *src , inside_comment, inside_literal);
		if(inside_comment) {
			dbg(1);
			if(is_newline(src) == true) {
				*dest++ = *src++;
				inside_comment = false;
			dbg(2);

			}
			else {
			dbg(3);

				src++;
			}
		}
		else if(inside_literal) {
			dbg(4);
			if(is_comment_start(src)) {
			dbg(5);

				*dest++ = *src++;			
			} 
			else if(is_quote(src, cpos)) {
			dbg(6);

				*dest++ = *src++;			
				inside_literal = false;
			}
			else {
				*dest++ = *src++;			
			}
		}
		else if(!inside_comment && is_comment_start(src) && !inside_literal) {
			dbg(7);

			inside_comment = true;
			src++;
		}
		else if(is_quote(src, cpos) && !inside_literal && !inside_comment) {
			dbg(8);

			inside_literal = true;
			*dest++ = *src++;			
		}
		else {
			dbg(9);

			*dest++ = *src++;
		}
		printf("S2 :: inside_comment : %d , inside_literal : %d\n", inside_comment, inside_literal);
	}
	while(*src != '\0');
	*dest = '\0';
	return (size_t)(dest-orig_dest);
}

void chk(char *src) {
	size_t sz = strlen(src); // strlen excludes null terminator
	printf("\n---\n%lu\n", sz);
        char *dest = malloc(sizeof(char)*(sz+1));
        sz = strip_line_comments(src, dest);
        printf("src : %s\n===\n", src);
        printf("dest : %s\n===\n", dest);
	printf("%lu\n", sz);
	free(dest);
}

int main() {

    char *src1 = "foo//skipthis\n\"//dontskip\"bar";
	chk(src1);
	char *src2 = "a // say \"hi\"\nb";
	chk(src2); 
	char *src3 = "\"abc\\\"//not comment\"\n";
	chk(src3);
	return 0;
} 

