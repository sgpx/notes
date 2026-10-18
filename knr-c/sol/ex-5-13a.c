#include <stdio.h>
#include <string.h>

void x_set(char x[], char y[]){
	printf("setting %s into %s\n", y, x);
	int i;
	for(i = 0; y[i] != '\0'; i++)
		x[i] = y[i];
	x[i] = '\0';
}

void swap(char x[], char y[]){
	printf("swapping %s with %s\n", x, y);
	char p[100];
	int i;
	for(i=0; x[i] != '\0'; i++)
		p[i] = x[i];
	p[i] = '\0';
	for(i=0; y[i] != '\0'; i++)
		x[i] = y[i];
	x[i] = '\0';
	for(i=0; p[i] != '\0'; i++)
		y[i] = p[i];
	y[i] = '\0';


}

int x_getline(char s[]){
	printf("---\n");

	char c;
	int i = 0;
	while((c = getchar())!= '\n')
		s[i++] = c;
	s[i] = '\0';
	printf("x_getline : %s\n", s);
	return i-1;
}

int zmain(){
	char s[10] = "lmeoe";
	char t[10] = "elele";
	printf("%s %s\n", s, t);
	swap(s, t);
	printf("%s %s\n", s, t);
}

int main(){
	char a[5][100];
	for(int u = 0; u < 5; u++) a[u][0] = '\0';
	char s[100];
	int len, i = 0;
	while( (len = x_getline(s)) > 0){
// 5 4
// 4 3
// 3 2
// 2 1
// 1 0
		// bugged implementation, find why
		//int k = i < 5 ? i : 5;
		int k = i < 5 ? i : 4;
		printf("i : %d, k : %d\n", i, k);
		for(int j = k; j > 0; j--)
			swap(a[j], a[j-1]);
		x_set(a[0], s);
		printf("s : %s\n", s);
		s[0] = '\0';
		i++;
		for(int j = 0; j < 5; j++)
			printf("%d : %s\n", j, a[j]);
	}
	printf("final :\n");
	for(int j = 4; j >= 0; j--)
		printf("%d : %s\n", j, a[j]);

}
