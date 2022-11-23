#include <stdio.h>
#include <string.h>

int main(){
        char *x[5000];
        char p[100];
        strcpy(p, "lol");
        x[0] = p;
        printf("%s\n", x[0]);
}
