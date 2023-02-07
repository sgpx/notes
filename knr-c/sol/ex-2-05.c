#include <stdio.h>

int any(char s1[], char s2[]){
	int arr[500];
	for(int i = 0; i < 500; i++) arr[i] = 0;
	for(int i = 0; s2[i] != '\0'; i++) arr[s2[i]] = 1;
	int i = 0;
	while(s1[i] != '\0'){
		char c = s1[i];
		int cond = (arr[c] == 1);
		if(cond) return i;
		++i;
	}
	return -1;
}

int main(){
	//char s1[] = "asdasfasfbbbdasdFzxvz24r", s2[] = "asdfb";
	char s1[] = "element", s2[] = "t";
	printf("%s %s %d\n", s1, s2, any(s1, s2));
	return 0;
}
