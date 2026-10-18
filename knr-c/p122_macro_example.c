#include <stdio.h>
#include <string.h>
#define IS_PRINTABLE(x)( x >= 32 && x <= 127 )

int main(){
    printf("%d", IS_PRINTABLE(128));
    return 0;
}
