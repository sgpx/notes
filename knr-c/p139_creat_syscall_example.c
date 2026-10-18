#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#define SZ 10

int main(){
	char *fn = "a.txt";
	int creat_res = creat(fn, 0666);
	if(creat_res != -1){
		printf("creat() ok\n");
	}
	int flags = O_WRONLY;
	int fd = open(fn, flags);
	char s[SZ] = "abcdabcdab";
	write(fd, s, SZ);
	close(fd);
}