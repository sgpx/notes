/*

Description: Implement int safe_strcat(char *dest, size_t dest_cap, const char *src) preventing buffer overruns.

Requirements:

    Determine current length of dest.
    Append src up to dest_cap - 1 bytes total.
    Guarantee null-termination under all conditions.
    Return 0 on complete append, or -1 if truncated.

*/

#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int safe_strcat(char *dest, size_t dest_cap, const char *src) {
	if(src == NULL || dest == NULL) return -1;
	if(dest_cap == 0) {
		return -1;
	}
	size_t ld = strnlen(dest, dest_cap);
	size_t ls = strlen(src);
	if(ld >= dest_cap) {
		dest[dest_cap-1] = '\0';
		return -1;
	}
	if(ld == 0) {
		size_t i = 0;
		while (i < ls && i < dest_cap - 1) {
			*(dest + i) = *(src + i);
			i++;
		}
		*(dest + i) = '\0';
		return i == ls ? 0 : -1 ;
	}
	//printf("%zu %zu\n", ld, ls);
	size_t i = 0;
	while(ld + i < dest_cap - 1 && i < ls) {
		//printf("%zu %zu %zu %zu\n", ld, i, ld+i, dest_cap);
		*(dest+ld+i) = *(src+i);
		i++;
	}
	*(dest+ld+i) = '\0';
	return i == ls ? 0 : -1;
}

int main() {
	const char *src = "hello";
	char *dest = malloc(sizeof(char)*10);
	dest[0] = 'h';
	dest[1] = 'i';
	dest[2] = '\0';
	int rv = safe_strcat(dest, 10, src);
	printf("%s\n", dest);
	printf("%d\n", rv);
	return 0;
}
