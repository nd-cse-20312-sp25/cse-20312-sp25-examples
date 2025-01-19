#include <stdio.h>

int add(int x, int y) {
    x = x + y;
    return x;
}

void square(int *a) {
    *a = *a * *a;
}

int main() {
    int x = 1;
    int y = 2;
    int z = add(x, y);
    square(&z);
    printf("x=%d  y=%d  z=%d\n", x, y, z);
    return 33;
}