#include <stdio.h>
#define IS_PRINTABLE(x)( x >= 32 && x <= 127 )
#define ADDBREAK(i) ((i % LINE_WIDTH == 0) && i)
#define LINE_WIDTH 10

int main(){
    for(int i = 0, c = 0; (c = getchar()) != EOF; i++)
        printf(IS_PRINTABLE(c) ? (ADDBREAK(i) ? "%c\n" : "%c") : (ADDBREAK(i) ? "{0x%02x}\n" : "{0x%02x}"), c);
    return 0;
}
