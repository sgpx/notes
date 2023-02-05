#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define HASHSIZE 101

char *x_strdup(char *x)
{
	char *p = (char *)malloc(strlen(x));
	strcpy(p, x);
	return p;
}

struct nlist
{
	struct nlist *next;
	char *name;
	char *defn;
};

struct nlist blank;

static struct nlist *hashtab[HASHSIZE];

unsigned hash(char *s)
{
	unsigned hashval;
	for (hashval = 0; *s != '\0'; s++)
		hashval = *s + 31 * hashval;
	return 5; // hashval % HASHSIZE;
}

struct nlist *lookup(char *s)
{
	struct nlist *np;
	for (np = hashtab[hash(s)]; np != NULL; np = np->next)
		if (strcmp(s, np->name) == 0)
			return np;
	return NULL;
}

struct nlist *install(char *name, char *defn)
{
	struct nlist *np;
	unsigned hashval;
	if ((np = lookup(name)) == NULL)
	{
		//  if definition for name is null
		np = (struct nlist *)malloc(sizeof(*np));
		if (np == NULL || (np->name = x_strdup(name)) == NULL)
		{
			return NULL;
		}
		hashval = hash(name);
		np->next = hashtab[hashval];
		hashtab[hashval] = np;
	}
	else
	{
		// erase previous definition
		free((void *)np->defn);
	}
	if ((np->defn = x_strdup(defn)) == NULL)
		return NULL;
	return np;
}

int check_node(struct nlist *ref, char *name, char *defn)
{
	return (strcmp(ref->name, name) == 0 && strcmp(ref->defn, defn) == 0);
}

void remove_node(struct nlist *ref, char *name, char *defn)
{
	struct nlist *p = ref;
	struct nlist *q = p->next;
	printf("rm p : %p\n", p);
	printf("rm q : %p\n", q);
	if (p == NULL)
		return;
	else
	{
		printf("name : %s, defn : %s\n", p->name, p->defn);
		printf("nodematch : %d\n", check_node(p, name, defn) == 1);
	}

	if (check_node(p, name, defn) && q != NULL)
	{
		printf("i1\n");
		struct nlist tmp = *p;
		*p = *(p->next);
		free(tmp.next);
		return;
	}
	else if (q != NULL && check_node(q, name, defn) && q->next == NULL)
	{
		printf("i2\n");

		free(p->next);
		p->next = NULL;
		return;
	}
	else
	{
		printf("i3\n");

		p = p->next;
		return remove_node(p, name, defn);
	}
}

void undef(char *name, char *defn)
{
	struct nlist *np = lookup(name);
	if (np == NULL)
		return;
	unsigned hashval = hash(name);
	struct nlist *base = hashtab[hashval];
	remove_node(base, name, defn);
}

void overwrite_check()
{
	install("a1", "b1");
	install("a1", "b2");
	printf("%s\n", lookup("a1")->defn);
}
void basic_check()
{
	install("a1", "b1");
	install("a2", "b2");
	printf("%p\n", lookup("a1"));
	undef("a1", "b1");
	printf("%p %s\n", lookup("a1"), lookup("a1")->name);
}

void basic_check2()
{
	install("a1", "b1");
	install("a244", "b2");
	install("a321", "b3");
	struct nlist *res = lookup("a244");
	if (res != NULL)
		printf("%s : %s\n", res->name, res->defn);
	printf("res : %p, next : %p\n", res, res->next);
}

void undef_check()
{
	install("a2", "b2");
	install("a1", "b1");
	printf("erasing..\n");
	printf("before : %p\n", lookup("a1"));
	undef("a1", "b1");
	printf("after : %p\n", lookup("a1"));
	if (lookup("a1") != NULL)
	{
		printf("%s\n", lookup("a1")->defn);
	}
}

void testrun()
{
	 char *testname = "a2", *testdefn = "b2";
	install("a1", "b1");
	install("a2", "b2");
	install("a3", "b3");
	printf("before delete, found : %d\n", lookup(testname) != NULL);
	undef(testname, testdefn);
	printf("after delete, found : %d\n", lookup(testname) != NULL);
	// printf("%s %s\n", lookup("a1")->name, lookup("a1")->defn);
}

int main()
{
	testrun();
}