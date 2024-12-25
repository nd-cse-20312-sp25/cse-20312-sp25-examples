#include <stdio.h>

int square(int x)
{
    int result = x + x;
    return result;
}

void print_array(int *a, int n)
{
    for (int i = 0;  i <= n;  i++) {
        printf("%d\n", a[i]);
    }
}

int main()
{
    int array[5];

    for (int i = 0;  i < 5;  i++) {
        array[i] = square(i);
    }

    print_array(array, 5);
}