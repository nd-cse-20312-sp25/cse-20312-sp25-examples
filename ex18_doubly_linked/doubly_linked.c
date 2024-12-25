// Created with help from ChatGPT

#include <stdio.h>
#include <stdlib.h>

// Definition of a Node
typedef struct Node {
    int data;
    struct Node* prev;
    struct Node* next;
} Node;

// Definition of a Doubly Linked List
typedef struct DoublyLinkedList {
    Node* head;  // Dummy head
    Node* tail;  // Dummy tail
} DoublyLinkedList;

// Create a new node
Node* create_node(int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    new_node->prev = new_node->next = NULL;
    return new_node;
}

// Initialize the doubly linked list with Dummy nodes
DoublyLinkedList* create_list() {
    DoublyLinkedList* list = (DoublyLinkedList*)malloc(sizeof(DoublyLinkedList));
    list->head = create_node(0);  // Dummy head
    list->tail = create_node(0);  // Dummy tail
    list->head->next = list->tail;
    list->tail->prev = list->head;
    return list;
}

// Check if the list is empty
int is_empty(DoublyLinkedList* list) {
    return list->head->next == list->tail;
}

// Helper function: Insert node after current node
void insert_after(Node *current, int data) {
    Node* new_node = create_node(data);
    Node* next_node = current->next;

    current->next = new_node;
    new_node->prev = current;
    new_node->next = next_node;
    next_node->prev = new_node;
}

// Helper function: Remove current node and return data
int pop(Node* current) {
    int data = current->data;
    current->prev->next = current->next;
    current->next->prev = current->prev;
    free(current);
    return data;
}

// Prepend an element to the head  of the list
void prepend(DoublyLinkedList* list, int data) {
    insert_after(list->head, data);
}

// Append an element to the tail of the list
void append(DoublyLinkedList* list, int data) {
    insert_after(list->tail->prev, data);
}

// Remove the (non-dummy) head of the list and return value
int pop_head(DoublyLinkedList* list) {
    return pop(list->head->next);
}

// Remove the (non-dummy) head of the list and return value
int pop_tail(DoublyLinkedList* list) {
    return pop(list->tail->prev);
}

// Insert an element at a specific position (0-based index)
void insert_at(DoublyLinkedList* list, int data, int position) {
    Node* current = list->head;
    int i = 0;

    // Traverse the list to find the position
    while (current->next != list->tail && i < position) {
        current = current->next;
        i++;
    }

    insert_after(current, data);
}

// Delete an element at a specific position (0-based index)
void delete_at(DoublyLinkedList* list, int position) {
    Node* current = list->head->next;  // Start from the first valid node
    int i = 0;

    // Traverse to the node at the specified position
    while (current != list->tail && i < position) {
        current = current->next;
        i++;
    }

    // If we are at a valid node (not the Dummy tail)
    if (current != list->tail) {
        pop(current);
    }
}

// Delete an element by value
int delete_by_value(DoublyLinkedList* list, int data) {
    Node* current = list->head->next;  // Start from the first valid node
    while (current != list->tail) {
        if (current->data == data) {
            pop(current);
            return 1;  // Data found and deleted
        }
        current = current->next;
    }
    return 0;  // Data not found
}

// Display the list forward
void display_forward(DoublyLinkedList* list) {
    printf("Head <-> ");
    Node* current = list->head->next;  // Start from the first valid node
    while (current != list->tail) {
        printf("%d <-> ", current->data);
        current = current->next;
    }
    printf("Tail\n");
}

// Display the list backward
void display_backward(DoublyLinkedList* list) {
    printf("Tail <-> ");
    Node* current = list->tail->prev;  // Start from the last valid node
    while (current != list->head) {
        printf("%d <-> ", current->data);
        current = current->prev;
    }
    printf("Head\n");
}

// Free the memory allocated for the list
void free_list(DoublyLinkedList* list) {
    Node* current = list->head;
    while (current != NULL) {
        Node* next = current->next;
        free(current);
        current = next;
    }
    free(list);
}

int main() {
    DoublyLinkedList* dll = create_list();

    printf("List formard empty list:                  ");
    display_forward(dll);
    // Head <-> Tail

    append(dll, 20);
    printf("List forward after append(dll, 20):       ");
    display_forward(dll);
    // Head <-> 20 <-> Tail

    append(dll, 30);
    printf("List forward after append(dll, 30):       ");
    display_forward(dll);
    // Head <-> 20 <-> 30 <-> Tail

    prepend(dll, 10);
    printf("List forward after prepend(dll, 10):      ");
    display_forward(dll);
    // Head <-> 10 <-> 20 <-> 30 <-> Tail

    printf("List backward:                            ");
    display_backward(dll);
    // Tail <=> 30 <-> 20 <-> 10 <-> Head

    insert_at(dll, 25, 2);  // Insert 25 at position 2
    printf("List forward after insert_at(dll, 25, 2): ");
    display_forward(dll);
    // Head <-> 10 <-> 20 <-> 25 <-> 30 <-> Tail

    delete_at(dll, 1);  // Delete element at position 1
    printf("List forward after delete_at(dll, 1):     ");
    display_forward(dll);
    // Head <-> 10 <-> 25 <-> 30 <-> Tail

    pop_head(dll);  // Pop the head of the list
    printf("List forward after pop_head(dll):         ");
    display_forward(dll);
    // Head <-> 25 <-> 30 <-> Tail

    pop_tail(dll);  // Pop the head of the list
    printf("List forward after pop_tail(dll):         ");
    display_forward(dll);
    // Head <-> 25 <-> Tail

    // Free the allocated memory for the list
    free_list(dll);

    return 0;
}
