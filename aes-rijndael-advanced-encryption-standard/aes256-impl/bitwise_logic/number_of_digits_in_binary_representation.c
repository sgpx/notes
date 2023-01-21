#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

double log_base_2(double x){
	return log(x)/log(2);
}

void reverse(char * buf){
	int len = strlen(buf);
	for(int i = 0; i < len/2; i++){
		char tmp = buf[len - i - 1];
		buf[len - i - 1] = buf[i];
		buf[i] = tmp;
	}
}

void to_bin(int i, char * buf){
	int a = i, ctr = 0;
	while(a){
		int rem = a % 2;
		buf[ctr++] = '0' + rem;
		a -= rem;
		a /= 2;
	}
	buf[ctr] = '\0';
	reverse(buf);
}

int main(){
	for(int i = 1; i <= 10000; i++){
		int est = 1 + ((int)log_base_2(i));
		char *buf = (char *)malloc(est + 1); // + 1 for \0
		to_bin(i, buf);
		/*
		printf("i : %d\n", i);
		printf("buf : %s\n", buf);
		printf("est : %d\n", est);
		printf("strlen : %ld\n", strlen(buf));
		*/
		if(est != strlen(buf)){
			printf("failed at %d, est : %d, len : %ld\n", i, est, strlen(buf));
			break;
		}
		else printf("%d OK\n", i);
		free(buf);
	}
}
