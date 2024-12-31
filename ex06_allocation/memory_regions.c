#include <stdio.h>
#include <stdlib.h>

double GLOBAL = 3.14;

int main() {
    int        int_scalar   = 25;
    int        int_array[]  = {100, 101, 102, 103};
    char      *str_const    = "hello";
    int       *malloc_array = malloc(10 * sizeof(int));
    static int static_int   = 2;

    puts("---------------------------stack----------------------------");
    printf("    int_array: %p,    *int_array: %d\n",  int_array, *int_array);
    printf("&malloc_array: %p,  malloc_array: %p\n",  &malloc_array, malloc_array);
    printf("   &str_const: %p,     str_const: %p\n",  &str_const, str_const);
    printf("  &int_scalar: %p,    int_scalar: %d\n",  &int_scalar, int_scalar);
    puts("----------------------------heap----------------------------");
    printf(" malloc_array: %p, *malloc_array: %d\n",  malloc_array, *malloc_array);
    puts("----------------------------data----------------------------");
    printf("  &static_int: %p,    static_int: %d\n",  &static_int, static_int);
    printf("      &GLOBAL: %p,        GLOBAL: %f\n",  &GLOBAL, GLOBAL);
    printf("    str_const: %p,    *str_const: %c\n",  str_const, *str_const);
    puts("----------------------------code----------------------------");
    printf("         main: %p,         *main: 0x%x\n", main, (unsigned char)(*main));
}
