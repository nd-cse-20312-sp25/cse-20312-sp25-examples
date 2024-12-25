#include <stdio.h>

int main() {
    // Declare an array as a local variable and initialize it.
    // The array is allocated in the current stack frame
    char a[] = "cat";

    // Declare a pointer variable and point it at a string constant.
    // The pointer variable is allocated in the current stack
    // frame, but the string constant is allocated in the data segment.
    char *p = "dog";

    puts("Print a and p");
    printf("a: %s\n", a);
    printf("p: %s\n", p);
    puts("");

    puts("Print the sizes of a and p");
    printf("sizeof(a): %ld\n", sizeof(a));
    printf("sizeof(p): %ld\n", sizeof(p));
    puts("");

    puts("Print the addresses and content of a and p");
    printf("a:  %p, *a: %c\n", a, *a);
    printf("&p: %p,  p: %p  *p: %c\n", &p, p, *p);
    puts("");

    puts("Can you write a value to a string array?");
    // a[0] = 'X';
    // puts(a);
    puts("");
    
    puts("Can you write a value to a string constant?");
    // p[0] = 'X';
    // puts(p);
    puts("");
    
    puts("Can you assign a new address value to a char* variable?");
    // p = a;
    // puts(p);
    puts("");

    puts("Can you assign a new address value to an array label?");
    // a = p;
    // puts(a);
    puts("");
}