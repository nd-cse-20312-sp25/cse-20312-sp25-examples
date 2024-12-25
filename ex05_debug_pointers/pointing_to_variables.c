#include <stdio.h>

int main()
{
    int *p;
    int *q;
    int x = 5;
    int y = 1;

    p = &x; // p gets pointer to x
    y = *p; // y gets value pointed to by p
    printf("y = %d\n", y);

    q = p;  // q gets same pointer as p

    printf("*p = %d    *q = %d\n", *p, *q); 
}