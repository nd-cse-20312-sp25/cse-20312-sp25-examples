#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node {
    int value;    // Value associated with Node
    Node *next;   // Pointer to next Node in List
};

Node *list_add_head(Node *head, int value) {
    Node *n = malloc(sizeof(Node));
    n->value = value;
    n->next = head;
    return n;
}

Node *list_remove_head(Node *head) {
    Node *n = head;
    head = head->next;
    free(n);
    return head;
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
        free(n);
    }
}

void list_add_after(Node *curr, int value) {
    Node *n = malloc(sizeof(Node));
    n->value = value;
    n->next = curr->next;
    curr->next = n;
}

void list_remove_after(Node *curr) {
    Node *successor = curr->next->next;
    free(curr->next);
    curr->next = successor;
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
    free(head);
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