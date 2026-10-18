#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include "externptr.c"

#define NALLOC 1024
#define MLIM 4294967296 - 1
typedef long Align;

union header
{
    Align x;
    // size of union variable is equal to size of Alignment var long x (16)

    struct
    {
        union header *ptr;
        unsigned char is_composite : 1;
        unsigned int size;
        void *composite_ptr;
    } s;
};

typedef union header Header;

static Header base;
static Header *freep = NULL;

void x_free(void *ap)
{
    printf("freeing %p\n", ap);
    Header *bp = NULL, *p = NULL;
    bp = (Header *)ap - 1;
    printf("ap : %p, bp = ap - 1 : %p\n", ap, bp);
    printf("bp : freep : %p\n", freep);
    for (p = freep; !(bp > p && bp < p->s.ptr); p = p->s.ptr)
    {
        if (p >= p->s.ptr && (bp > p || bp < p->s.ptr))
        {
            printf("p is greater than p->s.ptr and bp is greater than p OR bp is less than p->s.ptr\n");
            break;
        }
        printf("iterating to p to p->s.ptr\n");
    }
    if (bp + bp->s.size == p->s.ptr)
    {
        printf("bp + bp->s.s.ize == p->s.ptr\n");
        bp->s.size += p->s.ptr->s.size;
        bp->s.ptr = p->s.ptr->s.ptr;
    }
    else
    {
        p->s.ptr = bp;
    }
    freep = p;
    printf("freep = p : %p\n", p);
}

void bpfree(void *p, unsigned int n)
{
    for (int i = 0; i < n; i++)
        x_free(p++);
}

static Header *morecore(unsigned int nu)
{
    char *cp;
    Header *up;
    printf("morecore() called\n");
    printf("nu : %u\n", nu);
    printf("nu : %u\n", nu);
    if (nu < NALLOC)
    {
        nu = NALLOC;
        printf("nu is less than NALLOC, setting nu : %u\n", nu);
    }
    printf("calling sbrk(%lu)\n", (nu * sizeof(Header)));
    cp = sbrk(nu * sizeof(Header));
    printf("after sbrk, cp : %p\n", cp);
    if (cp == (char *)-1) // no space left
    {
        printf("sbrk result is -1, no memory left\n");
        return NULL;
    }
    printf("setting *(up).s.size : %u\n", nu);
    up = (Header *)cp;
    up->s.size = nu;
    // up->s.ptr = NULL;

    printf("x_free((void*)(up + 1)), up+1 : %p\n", (up + 1));
    x_free((void *)(up + 1));
    printf("returning freep : %p\n", freep);
    return freep;
}

void *x_calloc(unsigned int nx, unsigned int ns)
{
    unsigned int nbytes = nx * ns;
    if (nbytes > MLIM)
        return NULL;
    if (nbytes == 0)
        return NULL;
    if (((nbytes + sizeof(Header) - 1) / sizeof(Header)) > MLIM)
        return NULL;
    printf("x_calloc nbytes : %u\n", nbytes);

    Header *p, *prevp;
    Header *morecore(unsigned int);
    unsigned int nunits;

    nunits = (nbytes + sizeof(Header) - 1) / sizeof(Header) + 1;
    printf("x_calloc nunits : %u\n", nunits);
    if ((prevp = freep) == NULL)
    {
        printf("prevp = freep = NULL\n");
        base.s.ptr = freep = prevp = &base;
        printf("base.s.ptr, freep, prevp := &base = %p\n", &base);
        base.s.size = 0;
        printf("base.s.size = 0\n");
    }
    printf("p = prevp->s.ptr = %p\n", prevp->s.ptr);

    for (p = prevp->s.ptr;; prevp = p, p = p->s.ptr)
    {
        printf("(p->s.size) %d >= nunits %u is %d\n", p->s.size, nunits, (p->s.size >= nunits));
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
            printf("returning p : %p, p+1 : %p, p->s.size : %u, p->s.ptr : %p\n", p, p + 1, p->s.size, p->s.ptr);
            unsigned char *z = (unsigned char *)(p + 1);
            *z = 0;
            return (void *)(z);
        }
        if (p == freep)
        {
            printf("p is equal to freep\n");
            if ((p = morecore(nunits)) == NULL)
            {
                return NULL;
            }
            printf("p after morecore : %p\n", p);
        }
    }
}

void *x_malloc(unsigned int nbytes)
{
    if (nbytes > MLIM)
        return NULL;
    if (nbytes == 0)
        return NULL;
    if (((nbytes + sizeof(Header) - 1) / sizeof(Header)) > MLIM)
        return NULL;
    printf("x_malloc nbytes : %u\n", nbytes);

    Header *p, *prevp;
    Header *morecore(unsigned int);
    unsigned int nunits;

    nunits = (nbytes + sizeof(Header) - 1) / sizeof(Header) + 1;
    printf("x_calloc nunits : %u\n", nunits);
    if ((prevp = freep) == NULL)
    {
        printf("prevp = freep = NULL\n");
        base.s.ptr = freep = prevp = &base;
        printf("base.s.ptr, freep, prevp := &base = %p\n", &base);
        base.s.size = 0;
        printf("base.s.size = 0\n");
    }
    printf("p = prevp->s.ptr = %p\n", prevp->s.ptr);

    for (p = prevp->s.ptr;; prevp = p, p = p->s.ptr)
    {
        printf("(p->s.size) %d >= nunits %u is %d\n", p->s.size, nunits, (p->s.size >= nunits));
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
            printf("returning p : %p, p+1 : %p, p->s.size : %u, p->s.ptr : %p\n", p, p + 1, p->s.size, p->s.ptr);
            unsigned char *z = (unsigned char *)(p + 1);
            *z = 0;
            return (void *)(z);
        }
        if (p == freep)
        {
            printf("p is equal to freep\n");
            if ((p = morecore(nunits)) == NULL)
            {
                return NULL;
            }
            printf("p after morecore : %p\n", p);
        }
    }
}

void t1(int mode)
{
    static char *p;
    if (mode == 1)
    {
        p = x_calloc(5, 4);
        strcpy(p, "kek");
    }
    else
    {
        printf("bpfree() p : %s\n", p);
        bpfree(p, 4);
    }
}


void t2(){
    extern int *externptr;
    externptr = x_malloc(10);
    *externptr = 5;
    printf("externptr : %p\n", externptr);
    printf("externptr : %d\n", *externptr);
    bpfree(externptr, 1);
}

int main()
{
    // x_malloc(1234567890);
    // x_malloc(999999999);
    // x_malloc(MLIM);
    // t1(1);
    // t1(2);
    t2();
    return 0;
}