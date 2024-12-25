#include <stdio.h>

int f1(int x);
int f2(int x);
int f3(int x);

int f1(int x) {
    int result;
    result = 1 * f2(x);
    return result;
}

int f2(int x) {
    int result;
    result = 2 * f3(x);
    return result;
}

int f3(int x) {
    int result;
    result = 3 * x;
    return result;
}

int main() {
    int x = 1;
    int result;
    result = f1(x);
    printf("result = %d\n", result);
}