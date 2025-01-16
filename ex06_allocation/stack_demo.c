#include <stdio.h>

int  f1(int x);
int  f2(int x);
void f3(int *x);

int f1(int x) {
    int result;
    result = 1 + f2(x);
    return result;
}

int f2(int x) {
    int result;
    f3(&x);
    result = 2 + x;
    return result;
}

void f3(int *x) {
    *x = 3 + *x;
}

int main() {
    int x = 1;
    int result;
    result = f1(x);
    printf("result = %d\n", result);
}