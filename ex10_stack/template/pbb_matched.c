/* Lecture 08: PBB-Matched */

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "stack.h"

void chomp(char *str) {
    size_t size = strlen(str);
    if (*(str + size - 1) == '\n') *(str + size - 1) = 0;
}

bool is_pbb_matched(char *s) {
    Stack *stack = stack_create();

    for (char *c = s; *c; c++) {
        // if char is an opener, push 
        if (*c == '{' || *c == '[' || *c == '(') {
            // TODO
        // else if char is a closer that match opener on stack, pop
        } else if (!stack_empty(stack) &&
                   ((*c == '}' && stack_top(stack) == '{') ||
                    (*c == ']' && stack_top(stack) == '[') ||
                    (*c == ')' && stack_top(stack) == '('))) {
            // TODO
        // else no match
        } else {
            stack_delete(stack);
            // TODO
        }
    }
    if (stack_empty(stack)) {
        stack_delete(stack);
        // TODO
    } else {
        stack_delete(stack);
        // TODO
    }
}

int main(int argc, char *argv[]) {
    char buffer[BUFSIZ];

    while (fgets(buffer, BUFSIZ, stdin)) {
        chomp(buffer);
        puts(is_pbb_matched(buffer) ? "pbb-matched" : "not pbb-matched");
    }

    return 0;
}