#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define PAGE_HEIGHT 50
#define LINE_WIDTH 1000

int page_number = 0;

void xprint(FILE *fp)
{
    page_number += 1;
    int i;
    char buf[LINE_WIDTH], *xyz;
    for (i = 0; i < PAGE_HEIGHT; i++)
    {
        xyz = fgets(buf, LINE_WIDTH, fp);
        int buflen = strlen(buf);
        if (xyz == NULL)
            printf("\n%d: ", i+1);
        else
            printf("%d: %s", i+1, buf);
    }
    printf("\n===\npage number : %d\n===\n", page_number);

    if (xyz != NULL)
        xprint(fp);
    else
        printf("\n");
}

int xproc(char **argv, int argc, int i)
{
    if (i >= argc)
        return 0;

    char * filename = argv[i];
    FILE *fp = fopen(filename, "r");
    if (fp != NULL)
    {
        xprint(fp);
    }
    return xproc(argv, argc, i + 1);
}

int main(int argc, char **argv)
{
    if (argc < 2)
    {
        printf("error: not enough arguments\n");
        return 1;
    }

    /*
    1. get next file contents
    2. print lines until end of file OR page height full
    3. if end of file and page height remaining, fill with blanks, goto step1
    4. if end of file and page height not remaining, do nothing, goto step1
    5. if page height full and file data remaining, increment page number, goto step2
    */
    xproc(argv, argc, 1);

    return 0;
}