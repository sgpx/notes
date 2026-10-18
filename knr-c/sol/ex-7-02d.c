#include <stdio.h>
#define IS_PRINTABLE(x)( x >= 32 && x <= 127 )
#define ADDBREAK(i) ((i % LINE_WIDTH == 0) && i)
#define LINE_WIDTH 10
#define GTMP(x)(IS_PRINTABLE(x) ? "%c" : "{0x%02x}")
#define GFMT(i, j, c)(j ? "" #c "\n" : c)
#define GXE(i, c) (GFMT(i, ADDBREAK(i), GTMP(c)))

int main(){ 
    for(int i = 0, c = 0; (c = getchar()) != EOF; i++)
        printf(GXE(i, c), c);
    return 0;
}
