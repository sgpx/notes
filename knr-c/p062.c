#include <stdio.h>
#include <ctype.h>

double atof(char s[]){
	double val = 0 , power = 0;
	int sign = s[0] == '-' ? -1 : 1;
	int pm = 0;

	for(int i = 0; s[i] != '\0'; i++){
		if(i == 0 && s[i] == '-') continue;
		else if(s[i] >= '0' && s[i] <= '9'){
			val = val * 10;
			val = val + (s[i] - '0');

			if(pm == 1) ++power;
		}
		else if(s[i] == '.'){
			pm = 1;
		}
	}

	for(int i = 0; i < power; i++){
		val = val / 10;
	}

	return val;
}

int main(){
	char s[20] = "112312.12311";
	double d = atof(s);
	printf("%f\n", -d);
	return 0;
}
