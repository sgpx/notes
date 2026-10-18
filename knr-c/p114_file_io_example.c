#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){
	FILE* fptr = fopen("a.c", "r");
	fseek(fptr, 0L, SEEK_END);
	size_t sz = (size_t)ftell(fptr);
	fseek(fptr, 0L, SEEK_SET);
	printf("sz : %d\n", sz);

	char * buf = (char*)malloc(sz + 1);
	fread(buf, 1, sz, fptr);
	fclose(fptr);
	*(buf + sz) = '\0';
	printf("%s\n", buf);

	return 0;
}
