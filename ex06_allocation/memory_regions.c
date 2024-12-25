/* regions:c */

#include <stdio.h>
#include <stdlib.h>

double G = 3.14;

int main(int argc, char *argv[]) {
    int        x   = 1;
    int        a[] = {4, 6, 6, 3, 7};
    char      *s   = "string";
    int       *p   = malloc(10 * sizeof(int));
    static int t   = 2;

    puts("----------------stack----------------");
    printf("   a: Address: %p, Size: %lu\n",  &a, sizeof( a));  // stack
    printf(" &p2: Address: %p, Size: %lu\n",  &p, sizeof(&p));  // stack
    printf("  &s: Address: %p, Size: %lu\n",  &s, sizeof(&s));  // stack
    printf("   x: Address: %p, Size: %lu\n",  &x, sizeof( x));  // stack
    puts("----------------heap----------------");
    printf("   p: Address: %p, Size: %lu\n",   p, sizeof( p)); // heap
    puts("----------------data----------------");
    printf("   t: Address: %p, Size: %lu\n",  &t, sizeof(t));   // data
    printf("   G: Address: %p, Size: %lu\n",  &G, sizeof( G));  // data
    printf("   s: Address: %p, Size: %lu\n",   s, sizeof( s));  // data
    printf("  *s: Address: %p, Size: %lu\n", &*s, sizeof(*s));  // data (same as s)
    puts("----------------code----------------");
    printf("main: Address: %p, Size: %lu\n", &main, sizeof(main));  // code
}
