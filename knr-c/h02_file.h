#define X_NULL 0
#define X_EOF (-1)
#define X_BUFSIZ 1024
#define X_OPEN_MAX 20

typedef struct _iobuf
{
    int cnt;
    char *ptr;
    char *base;
    int flag;
    int fd;
} X_FILE;

X_FILE _iob[X_OPEN_MAX];

#define X_stdin (&_iob[0])
#define X_stdout (&_iob[1])
#define X_stderr (&_iob[2])

enum X_flags
{
    _READ = 01,
    _WRITE = 02,
    _UNBUF = 04,
    _EOF = 010,
    _ERR = 020,
};

int X_fillbuf(X_FILE *);
int X_flushbuf(X_FILE *);

#define X_feof(p) (((p)->flag & _EOF) != 0)
#define X_ferror(p) (((p)->flag & _EOF) != 0)
#define X_fileno(p) ((p)->fd)
#define X_getc(p) ((--(p)->cnt >= 0) ? (unsigned char)*(p)->ptr++ : X_fillbuf(p))
#define X_putc(x, p) (--(p)->cnt >= 0 ? *(p)->ptr++ = x : X_flushbuf((x), p))
#define X_getchar() X_getc(X_stdin)
#define X_putchar(x) X_putc((x), X_stdout)