#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node {
    int value;    // Value associated with Node
    Node *next;  // Pointer to next Node in List
};

Node *node_create(int value, Node *next) {
    Node *n = malloc(sizeof(Node));
    n->value = value;
    n->next = next;
    return n;
}

void node_delete(Node *n) {
    free(n);
}

void list_print_iterative(Node *head) {
    for (Node *n = head;  n != NULL;  n = n->next) {
        printf("%d ", n->value);
    }
    printf("\n");
}

void list_delete_iterative(Node *head) {
    while (head != NULL) {
        Node *n = head;
        head = head->next;
        node_delete(n);
    }
}

void list_add_after(Node *curr, int value) {
    curr->next = node_create(value, curr->next);
}

void list_remove_after(Node *curr) {
    Node *successor = curr->next->next;
    node_delete(curr->next);
    curr->next = successor;
}

void list_add_head(Node **head, int value) {
    *head = node_create(value, *head);
}

void list_remove_head(Node **head) {
    Node *n = *head;
    *head = (*head)->next;
    node_delete(n);
}

void list_print_recursive(Node *head) {
    if (head == NULL) {
        printf("\n");
        return;
    }

    printf("%d ", head->value);
    list_print_recursive(head->next);
}

void list_print_reversed_recursive(Node *head, Node *curr) {
    if (curr == NULL) {
        return;
    }

    list_print_reversed_recursive(head, curr->next);
    printf("%d ", curr->value);
    if (curr == head) {
        printf("\n");
    }
}

void list_delete_recursive(Node *head) {
    if (head == NULL) {
        return;
    }

    list_delete_recursive(head->next);
    node_delete(head);
}

int main() {
    Node *head = NULL;

    puts("Manually add a few nodes at head of list");
    head = node_create(1, head);
    printf("%d\n", head->value);

    head = node_create(2, head);
    printf("%d %d\n", head->value, head->next->value);

    head = node_create(3, head);
    printf("%d %d %d\n", head->value, head->next->value, head->next->next->value);

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