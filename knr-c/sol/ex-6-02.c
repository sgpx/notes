#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#define KWLEN 9
#define NLEN 1000

int x_getline(char s[]){
	char *p = s;
	while( (*p++ = getchar()) != '\n');
	*(p-1) = '\0';
	//printf("%d\n", p-s-1);
	return p-s-1;
}

int nnc = 0;
char line[1000];
char name[100];
int inside_string = 0;

int substr(char s[], char t[], int n){
	int i;
	for(i = 0; i < n; i++) s[i] = t[i];
	s[i] = '\0';
}

/*
int find_next_name(void){
	int tctr = 0;
	name[0] = '\0';
	while(!isalpha(line[nnc]) && line[nnc] != '\0') nnc++;

	if(isalpha(line[nnc])){
		while(isalnum(line[nnc]) && line[nnc] != '\0')
			name[tctr++] = line[nnc++];
		name[tctr] = '\0';
	}
	return (line[nnc] != '\0');
}
*/


int find_next_name(void){
	int tctr = 0;
	name[0] = '\0';
	//while(!isalpha(line[nnc]) && line[nnc] != '\0') nnc++;
	while(1){
		if(line[nnc] == '\0') return 0;
		if(inside_string == 1){
			nnc++;
			continue;
		}
		else {
			if(isalpha(line[nnc])) break;
			else if(line[nnc] == '"' || line[nnc] == '\''){ inside_string = 1; nnc++; continue; }
			else {
				nnc++;
				continue;
			}
		}
	}

	if(isalpha(line[nnc])){
		while(isalnum(line[nnc]) && line[nnc] != '\0')
			name[tctr++] = line[nnc++];
		name[tctr] = '\0';
	}
	return (line[nnc] != '\0');
}

const char *keyword_list[KWLEN] = {
	"int",
	"float",
	"double",
	"unsigned",
	"long",
	"short",
	"const",
	"volatile",
	"struct",
};


int nlctr = 0;
char name_list[NLEN][NLEN];
int name_check_array[NLEN];

int is_keyword(char name[]){
	for(int i = 0; i < KWLEN; i++)
		if(strcmp(keyword_list[i], name) == 0) return 1;
	return 0;
}

void process_name(void){
	if(is_keyword(name) == 0 && strcmp(name, "") != 0)
		printf("name is '%s'\n", name);

	if(is_keyword(name) == 0 && strcmp(name, "") != 0)
		strcpy(name_list[nlctr++], name);
}

void process_line(char s[]){
	inside_string = 0;
	if(s[0] == '#') return;
	else if(s[0] == '/' && s[1] == '/') return;
	else {
		while(find_next_name())
			process_name();
		process_name();
		nnc = 0;
	}
}


int process_arguments(int argc, char **argv){
	return argc < 2 ? 6 : atoi(argv[1]);
}

int main(int argc, char **argv){
	int mmc = process_arguments(argc, argv);
	printf("mmc : %d\n", mmc);
	while(x_getline(line))
		process_line(line);

	for(int i = 0; i < nlctr; i++) printf("name : '%s'\n", name_list[i]);
	for(int i = 0; i < nlctr; i++) {
		for(int j = 0; j < nlctr; j++) {
			if(i != j){
				char ts1[100], ts2[100];
				if(strlen(name_list[i]) < mmc || strlen(name_list[j]) < mmc)
					continue;

				substr(ts1, name_list[i], mmc);
				substr(ts2, name_list[j], mmc);
				printf("%s %s\n", ts1, ts2);
				if(strcmp(ts1, ts2) == 0) {
					name_check_array[i] = 1;
					name_check_array[j] = 1;
				}
			}
		}
	}

	for(int i = 0; i < nlctr; i++) {
		if(name_check_array[i] == 0) strcpy(name_list[i], "");
	}


	int (*fn)(const void*, const void*) = (int (*)(const void*, const void*))strcmp;
	qsort(name_list, nlctr, sizeof(name_list[0]), fn);
	for(int i = 0; i < nlctr; i++)
			if(strlen(name_list[i]) > 0)
				printf("name : '%s'\n", name_list[i]);

}
