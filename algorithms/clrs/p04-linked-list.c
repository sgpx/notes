#include <stdio.h>
#include <stdlib.h>

struct node {
	struct node * next;
	int val;	
};

typedef struct node ts;

void insert(ts *root, int pos, int val) {
	if(pos == 0) {
		ts *tmp = root;
		root = malloc(sizeof(ts));
		root->val = val;
		root->next = tmp;
		return;
	}
}

void llprint(ts *root) {
	ts * abc = root;
	while(abc) {
		printf("%d ", abc->val);
		abc = abc->next;
	}
	printf("\n");
}

int main() {
	ts *h1 = malloc(sizeof(ts)), *h2 = malloc(sizeof(ts));
	h1->val = 5;
	h1->next = h2;
	h2->val = 6;
	h2->next = NULL;
	llprint(h1);
	insert(h1, 0, 7);
	llprint(h1);
}
