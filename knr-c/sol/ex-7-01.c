#include <stdio.h>
#include <string.h>

char x_toupper(char x) {
    return x >= 'a' && x <= 'z' ? x - 'a' + 'A' : x;
}

char x_tolower(char x) {
    return x >= 'A' && x <= 'Z' ? x - 'A' + 'a' : x;
}

int main(int argc, char ** argv){
    char *p = argv[1];
    char (*fn)(char) = strcmp(argv[0], "./toupper") ? x_tolower : x_toupper;
    while(*p != '\0') {
        printf("%c", fn(*p));
        ++p;
    }
    return 0;
}
