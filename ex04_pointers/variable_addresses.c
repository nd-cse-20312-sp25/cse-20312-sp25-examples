#include <stdio.h>

int main()
{
    char char_v1;
    int  int_v1;
    char char_v2;
    int  int_v2;
    char char_array[4];
    int  int_array[4];

    printf("Address of char_v1:        %p\n", &char_v1);
    printf("Address of int_v1:         %p\n", &int_v1);
    printf("Address of char_v2:        %p\n", &char_v2);
    printf("Address of int_v2:         %p\n", &int_v2);
    printf("Address of char_array[0]:  %p\n", &char_array[0]);
    printf("Address of char_array[1]:  %p\n", &char_array[1]);
    printf("Address of int_array[0]:   %p\n", &int_array[0]);
    printf("Address of int_array[1]:   %p\n", &int_array[1]);
}