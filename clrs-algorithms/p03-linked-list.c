#include <stdio.h>
#include <stdlib.h>

struct node {
	struct node * next;
	int value;	
};

void linked_list_print(struct node root) {
	struct node *p = &root;
	while(p != NULL){
		printf("%d ", p->value);
		p = p->next;	
	}
	printf("\n");
}

void linked_list_insert(struct node *p, int value, int at_pos) {
	int ctr = 0;
	if(at_pos == 0){
		struct node *tmp = p;
		struct node *newroot = malloc(sizeof(struct node));
		p = newroot;
		p->next = tmp;
		return;
	}

	while( p != NULL ) {
		printf("p: %p\n", p);

		if(ctr == at_pos-1){
			printf("%d %d\n", ctr, at_pos);
			printf("old pn: %p\n", p->next);
			struct node *q = malloc(sizeof(struct node));
			q->value = value;
			struct node *tmp = p->next;
			p->next = q;
			printf("new pn: %p\n", p->next);
			printf("new pv: %d\n", p->next->value);
			q->next = tmp;
			return;
		}
		ctr += 1;
		p = p->next;
	}
	
}

void linked_list_delete(struct node *p, int at_pos){
	int ctr = 0;
	if(at_pos == 0){
		p = p->next;
		return;
	}
	while( p != NULL ) {
		if(ctr == at_pos - 1) {
			struct node * tmp = p->next;
			p->next = tmp->next;
			printf("%p\n", p);
			return;
		}
		ctr += 1;
		p = p->next;
	}
}

void testcase1() {
	struct node h1, h2;
	h1.value = 5;
	h1.next = &h2;
	h2.value = 6;
	h2.next = NULL;

	linked_list_print(h1);
	linked_list_insert(&h1, 7, 1);
	linked_list_print(h1);
	linked_list_delete(&h1, 2);
	linked_list_print(h1);
}

int main() {
	testcase1();
	return 0;
}
