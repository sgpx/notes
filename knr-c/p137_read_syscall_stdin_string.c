#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/errno.h>

int main(int argc, char *argv[]){
	char * c = (char*)malloc(100);
	read(0, c, 5);
	printf("'%s'\n", c);
	return 0;
}

