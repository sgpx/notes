#include <stdio.h>

int main(int argc, char **argv){
    char *fn1 = argv[1], *fn2 = argv[2];
    FILE *fp1 = fopen(fn1, "r"), *fp2 = fopen(fn2, "r");
    char buf1[1000], buf2[1000];

    while(fgets(buf1, 1000, fp1) != NULL) printf("line1 : %s\n", buf1);
    while(fgets(buf2, 1000, fp2) != NULL) printf("line2 : %s\n", buf2);
    return 0;
}
