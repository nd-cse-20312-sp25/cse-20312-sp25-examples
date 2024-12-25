#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *name;
    int  age;
} Person;

int main() {
    // Declare a Person as a local variable
    Person p;

    // Set name to "James" and age to 20
    // TODO:


    // Allocate a Person on the heap
    Person *p_ptr = malloc(sizeof(Person));
    
    // Set name to "Madison" and age to 21
    // TODO:


    // Print the sizes of the structs
    printf("sizeof(p):      %lu\n", sizeof(p));
    printf("sizeof(*p_ptr): %lu\n", sizeof(*p_ptr));

    // Don't forget to free anything you malloc'ed!
    free(p_ptr);
}