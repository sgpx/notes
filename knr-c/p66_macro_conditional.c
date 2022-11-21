#include <stdio.h>
#define X 5

#ifdef X
#define Y 7
#endif

int main(){
        printf("%d\n", X+Y);
        return 0;
}
