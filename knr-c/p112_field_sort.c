#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define INPUT_SIZE 6
#define FIELDSIZE 100
#define MAXFIELDS 100
#define SEP '#'

typedef int (*fn)(const void*,const void*);

int sort_order[MAXFIELDS];
int number_of_fields = 0;

void get_field(char *s, int num, char *res){
	char tmp[FIELDSIZE];
	int fc = 1, ctr = 0;
	char *p = s;
	while(*p != '\0'){
		char c = *p;
		if(c == SEP){
			if(fc == num){
				printf("breaking..\n");
				break;
			}
			else {
				++fc;
				ctr = 0;
				tmp[0] = '\0';
			}
		}
		else {
			tmp[ctr++] = c;
		}
		p++;
		//printf("tmp: '%s'\n", tmp);

	}
	tmp[ctr++] = '\0';
	strcpy(res, tmp);
}


int compare(char * a, char * b){
	printf("comparing '%s' and '%s'\n", a, b);
	char tmp1[FIELDSIZE], tmp2[FIELDSIZE];
	for(int i = 0; i < MAXFIELDS; i++){
		int target_field = sort_order[i];
		if(target_field){
			get_field(a, target_field, tmp1);
			get_field(b, target_field, tmp2);
			int res = strcmp(tmp1, tmp2);
			printf("compare res : %d\n", res);
			if(res != 0)
				return res;
			else {
				tmp1[0] = '\0';
				tmp2[0] = '\0';
				continue;
			}
		}
		else break;
	}
	return 0;
}


int get_number_of_fields(char *s){
	char tmp[FIELDSIZE];
	int res = 1;
	for(char *p = s; *p != '\0'; p++)
		if(*p == SEP) ++res;

	return res;
}

int main(int argc, char *argv[]){
	for(int i = 0; i < MAXFIELDS; i++) sort_order[i] = 0;
	int sctr = 0;
	for(int i = 1; i < argc; i++) {
		char *tmp = argv[i];
		int x = (int)atof(tmp);
		if(x < 0) x = -x;
		sort_order[sctr++] = x;
	}

	for(int i = 0; i < MAXFIELDS; i++)
		if(sort_order[i])
			printf("order: %d, field: %d\n", i, sort_order[i]);

	char s[INPUT_SIZE][100] = {
		"3 # b # f",

		"1 # a # c",
		"3 # a # e",

		"2 # a # c",
		"1 # b # e",
		"2 # c # f",


	};
	number_of_fields = get_number_of_fields(s[0]);
	printf("number of fields : %d\n", number_of_fields);

	char sample[50] = "aa # ab # ac", res[50];
	int fnum = 3;
	get_field(sample, fnum, res);
	printf("field %d : '%s'\n", fnum, res);
	fn tf = (fn) compare;
	for(int i = 0; i < INPUT_SIZE; i++)
		printf("%d : '%s'\n", i, s[i]);
	printf("\n\n\n");
	qsort(s, INPUT_SIZE, sizeof(s[0]), tf);
	for(int i = 0; i < INPUT_SIZE; i++)
		printf("%d : '%s'\n", i, s[i]);
}
