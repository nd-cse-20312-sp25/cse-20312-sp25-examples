/* sizes.c: sizes of common types */

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/* Main Execution */

int main(int argc, char *argv[]) {
    printf("sizeof(bool)          = %lu\n", sizeof(bool));
    printf("sizeof(char)          = %lu\n", sizeof(char));
    printf("sizeof(short)         = %lu\n", sizeof(short));
    printf("sizeof(int)           = %lu\n", sizeof(int));
    printf("sizeof(float)         = %lu\n", sizeof(float));
    printf("sizeof(double)        = %lu\n", sizeof(double));
    printf("sizeof(char*)         = %lu\n", sizeof(char*));
    printf("sizeof(int*)          = %lu\n", sizeof(int*));
}
