#include <stdio.h>
#include "h02_file.h"
#define PERMS 0666
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

X_FILE *X_fopen(char *name, char *mode)
{
    X_FILE *fp; // = &_iob[0]; // = malloc(sizeof(X_FILE));
    int fd;
    printf("1. fp : %p\n", fp);
    if (*mode != 'r' && *mode != 'w' && *mode != 'a')
        return NULL;
    // fp = _iob;
    for (fp = _iob; fp < _iob + X_OPEN_MAX; fp++)
    {
        printf("2. fp : %p\n", fp);

        if (fp->flag && (_READ | _WRITE) == 0)
        {
            break;
        }
        printf("3. fp : %p\n\n\n", fp);
    }
    printf("4. fp : %p\n", fp);

    // if (fp >= _iob + X_OPEN_MAX)
    //     return NULL;
    if (*mode == 'w')
        fd = creat(name, PERMS);
    else if (*mode == 'a')
    {
        if ((fd = open(name, O_WRONLY, 0)) == -1)
        {
            fd = creat(name, PERMS);
        }
        lseek(fd, 0L, SEEK_END);
    }
    else
    {
        fd = open(name, O_RDONLY, 0);
        printf("%d", fd);
    }
    if (fd == -1)
    {
        return NULL;
    }
    fp->fd = fd;
    fp->cnt = 0;
    fp->base = NULL;
    fp->flag = (*mode == 'r') ? _READ : _WRITE;
    return fp;
}

int X_fread(char *buf, int sz, X_FILE *fp)
{
    return read(fp->fd, buf, sz);
}

int main()
{
    X_FILE *fp = X_fopen("a.txt", "r");
    printf("%p\n", fp);
    char zbuf[100] = "";
    X_fread(zbuf, 50, fp);
    printf("%s", zbuf);

    return 0;
}
