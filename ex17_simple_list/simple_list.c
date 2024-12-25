#include <stdio.h>
#include <stdlib.h>

typedef struct Node Node;
struct Node {
    int data;    // Value associated with Node
    Node *next;  // Pointer to next Node in List
};

Node *node_create(int data, Node *next) {
    Node *n = malloc(sizeof(Node));
    n->data = data;
    n->next = next;
    return n;
}

void node_delete(Node *n) {
    free(n);
}

void print_list_iterative(Node *head) {
    for (Node *n = head;  n != NULL;  n = n->next) {
        printf("%d ", n->data);
    }
    printf("\n");
}

void print_list_recursive(Node *head) {
    if (head == NULL) {
        printf("\n");
        return;
    }

    printf("%d ", head->data);
    print_list_recursive(head->next);
}

void print_list_reversed_recursive(Node *head, Node *curr) {
    if (curr == NULL) {
        return;
    }

    print_list_reversed_recursive(head, curr->next);
    printf("%d ", curr->data);
    if (curr == head) {
        printf("\n");
    }
}

void delete_list_iterative(Node *head) {
    while (head != NULL) {
        Node *n = head;
        head = head->next;
        node_delete(n);
    }
}

void delete_list_recursive(Node *head) {
    if (head == NULL) {
        return;
    }

    delete_list_recursive(head->next);
    node_delete(head);
}

int main() {
    Node *head = NULL;

    head = node_create(1, head);
    printf("%d\n", head->data);

    head = node_create(2, head);
    printf("%d %d\n", head->data, head->next->data);

    head = node_create(3, head);
    printf("%d %d %d\n", head->data, head->next->data, head->next->next->data);

    print_list_iterative(head);
    print_list_recursive(head);
    print_list_reversed_recursive(head, head);

    delete_list_iterative(head);
    // delete_list_recursive(head);
}