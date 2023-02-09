#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>

void x_print_str(char *pbuf)
{
	char *p = pbuf;
	for (p = pbuf; *p != '\0'; p++)
		;
	size_t bufsize = p - pbuf;
	write(0, pbuf, bufsize + 1);
}

void x_print_char(char c)
{
	char x[2];
	x[0] = c;
	x[1] = '\0';
	write(0, x, 2);
}

void x_print_ptr(void *ptr)
{
	unsigned long long z = (unsigned long long)ptr;
	int q[1024], ctr = 0;
	while (z > 0)
	{
		q[ctr++] = z % 10;
		z /= 10;
	}
	if (z == 0)
		x_print_str("NULL\n");
	for (int i = ctr - 1; i > -1; i--)
		x_print_char('0' + i);
	x_print_str("\n");
}

#define OPEN_MAX 20
struct flag_fields
{
	int read : 1;
	int write : 1;
	int unbuf : 1;
	int eof : 1;
	int error : 1;
};
typedef struct _iobuf
{
	int cnt;
	char *ptr;
	char *base;
	// int flag;
	struct flag_fields file_flag;
	int fd;
} FILE;

enum _flags
{
	_READ = 01,	 // 00001
	_WRITE = 02, // 00010
	_UNBUF = 04, // 00100
	_EOF = 10,	 // 01100
	_ERR = 020	 // 10100
};
#define BUFSIZE 1024

FILE _iob[OPEN_MAX] = {
	{0, (char *)0, (char *)0, {1, 0, 0, 0, 0}, 0},
	{0, (char *)0, (char *)0, {0, 1, 0, 0, 0}, 1},
	{0, (char *)0, (char *)0, {1, 0, 1, 0, 0}, 2}};

int _fillbuf(FILE *);
int _flushbuf(int, FILE *);

#define EOF -1
#define stdin &_iob[0]
#define stdout &_iob[1]
#define stderr &_iob[2]

#define getc(p) (--(p)->cnt >= 0 ? (char)*(p)->ptr++ : _fillbuf(p))
#define getchar() getc(stdin)
#define putc(x, p) (--(p)->cnt >= 0 ? *(p)->ptr++ = (x) : _flushbuf((x), p))
#define putchar(x) putc((x), stdout)

int _fillbuf(FILE *fp)
{
	size_t bufsize = BUFSIZE;
	// if ((fp->flag & (_READ | _EOF | _ERR)) != _READ)
	if (fp->file_flag.read == 0 || (fp->file_flag.eof || fp->file_flag.error || fp->file_flag.write))
		return EOF;
	// bufsize = (fp->flag & _UNBUF) ? 1 : BUFSIZE;
	bufsize = fp->file_flag.unbuf ? 1 : BUFSIZE;
	if (fp->base == NULL)
	{
		fp->base = (char *)malloc(bufsize);
	}
	fp->ptr = fp->base;
	fp->cnt = read(fp->fd, fp->ptr, bufsize);
	return (int)*(fp->ptr++);
}

int _flushbuf(int x, FILE *fp)
{
	// x_print_str("\nflushbuf\n");
	if (fp->base == NULL)
		fp->base = (char *)malloc(1);
	*(fp->base) = x;
	write(fp->fd, fp->base, 1);
	fp->base = NULL;
	return 0;
}

void check_eof()
{
	int x[5];
	read(0, x, 2);
	if (x[0] == -1)
		x_print_str("got eof\n");
	else
	{
		x_print_str("got something else\n");
		int y = x[0];
		if (y < 0)
		{
			x_print_str("-");
			y = -y;
		}
		if (y == 0)
			x_print_str("y is zero");
		while (y != 0)
		{
			int z = y % 10;
			y /= 10;
			x_print_char('0' + z);
			x_print_char('\n');
		}
	}
}

int main()
{
	// x_print_str("lol\n");
	char c;

	while ((c = getchar()) != 'z')
	{
		putchar(c);
	}
	return 0;
}
