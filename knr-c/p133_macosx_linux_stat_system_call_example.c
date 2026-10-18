#include <stdio.h>
#include <sys/stat.h>

int main(){
        struct stat s1;
        int res = stat("a.c", &s1);
        printf("%d\n", res);
        #ifdef __APPLE__
        printf("%lld\n", s1.st_size);
        #elif __linux__
        printf("%ld\n", s1.st_size);
        #endif
}