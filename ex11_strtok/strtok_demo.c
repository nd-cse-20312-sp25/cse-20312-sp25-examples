#include <stdio.h>
#include <string.h>

int main() {
    char expression[80];
    int value;
    char operator;
    const char delim[] = " ";
    char *token;

    fgets(expression, 80, stdin);
    token = strtok(expression, delim);

    // while token available
    while (token) {
        // Check if token is a number
        if (sscanf(token, "%d", &value)) {
            printf("%d is a number\n", value);
        }
        // Otherwise it must be an operator
        else {
            sscanf(token, "%c", &operator);
            printf("%c must be an operator\n", operator);
        }
        // get next token
        token = strtok(NULL, delim);
    }
}