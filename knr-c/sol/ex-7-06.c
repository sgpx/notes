#include <stdio.h>
#include <string.h>

int main(int argc, char **argv){
    if(argc < 2) return 1;
    char *fn1 = argv[1], *fn2 = argv[2];
    FILE *fp1 = fopen(fn1, "r"), *fp2 = fopen(fn2, "r");
    if(fp1 == NULL || fp2 == NULL) {
        printf("invalid filename(s)\n");
        return 1;
    }
    char buf1[1000], buf2[1000];

    int is_same = 1;

    // while(fgets(buf1, 1000, fp1) != NULL && fgets(buf2, 1000, fp2) != NULL) is_same = is_same && strcmp(buf1, buf2) == 0;
    char *p1, *p2;
    while((p1 = fgets(buf1, 1000, fp1)) != NULL && (p2 = fgets(buf2, 1000, fp2)) != NULL){ 
        printf("%p %p\n", p1, p2);
        is_same = is_same && strcmp(buf1, buf2) == 0;
        if(!is_same) break;
    }
    
    if(is_same) {
        printf("files are same\n");
    }
    else {
        printf("<%s\n>%s\n", buf1, buf2);
    }
    return 0;
}
