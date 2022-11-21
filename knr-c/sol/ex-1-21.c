#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define TAB_SIZE 8

/*
abc\tx
abc	x
abc*****x

abc\t\tx
abc		x
abc*************x
*/

void entab(char s[], char p[]){
	int cs = 0, cp = 0, space_ctr = -1;
	while(s[cs] != '\0'){
		printf("cs : %d, s[cs] : '%c'\n", cs, s[cs]);
		if(cs % TAB_SIZE == 0 && space_ctr != -1){
			printf("cs : %d, space_ctr : %d\n", cs, space_ctr);
			if(cs - space_ctr > 1){
				p[cp++] = '\t';
			}
			else {
				p[cp++] = ' ';
			}
			space_ctr = -1;
		}
		// ====
		if(s[cs] == ' ') {
			if(space_ctr == -1) space_ctr = cs;
			cs++;
		}
		else {
			if(space_ctr != -1){
				int qref = cs - space_ctr;
				while(qref--) p[cp++] = ' ';
				space_ctr = -1;
			}
			p[cp++] = s[cs++];
		}
	}
	p[cp] = '\0';
}
	/*

int main(){
	char s[1024] = "abc     asdfsd          sssa", p[1024];
	entab(s, p);
	printf("s :\n%s\n", s);
	printf("p :\n%s\n", p);
	printf("abc\td\n");
	return 0;
}
	*/

int main(){
	char s[1024] = "axx	dwfwwkn wweank wew knk w   wknr w 	s		nkwnfw";
	char q[1024] = "axx     dwfwwkn wweank wew knk w   wknr w       s               nkwnfw";
	char qref[1024] = "axx.....dwfwwkn wweank wew knk w   wknr w ......s...............nkwnfw";

	char ans[1024];
	entab(q, ans);
	printf("%s\n", s);
	printf("%s\n", qref);
	printf("%s\n", q);
	printf("%s\n", ans);

}
