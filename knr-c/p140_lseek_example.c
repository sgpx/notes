#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#define SZ 10

int main()
{
	int flags = O_RDONLY;
	char *fn = "a.txt";
	int fd = open(fn, flags);
	// char s[SZ];
	// read(fd, s, SZ);
	lseek(fd, -10, SEEK_END);
	char c;
	for (int i = 0; i < 10; i++)
	{
		read(fd, &c, 1);
		printf("c : %c\n", c);
		lseek(fd, -10+i+1, SEEK_END);
	}
	lseek(fd, 0, SEEK_SET);
	for(int i = 0; i < 10; i++){
		read(fd, &c, 1);
		printf("s : %c\n", c);
		lseek(fd, 1+i, SEEK_SET);
	}
	lseek(fd, 0, SEEK_SET);
	for(int i = 0; i < 3; i++){
		read(fd, &c, 1);
		printf("s : %c\n", c);
		if(i == 1)
			lseek(fd, i+5, SEEK_CUR);
		else
			lseek(fd, 1+i, SEEK_SET);
	}
	
	close(fd);
}