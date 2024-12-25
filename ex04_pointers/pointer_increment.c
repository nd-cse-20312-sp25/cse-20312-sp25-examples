#include <stdio.h>

int main()
{
    char char_array[4] = {5, 6, 7, 8};
    int  int_array[4]  = {5, 6, 7, 8};

    printf("char_array     = %p   *char_array       = %d\n", char_array,     *char_array      );
    printf("char_array + 1 = %p   *(char_array + 1) = %d\n", char_array + 1, *(char_array + 1));
    printf("char_array + 2 = %p   *(char_array + 2) = %d\n", char_array + 2, *(char_array + 2));
    printf("char_array + 3 = %p   *(char_array + 3) = %d\n", char_array + 3, *(char_array + 3));
    printf("\n");
    printf("int_array     =  %p   *int_array       =  %d\n", int_array,     *int_array      );
    printf("int_array + 1 =  %p   *(int_array + 1) =  %d\n", int_array + 1, *(int_array + 1));
    printf("int_array + 2 =  %p   *(int_array + 2) =  %d\n", int_array + 2, *(int_array + 2));
    printf("int_array + 3 =  %p   *(int_array + 3) =  %d\n", int_array + 3, *(int_array + 3));
}