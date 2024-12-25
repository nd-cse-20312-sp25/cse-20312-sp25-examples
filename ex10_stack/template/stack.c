#include "stack.h"
#include <assert.h>

Stack* stack_create() {
    return array_create();
}

void stack_delete(Stack *stack) {
    array_delete(stack);
}

void stack_push(Stack *stack, int value) {
    // TODO
}

int	stack_top(Stack *stack) {
    assert(stack->size > 0);
    // TODO
}

int	stack_pop(Stack *stack) {
    int top = stack_top(stack);
    // TODO
    return top;
}

bool stack_empty(Stack *stack) {
    return stack->size == 0;
}