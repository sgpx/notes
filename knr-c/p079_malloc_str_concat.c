#include <stdio.h>
#include <stdlib.h>

int x_strlen(char * x){
	int ctr;
	while( *(x+ctr) != '\0' ) ++ctr;
}

char * concat(char * a, char * b){
	int newlength = x_strlen(a) + x_strlen(b);
	char * p = (char *)malloc(newlength * sizeof(char));
	char * ref = p;
	while( *a != '\0' ) *p++ = *a++;
	while( *b != '\0' ) *p++ = *b++;
	*p = '\0';
	return ref;
}

int main(){
	char * a = "abcd";
	char * b = "efghijklmnop";
	char * c = concat(a, b);
	printf("%s\n", c);
	return 0;
}
