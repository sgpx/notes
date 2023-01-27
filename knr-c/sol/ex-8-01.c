/*
mac os resources

https://opensource.apple.com/source/xnu/xnu-201/bsd/sys/errno.h
https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/read.2.html
https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/open.2.html
https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/stat.2.html
https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man2/write.2.html

linux resources

https://man7.org/linux/man-pages/man2/open.2.html
https://man7.org/linux/man-pages/man2/read.2.html
https://linux.die.net/man/2/stat
https://man7.org/linux/man-pages/man2/write.2.html
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>
#include <sys/errno.h>

void printfile(char *fn)
{
	int fd = open(fn, O_RDONLY);
	if (fd != -1)
	{
		unsigned long long size_in_bytes = 1000L;
		struct stat statres;
		int statout = stat(fn, &statres);
		if (statout == -1)
		{
			printf("error: couldn't stat %s", fn);
			return;
		}

		off_t sts = statres.st_size;
		size_in_bytes = (unsigned long long)sts;
		char *buf = (char *)malloc(size_in_bytes);
		read(fd, buf, size_in_bytes);
		write(STDOUT_FILENO, buf, size_in_bytes);
	}
	// ssize_t rs = read(fd, buf, 1000);
	// printf("%ld\n", rs);
	else
	{
		printf("%s : no such file or directory", fn);
	}
	close(fd);
}

int main(int argc, char *argv[])
{
	if (argc == 1)
	{
		char c = getchar();
		while(c != EOF){
			putchar(c);
			c = getchar();
		}
	}
	else
		for (int i = 1; i < argc; i++)
			printfile(argv[i]);
	return 0;
}