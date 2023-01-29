#include <stdio.h>
#include <unistd.h>
#define BUFSIZE 10

int getchar(void){
	static char buf[BUFSIZE];
	static char *bufp = buf;
	static int n = 0;

	if(n == 0){
		n = read(0, buf, sizeof(buf));
		bufp = buf;
	}
	return (--n >= 0) ? (unsigned char) *bufp++ : EOF;

}

int main(int argc, char *argv[])
{
	char c;
	while((c = getchar()) != EOF){
		printf("%c", c);
	}
	return 0;
}
