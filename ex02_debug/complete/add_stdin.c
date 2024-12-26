#include <stdio.h>

int main() {
    int x, y;

    while (1) {
        if (scanf("%d %d", &x, &y) != 2) {
            break;
        }
        printf("%d + %d = %d\n", x, y, x + y);
    }
    
}