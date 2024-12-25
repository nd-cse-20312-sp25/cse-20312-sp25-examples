#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node {
    int value;    // Value associated with Node
    Node *next;  // Pointer to next Node in List
};

Node *node_create(int value, Node *next) {

return NULL;
}

void node_delete(Node *n) {

}

void list_print_iterative(Node *head) {

}

void list_delete_iterative(Node *head) {

}

void list_add_after(Node *curr, int value) {

}

void list_remove_after(Node *curr) {

}

void list_add_head(Node **head, int value) {

}

void list_remove_head(Node **head) {

}

void list_print_recursive(Node *head) {

}

void list_print_reversed_recursive(Node *head, Node *curr) {

}

void list_delete_recursive(Node *head) {

}

int main() {
    Node *head = NULL;

    puts("Manually add a few nodes at head of list");
    head = node_create(1, head);
    printf("%d\n", 0);

    head = node_create(2, head);
    printf("%d %d\n", 0, 0);

    head = node_create(3, head);
    printf("%d %d %d\n", 0, 0, 0);

    puts("list_print_iterative(head)");
    list_print_iterative(head);

    puts("\nlist_delete_iterative(head)");
    list_delete_iterative(head);

    puts("\nhead = NULL");
    head = NULL;

    puts("\nhead = node_create(1, head)");
    head = node_create(1, head);
    list_print_iterative(head);

    puts("\nhead = node_create(2, head)");
    head = node_create(2, head);
    list_print_iterative(head);

    puts("\nlist_add_after(head, 99)");
    list_add_after(head, 99);
    list_print_iterative(head);

    puts("\nlist_remove_after(head)");
    list_remove_after(head);
    list_print_iterative(head);

    puts("\nlist_add_head(&head, 55)");
    list_add_head(&head, 55);
    list_print_iterative(head);

    puts("\nlist_remove_head(&head)");
    list_remove_head(&head);
    list_print_iterative(head);

    puts("\nlist_add_head(&head, 3)");
    list_add_head(&head, 3);
    list_print_iterative(head);

    puts("\nprint_list_recursive");
    list_print_recursive(head);

    puts("\nprint_list_reversed_recursive");
    list_print_reversed_recursive(head, head);

    puts("\nlist_delete_recursive(head)");
    list_delete_recursive(head);
}