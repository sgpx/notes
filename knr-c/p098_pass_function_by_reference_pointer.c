#include <stdio.h>

int cmp(char *s, char *t){
	char *ps = s, *pt = t;
	while(1){
		if(*s != '\0') ++s;
		if(*t != '\0') ++t;
		if(*s == '\0' && *t == '\0') break;
	}
	printf("ls : %ld\n", s-ps);
	printf("lt : %ld\n", t-pt);
	return (s-ps) - (t-pt);
}

int exec(void *s, void *t, int (*fn)(char*,char*) ){
	char * rs = (char *)s;
	char * rt = (char *)t;
	int res = (int)fn(rs, rt);
	printf("res : %d\n", res);
}

int main(){
	char *x = "lel";
	char *y = "ok";
	exec(x, y, cmp);
	return 0;
}
