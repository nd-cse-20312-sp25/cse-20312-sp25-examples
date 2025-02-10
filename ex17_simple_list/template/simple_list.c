#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node {
    int value;    // Value associated with Node
    Node *next;   // Pointer to next Node in List
};

Node *list_add_head(Node *head, int value) {
    
    return NULL;
}

Node *list_remove_head(Node *head) {

    return NULL;
}

void list_print_iterative(Node *head) {

}

void list_delete_iterative(Node *head) {

}

void list_add_after(Node *curr, int value) {

}

void list_remove_after(Node *curr) {

}

void list_print_recursive(Node *head) {

}

void list_print_reversed_recursive(Node *head, Node *curr) {

}

void list_delete_recursive(Node *head) {

}

int main() {
    Node *head = NULL;

    puts("Add a few nodes at head of list");
    head = list_add_head(head, 1);
    printf("%d\n", head->value);

    head = list_add_head(head, 2);
    printf("%d %d\n", head->value, head->next->value);

    head = list_add_head(head, 3);
    printf("%d %d %d\n", head->value, head->next->value, head->next->next->value);

    puts("list_print_iterative(head)");
    list_print_iterative(head);

    puts("\nlist_delete_iterative(head)");
    list_delete_iterative(head);

    puts("\nhead = NULL");
    head = NULL;

    puts("\nhead = list_add_head(head, 1)");
    head = list_add_head(head, 1);
    list_print_iterative(head);

    puts("\nhead = list_add_head(head, 2)");
    head = list_add_head(head, 2);
    list_print_iterative(head);

    puts("\nlist_add_after(head, 99)");
    list_add_after(head, 99);
    list_print_iterative(head);

    puts("\nlist_remove_after(head)");
    list_remove_after(head);
    list_print_iterative(head);

    puts("\nlist_add_head(head, 55)");
    head = list_add_head(head, 55);
    list_print_iterative(head);

    puts("\nlist_remove_head(head)");
    head = list_remove_head(head);
    list_print_iterative(head);

    puts("\nlist_add_head(head, 3)");
    head = list_add_head(head, 3);
    list_print_iterative(head);

    puts("\nprint_list_recursive");
    list_print_recursive(head);

    puts("\nprint_list_reversed_recursive");
    list_print_reversed_recursive(head, head);

    puts("\nlist_delete_recursive(head)");
    list_delete_recursive(head);
}