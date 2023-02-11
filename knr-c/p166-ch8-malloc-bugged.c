/*
malloc() in chapter 5 was stack oriented

for ch5 implementation, malloc() and free() calls must occur in order since memory is contiguous to avoid overwriting or losing data

ch8 version is unrestricted in this aspect

memory is not allocated in a fixed size array

this version of malloc() requests space from OS as needed (probably using the sbrk() system call)

malloc()'d spaces may not be continuous

storage is kept as a list of free space blocks

each block contains:
- size
- pointer of next block
- space itself

blocks are kept in order increasing address

highest address block (last block) points to first block in chain

*/
#include "xprintf.c"
#include <stdio.h>
#include <string.h>
#include <unistd.h>

#define NALLOC 1024

typedef long Align;

union header
{
    Align x; // unused, only there to make size of union equal to largest type on system
    struct
    {
        union header *next_block_ptr; // next block if this block is on free block list
        unsigned int size;            // size of this block
    } block_info;
};

typedef union header Header;

static Header base;
static Header *free_ptr = NULL;

void free(void *target_block)
{
    Header *block_header, *current_header;
    block_header = (Header *)target_block - 1;
    // printf("target_block : %p, block_header addr : %p\n", target_block, current_header);
    current_header = free_ptr;
    int cond;
    cond = ((block_header > current_header) && (block_header < current_header->block_info.next_block_ptr));
    while (!cond)
    {
        if (current_header >= current_header->block_info.next_block_ptr)
        {
            if ((block_header > current_header) || (block_header < current_header->block_info.next_block_ptr))
            {
                break;
            }
        }
        cond = ((block_header > current_header) && (block_header < current_header->block_info.next_block_ptr));
    }
    if (block_header + block_header->block_info.size == current_header->block_info.next_block_ptr)
    {
        block_header->block_info.size = (current_header->block_info.next_block_ptr)->block_info.size;
        block_header->block_info.next_block_ptr = (current_header->block_info.next_block_ptr)->block_info.next_block_ptr;
    }
    else
    {
        block_header->block_info.next_block_ptr = current_header->block_info.next_block_ptr;
    }
    if (current_header + current_header->block_info.size == block_header)
    {
        current_header->block_info.size = block_header->block_info.size;
        current_header->block_info.next_block_ptr = block_header->block_info.next_block_ptr;
    }
    else
    {
        block_header->block_info.next_block_ptr = current_header->block_info.next_block_ptr;
    }
    free_ptr = current_header;
}

// ask system for more memory
Header *morecore(unsigned int number_of_units_required)
{
    // printf("morecore number of units required : %u", number_of_units_required);
    write(0, "morecore start\n", 100);
    char *cp;
    Header *up;
    if (number_of_units_required)
    {
        number_of_units_required = NALLOC;
    }
    write(0, "calling sbrk()\n", 100);

    cp = sbrk(number_of_units_required * sizeof(Header));
    if (cp == (char *)-1)
    {
        return NULL;
    }
    up = (Header *)cp;
    up->block_info.size = number_of_units_required;
    free((void *)(up + 1));
    return free_ptr;
}

void *malloc(unsigned n_bytes)
{
    x_printf("unb %d\n", n_bytes);
    Header *current_header, *previous_header;
    unsigned int number_of_units;

    unsigned int total_spc = n_bytes + sizeof(Header) - 1;

    unsigned int spc_per_unit = sizeof(Header);

    number_of_units = (total_spc / spc_per_unit) + 1;

    x_printf("z: %u %u %u\n", total_spc, spc_per_unit, number_of_units);
    // if previous header and free pointer are NULL (first run)
    if ((previous_header = free_ptr) == NULL)
    {
        // create degenerate free pointer
        base.block_info.next_block_ptr = &base;
        //
        free_ptr = &base;
        // previous header location is base
        previous_header = &base;
        // previous header size
        previous_header->block_info.size = 0;
        // next pointed at base
        previous_header->block_info.next_block_ptr = &base;
        // free pointer also pointed at base
    }
    // = &base
    current_header = previous_header->block_info.next_block_ptr;
    while (1) // this is the PROBLEM
    {
        if (current_header->block_info.size >= number_of_units)
        {
            if (current_header->block_info.size == number_of_units)
            {
                // block is exactly equal to number of units required

                previous_header->block_info.next_block_ptr = current_header->block_info.next_block_ptr;
            }
            else
            {
                // block is bigger than number of units required
                // allocate tail end
                current_header->block_info.size -= number_of_units;
                // increment current header by required size
                current_header += current_header->block_info.size;
                current_header->block_info.size = number_of_units;
            }
            free_ptr = previous_header;
            // printf("current_header : %p, free_ptr : %p\n", current_header, free_ptr);
            return (void *)(current_header + 1);
        }
        if (current_header == free_ptr)
        {
            if ((current_header = morecore(number_of_units)) == NULL)
                return NULL; // no units left
        }

        current_header = current_header->block_info.next_block_ptr;
    }
}

void *calloc(int n, size_t sz)
{
    long *base = malloc(sz);
    Header *h = (Header *)(base - 1);
    for (int i = 0; i < n; i++)
    {
        long *next = malloc(sz);
        *next = 0;
        h->block_info.next_block_ptr = (Header *)(next - 1);
        h = (Header *)(next - 1);
    }
    return (void *)base;
}

void test_malloc()
{
    char *p = malloc(20);
    strcpy(p, "lol");
    printf("%s %p\n", p, p);
    free(p);
}

void test_calloc()
{
    char *p = calloc(10, 4);
    strcpy(p, "lelllllllllllllllllllllllllllllllllelel123");
    printf("%s\n", p);
}

void test_malloc_header_1()
{
    long *b2 = malloc(50);
    Header *h = (Header *)(b2 - 1);
    printf("nbptr : %p\n", h->block_info.next_block_ptr);
}

void test_malloc_header_2()
{
    long *b2 = malloc(50);
    printf("%p", base.block_info.next_block_ptr);
}

int main()
{
    malloc(20);
    return 0;
}
