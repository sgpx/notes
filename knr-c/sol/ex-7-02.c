#include <stdio.h>
#define IS_PRINTABLE(x)( x >= 32 && x <= 127 )
#define LINE_WIDTH 10

int main(){
    char c;
    int lctr = 0;
    while( (c = getchar()) != EOF) {
        printf(IS_PRINTABLE(c) ? "%c" : "{0x%02x}", c); 
        if(lctr++ % LINE_WIDTH == 0 && lctr > 1) printf("\n");
    }
    return 0;
}
