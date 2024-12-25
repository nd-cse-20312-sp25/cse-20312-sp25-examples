#include <stdio.h>

int f1(int x);
int f2(int x);
int f3(int x);

int f1(int x) {
    int result;
    printf("enter f1:    &x = %p    &result = %p\n", &x, &result);
    result = 1 * f2(x);
    printf("leave f1:    &x = %p    &result = %p\n", &x, &result);
    return result;
}

int f2(int x) {
    int result;
    printf("enter f2:    &x = %p    &result = %p\n", &x, &result);
    result = 2 * f3(x);
    printf("leave f2:    &x = %p    &result = %p\n", &x, &result);
    return result;
}

int f3(int x) {
    int result;
    printf("enter f3:    &x = %p    &result = %p\n", &x, &result);
    result = 3 * x;
    printf("leave f3:    &x = %p    &result = %p\n", &x, &result);
    return result;
}

int main() {
    int x = 1;
    int result;
    printf("enter main:  &x = %p    &result = %p\n", &x, &result);
    result = f1(x);
    printf("leave main:  &x = %p    &result = %p\n", &x, &result);
}