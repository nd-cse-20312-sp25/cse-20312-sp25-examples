#include <stdio.h>
#include <stdbool.h>

int counter(bool reset) {
    static int count = 0;
    if (reset) {
        count = 0;
    }
    return count++;
}

int main() {
    printf("counter = %d\n", counter(false));
    printf("counter = %d\n", counter(false));
    printf("counter = %d\n", counter(false));
    printf("counter = %d\n", counter(true));
    printf("counter = %d\n", counter(false));
    printf("counter = %d\n", counter(false));
}