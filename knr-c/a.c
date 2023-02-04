
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
struct snode
{
  char *name;
  char *defn;
  struct snode *next;
};

typedef struct snode node;
typedef node *nodeptr;

nodeptr root = NULL, rptr = NULL;

void install(char *name, char *defn)
{
  printf("r1 rptr : %p\n", rptr);
  if (root == NULL)
  {
    root = malloc(sizeof(node));
    rptr = root;
  }
  printf("r2 rptr : %p\n\n\n", rptr);
  rptr->name = name;
  rptr->defn = defn;
  rptr->next = malloc(sizeof(node));
  rptr = rptr->next;
  rptr->next = NULL;
}

void treeprint()
{
  printf("\n\ntreeprint\n");
  rptr = root;
  if (rptr == NULL)
    return;
  while (rptr->next != NULL)
  {
    printf("%s %s @ %p, next : %p\n", rptr->name, rptr->defn, rptr, rptr->next);
    rptr = rptr->next;
  }
}

void freetree()
{
  rptr = root;
  while (rptr->next != NULL)
  {
    nodeptr tmp = rptr;
    rptr = rptr->next;
    free(tmp);
  }
  free(rptr);
}

int check_node(char *name, char *defn, nodeptr n)
{
  return (strcmp(n->name, name) == 0 && strcmp(n->defn, defn) == 0);
}

void erase_node(char *name, char *defn)
{
  printf("erasing %s %s\n", name, defn);
  rptr = root;
  nodeptr prev = NULL;
  while (rptr != NULL)
  {
    if (check_node(name, defn, rptr))
    {
      // if node matches
      if (prev == NULL)
      {
        // if first node
        if (rptr->next == NULL)
        {
          // if only element (first node and next node is not null) (single list)
          free(root);
          root = malloc(sizeof(node));
          root->next = NULL;
          return;
        }
        else
        {
          // if first node and non-single list
          nodeptr tmp = root;
          root = root->next;
          free(root);
          return;
        }
      }
      else
      {
        // if not first node
        if (rptr->next == NULL)
        {
          // if last node
          nodeptr tmp = prev->next;
          prev->next = NULL;
          free(tmp);
          return;
        }
        else
        {
          // if middle node (not first node and not last node)
          prev->next = rptr->next;
          free(rptr);
          return;
        }
      }
    }
    prev = rptr;
    rptr = rptr->next;
  }
}

void testrun()
{
  install("a1", "b1");
  install("a2", "b2");
  install("a3", "b3");
  treeprint();
  erase_node("a1", "b1");
  treeprint();
  freetree();
}

int main()
{
  testrun();
  return 0;
}
