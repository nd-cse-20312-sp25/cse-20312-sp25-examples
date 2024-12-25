#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

int cumulative_sum(int n) {
    if (n == 0) {
        return 0;
    }

    // TODO
}

int factorial(int n) {
    // TODO

    return n * factorial(n - 1);
}

void print_string(char *s) {
    if (*s == '\0') {
        putchar('\n');
        return;
    }

    // TODO
}

void reverse_array(int *list, int start_index, int end_index) {
    // TODO

    // swap elements
    int temp = list[start_index];
    list[start_index] = list[end_index];
    list[end_index] = temp;

    reverse_array(list, start_index + 1, end_index - 1);
}

int linear_search(int *numbers, int high, int key) {
    if (numbers[high] == key) {
        return high;
    }
    
    // TODO

    return linear_search(numbers, high -1, key);
}

int binary_search(int *numbers, int low, int high, int key) {
   if (low > high)
      return -1;

   int mid = (low + high) / 2;

   if (key > numbers[mid]) {
      // TODO
   }

   if (key < numbers[mid]) {
      // TODO
   }

   return mid;
}

int main()
{
    int numbers[] = {0, 10, 20, 30, 40};

    assert(cumulative_sum(3) == 6);
    assert(factorial(3) == 6);

    print_string("abcde");

    assert(linear_search(numbers, 4, 30) == 3);
    assert(binary_search(numbers, 0, 4, 30) == 3);

    reverse_array(numbers, 0, 4);
    assert(*numbers == 40);
    reverse_array(numbers, 0, 4);
    assert(*numbers == 0);
}

