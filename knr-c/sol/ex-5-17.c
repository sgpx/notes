#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define SEP '#'
#define MAXARG 100
#define ARGLEN 100
#define MAXLINES 1000
typedef int (*fn) (const void*, const void*);

int isnumber(char c){
	return (c >= '0' && c <= '9');
}

char **xarg;
int xargctr;

char lineptr[MAXLINES][1000];

char lower(char x){
        if(x >= 'A' && x <= 'Z') return (x - 'A' + 'a');
        else return x;
}

char donothing(char x){ return x; }

int x_strcmp(char *a, char *b, int fold, int dir){
        char (*cmpx)(char) = fold ? lower : donothing;
	if(dir){
		while(*a == ' ') a++;
		while(*b == ' ') b++;
	}
        while(cmpx(*a) == cmpx(*b)){
		if(*a == ' '){ a++; continue; }
		if(*b == ' '){ b++; continue; }
                if(*a == '\0') return 0;
                a++;
                b++;
        }
	if(dir){
		while(*a == ' ') a++;
		while(*b == ' ') b++;
	}
        return cmpx(*a) - cmpx(*b);
}




void get_field(char *a, int fd, char *tmp){
	char *p = a;
	int fc = 1, tc = 0;
	while(*p != '\0'){
		if(*p == SEP){
			if(fc == fd) break;
			else {
				tmp[0] = '\0';
				tc = 0;
				p++;
				fc++;
			}
		}
		else tmp[tc++] = *p++;
	}
	tmp[tc] = '\0';
}

int get_fnum(char *x){
	char tmp[100];
	char * t2 = tmp;
	for(int i = 0; x[i] != '\0'; i++){
		printf("%c\n", x[i]);
		printf("'%s'\n", tmp);
		if(  x[i] == '-' || isnumber(x[i]) )
			*(t2++) = x[i];
		else if( x[i] == ' ' ) continue;
		else break;
	}
	*t2 = '\0';
	printf("%s\n", tmp);
	int res = atoi(tmp);
	if (res < 0) return  -res;
	else if (res > 0) return res;
	else return -1;
}

int compare(char * a, char * b){
	printf("comparing : '%s' with '%s'\n", a, b);
	int cctr = 1;
	while(cctr < xargctr){
		char * cfmt = *(xarg+cctr);
		int reverse = 0, numeric = 0, fold = 0, dirmode = 0;
		int fnum = -1;
		int ftmpctr = 0, sotmpctr = 0;
		char ftmp[100], sotmp[100];
		while(*cfmt != '\0'){
			printf("ftmp : '%s'\n", ftmp);
			printf("cfmt : '%c'\n", *cfmt);
			if(*cfmt == ' ') cfmt++;
			else if(*cfmt == '-')
				ftmp[ftmpctr++] = *cfmt++;
			else if(*cfmt >= '0' && *cfmt <= '9')
				ftmp[ftmpctr++] = *cfmt++;
			else {
				if(*cfmt == 'n') numeric = 1;
				else if(*cfmt == 'r') reverse = 1;
				else if(*cfmt == 'd') dirmode = 1;
				else if(*cfmt == 'f') fold = 1;
				cfmt++;
			}
		}
		ftmp[ftmpctr] = '\0';
		fnum = atoi(ftmp);
		fnum = fnum > 0 ? fnum : -fnum;
		printf("fnum : %d\n", fnum);
		if(fnum > 0){
			printf("numeric : %d\n", numeric);
			printf("reverse : %d\n", reverse);
			printf("fold : %d\n", fold);
			printf("dirmode : %d\n", dirmode);
			int res = 0;
			char sa[100], sb[100];
			get_field(a, fnum, sa);
			get_field(b, fnum, sb);
			printf("sa : %s\n", sa);
			printf("sb : %s\n", sb);
			if(numeric == 0){
				double da = atof(sa);
				double db = atof(sb);
				if(da == db) res = 0;
				else if(da > db) res = 1;
				else if(da < db) res = -1;
			}
			else {
				res = x_strcmp(sa, sb, fold, dirmode);
			}
			if(reverse == 1) res = -res;
			if(res != 0) return res;
		}
		++cctr;
	}
	return 0;
}

int x_getline(char *s){
	char *p = s;
	while( (*p = getchar()) != '\n') ++p;
	*p = '\0';
	return p - s;
}

int main(int argc, char * argv[]){
	xargctr = argc;
	xarg = argv;
	char s[1000];
	int len, ctr = 0;
	while((len = x_getline(s)) > 0){
		printf("len : %d\ns : %s\n", len, s);
		strcpy(lineptr[ctr], s);
		++ctr;
	}
	for(int i = 0; i < ctr; i++)
		printf("%d : '%s'\n", i, lineptr[i]);

	fn fc = (fn)compare;
	qsort(lineptr, ctr, sizeof(lineptr[0]), fc);

	for(int i = 0; i < ctr; i++)
		printf("%d : '%s'\n", i, lineptr[i]);

	return 0;
}

