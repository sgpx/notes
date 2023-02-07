#include <stdio.h>

void squeeze(char s1[], char s2[]){
	int arr[500];
	for(int i = 0; i < 500; i++) arr[i] = 0;
	for(int i = 0; s2[i] != '\0'; i++) arr[s2[i]] = 1;
	int i = 0, ctr = 0;
	while(s1[i] != '\0'){
		char c = s1[i];
		if(arr[c] == 0){
			s1[ctr++] = s1[i];
		}
		++i;
	}
	s1[ctr] = '\0';
}

int main(){
	//char s1[] = "asdasfasfbbbdasdFzxvz24r", s2[] = "asdfb";
	char s1[] = "element", s2[] = "el";
	printf("%s %s\n", s1, s2);
	squeeze(s1, s2);
	printf("%s %s\n", s1, s2);
	return 0;
}
