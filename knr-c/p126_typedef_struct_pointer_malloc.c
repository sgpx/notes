#include <stdio.h>
#include <stdlib.h>

typedef struct {
  int a;
} ta;
typedef ta *tptr;

tptr asn() { return (tptr)malloc(sizeof(ta)); }
int main() {
  tptr n = asn();
  n->a = 5;
  printf("%d\n", n->a);
  free(n);
  return 0;
}
