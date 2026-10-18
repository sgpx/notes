#include <unistd.h>
#include <stdio.h>

#define NALLOC 1024

typedef long Align;

union header
{
    Align x;
    struct
    {
        union header *ptr;
        unsigned int size;
    } s;
};

typedef union header Header;

static Header base;
static Header *freep = NULL;

void free(void *ap) {
    Header *bp, *p;
    bp = (Header*)ap - 1;
    for(bp = freep; !(bp > p && bp < p->s.ptr); p = p->s.ptr){
        break;
    }
    if(bp + bp->s.size == p->s.ptr){
        bp->s.size += p->s.ptr->s.size;
        bp->s.ptr = p->s.ptr->s.ptr;
    }
    else
        p->s.ptr = bp;
    freep = p;
}

static Header *morecore(unsigned int nu){
    char *cp;
    Header *up;
    if(nu < NALLOC){
        nu = NALLOC;
    }
    cp = sbrk(nu * sizeof(Header));
    if(cp == (char*)-1) // no space left
        return NULL;
    up = (Header *)cp;
    up->s.size = nu;
    free((void*)(up + 1));
    return freep;
}

void *malloc(unsigned int nbytes)
{
    Header *p, *prevp;
    Header *morecore(unsigned int);
    unsigned int nunits;

    nunits = (nbytes + sizeof(Header) - 1) / sizeof(Header) + 1;
    if ((prevp = freep) == NULL)
    {
        base.s.ptr = freep = prevp = &base;
        base.s.size = 0;
    }
    for (p = prevp->s.ptr;; prevp = p, p = p->s.ptr)
    {
        // printf("loop1\n");
        if (p->s.size >= nunits)
        {
            if (p->s.size == nunits)
            {
                prevp->s.ptr = p->s.ptr;
            }
            else
            {
                p->s.size -= nunits;
                p += p->s.size;
                p->s.size = nunits;
            }
            freep = prevp;
            return (void *)(p + 1);
        }
        if (p == freep)
        {
            if ((p = morecore(nunits)) == NULL)
            {
                return NULL;
            }
        }
    }
}

int main()
{
    char *p = (char*)malloc(5);
    strcpy(p, "lol");
    printf("%s\n", p);
    return 0;
}