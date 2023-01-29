#include <stdio.h>
#include <stdlib.h>

struct t {
	int num;
	struct t* next;
};

typedef struct t ts;


int main(){
	ts* a1 = malloc(sizeof(ts));
	a1->num = 1;
	a1->next = malloc(sizeof(ts));
	a1->next->num = 2;
	a1->next->next = malloc(sizeof(ts));
	a1->next->next->num = 3;
	a1->next->next->next = NULL;
	ts* p = a1;
	while(p != NULL){
		printf("%d\n", p->num);
		p = p->next;
	}
}
