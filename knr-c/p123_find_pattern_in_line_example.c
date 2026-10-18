#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
#define LINE_LENGTH 1000

int x_getline(char *s, int len){
        char *p = s, c;
        while((c = getchar()) != '\n' && p - s < len) *p++ = c;
        *p = '\0';
        return p-s;
}

int main(int argc, char **argv){
    if(argc == 1)
    {
        printf("usage: find -n -x pattern\n");
        return 1;
    }
    char pattern[LINE_LENGTH], line[LINE_LENGTH];

    int number = 0, except = 0;
    for(int i = 0; i < argc; i++)
        if(strcmp("-n", argv[i]) == 0) number = 1;
        else if(strcmp("-x", argv[i]) == 0) except = 1;
        else strcpy(pattern, argv[i]);

    int ln = 0;
    while(x_getline(line, LINE_LENGTH) > 0){
        ln++;
        if((strstr(line, pattern) != NULL) != except){
            if(number) printf("line number : %d", ln);
            printf("%s\n", line);
        }
    }
    return 0;
}