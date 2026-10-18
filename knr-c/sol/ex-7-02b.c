#include <stdio.h>
#define IS_PRINTABLE(x)( x >= 32 && x <= 127 )

int main(){
    char c;
    while( (c = getchar()) != EOF)
        printf(IS_PRINTABLE(c) ? "%c" : "{0x%02x}", c); 
    return 0;
}
