#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <sys/dir.h>
#include <sys/types.h>
#include <sys/errno.h>
#include <dirent.h>
#include <string.h>
#include <stdarg.h>

#define PERMS 0666
#define FSEEK_OK 0
#define FSEEK_ERROR 1

typedef struct dirent Dirent;

void x_sprintf(char *zbuf, char *fmt, ...){
	va_list ap;
	va_start(ap, fmt);
	char *z = zbuf;
	char *p;
	for(p = fmt; *p != '\0'; p++){
		if(*p == '%'){
			char *param = va_arg(ap, char*);
			for(char *q = param; *q != '\0'; q++){
				*z++ = *q;
			}
		}
		else *(z++) = *p;
	}
	*z = '\0';
}



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

void x_print_digit(int x){
	if(x >= 0 && x <= 9) x_print_char('0' + x);
}

void x_print_number(long long z)
{
	int q[1024], ctr = 0;
	if (z < 0)
	{
		z = -z;
		x_print_char('-');
	}
	while (z)
	{
		int rem = z % 10;
		q[ctr++] = rem;
		z -= rem;
		z /= 10;
	}
	for(int i = ctr - 1; i >= 0; i--){
		x_print_digit(q[i]);
	}
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
		x_print_char('0' + q[i]);
	x_print_str("\n");
}

void x_printf(char *fmt, ...){
	va_list ap;
	va_start(ap, fmt);
	char *p;
	for(p = fmt; *p != '\0'; p++){
		if(*p == '%'){
			if(*(p+1) == 'd'){
				long long dval = (long long) va_arg(ap, long long);
				x_print_number(dval);
				x_print_char(' ');
				++p;
				continue;
			}
			else if(*(p+1) == 's'){
				char *sval = va_arg(ap, char*);
				x_print_str(sval);
				x_print_char(' ');
				++p;
				continue;
			}
			else {
				x_print_char('%');
			}
		}
		else x_print_char(*p);
	}
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

void fclose(FILE *fp)
{
	close(fp->fd);
	// free(fp);
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

void test_echo()
{
	// x_print_str("lol\n");
	char c;

	while ((c = getchar()) != 'z')
	{
		putchar(c);
	}
}

int fflush(FILE *fp)
{
	if (fp->file_flag.read == 0)
	{
		// size_t sz = fp->ptr - fp->base;
		write(fp->fd, fp->base, fp->cnt);
		fp->cnt = 0;
	}
	return 0;
}

FILE *fopen(char *name, char *mode)
{
	int fd;
	FILE *fp;

	if (*mode != 'r' && *mode != 'w' && *mode != 'a')
		return NULL;

	int i;
	for (i = 3; i < OPEN_MAX; i++)
	{
		fp = &_iob[i];
		if (fp->file_flag.read == 0 && fp->file_flag.write == 0)
			break;
	}
	if (*mode == 'w')
	{
		fd = creat(name, PERMS);
	}

	else if (*mode == 'a')
	{
		if ((fd = open(name, O_WRONLY, 0)) == -1)
		{
			fd = creat(name, PERMS);
		}
		// lseek(fd, 0L, 2);
	}
	else
	{
		x_print_str("readonly\n");
		fd = open(name, O_RDONLY, 0);
	}
	if (fd == -1)
		return NULL;
	fp->fd = fd;
	fp->cnt = 0;
	fp->base = NULL;

	if (*mode == 'r')
		fp->file_flag.read = 1;
	else
		fp->file_flag.write = 1;

	return fp;
}

int fread(char *buf, size_t sz, FILE *fp)
{
	fp->cnt -= read(fp->fd, buf, sz);
	return 0;
}

int fseek(FILE *fp, long offset, int origin)
{
	int r = lseek(fp->fd, offset, origin);
	if (r == -1)
		return FSEEK_ERROR;
	else
		return FSEEK_OK;
	// if(origin == 0){
	// 	// SEEK START
	// 	fp->ptr = fp->base + offset;
	// 	fp->cnt = (fp->ptr + fp->cnt - fp->base - offset);
	// }
	// else if(origin == 1){
	// 	// SEEK
	// 	fp->ptr += offset;
	// 	fp->cnt -= offset;
	// }
	// else if(origin == 2){
	// 	// SEEK END
	// 	fp->ptr = fp->ptr + fp->cnt - offset;
	// 	fp->cnt = offset;
	// }
	// fp->base = fp->ptr;
}

void test_fopen()
{
	FILE *fp = fopen("Makefile", "r");
	char zbuf[4096] = "initstr";
	fread(zbuf, 4096, fp);
	x_print_str(zbuf);
	fclose(fp);
}

void test_fseek()
{
	FILE *fp = fopen("Makefile", "r");
	char zbuf[4096] = "initstr";
	fseek(fp, 15, 0);
	fread(zbuf, 4096, fp);
	x_print_str(zbuf);
	fclose(fp);
}

void test_number_print(){
	x_print_number(-40424234);
}

void dirwalk(char *dirname, void (*fxn)(char *)){
	DIR *dfd = opendir(dirname);
	Dirent *dp;
	if(dfd == NULL) return x_printf("error opening dir : %s\n", dirname);
	while((dp = readdir(dfd)) != NULL){
			if(strcmp(dp->d_name, ".") == 0 || strcmp(dp->d_name, "..") == 0){
				continue;
			}
			// x_printf("dirname : %s\n", dp->d_name);
			char nbuf[1024];
			x_sprintf(nbuf, "%/%", dirname, dp->d_name);
			fxn(nbuf);
	}
}

void fsize(char *name){
	struct stat stbuf;
	if(stat(name, &stbuf) == -1){
		x_print_str("fsize: can't access ");
		x_print_str(name);
		return;
	}
	if((stbuf.st_mode & S_IFMT) == S_IFDIR){
		dirwalk(name, fsize);
	}
	// x_print_number((long long)stbuf.st_size);
	// x_print_str(" ");
	// x_print_str(name);
	// x_print_char('\n');
	x_printf("name : %s\n", name);
	x_printf("size : %d\n", (long long)stbuf.st_size );
	x_printf("inode number : %d\n", (long long)stbuf.st_ino );
	x_printf("mode : %d\n", (long long)stbuf.st_mode );
	x_printf("number of links to file : %d\n", (long long)stbuf.st_nlink );
	x_printf("owner group id : %d\n", (long long)stbuf.st_gid );
	x_printf("owner user id : %d\n", (long long)stbuf.st_uid );
	x_printf("rdev : %d\n", (long long)stbuf.st_rdev );
	x_printf("last modified : %d\n", (long long)stbuf.st_mtim.tv_sec );
	x_printf("last accessed : %d\n", (long long)stbuf.st_atim.tv_sec );
	x_printf("last originally created : %d\n", (long long)stbuf.st_ctim.tv_sec );
	x_print_char('\n');
}

void test_fsize(){
	// fsize("Makefile");
	fsize("abc");
}

void test_sprintf()
{
	char a[200] = "", b[10] = "ok", c[10] = "lol";
	x_sprintf(a, "%/%", b, c);
	x_print_str(a);
}

int main(){
	test_fsize();
	return 0;
}
