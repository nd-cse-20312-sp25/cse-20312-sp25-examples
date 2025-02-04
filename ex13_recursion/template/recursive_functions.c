#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include <stdbool.h>

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

    return linear_search(numbers, high - 1, key);
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

bool has_duplicate(int *array, int high) {
    if (high == 0)
        return false;
    
    // TODO: Search for the last element in the array preceeding it
    // and return true if the element is found
    return true;

    // TODO: recursive call
}

//----------- Unit tests -----------//

int test_00_cumulative_sum() {
    assert(cumulative_sum(3) == 6);
    return EXIT_SUCCESS;
}

int test_01_factorial() {
    assert(factorial(3) == 6);
    return EXIT_SUCCESS;
}

int test_02_print_string() {
    print_string("abcde");
    return EXIT_SUCCESS;
}

int test_03_linear_search() {
    int numbers[] = {0, 10, 20, 30, 40};

    assert(linear_search(numbers, 4, 40) == 4);
    assert(linear_search(numbers, 4, 30) == 3);
    assert(linear_search(numbers, 4, 0) == 0);
    assert(linear_search(numbers, 4, 7) == -1);
    return EXIT_SUCCESS;
}

int test_04_binary_search() {
    int numbers[] = {0, 10, 20, 30, 40};

    assert(binary_search(numbers, 0, 4, 40) == 4);
    assert(binary_search(numbers, 0, 4, 30) == 3);
    assert(binary_search(numbers, 0, 4, 0) == 0);
    assert(binary_search(numbers, 0, 4, 7) == -1);
    return EXIT_SUCCESS;
}

int test_05_has_duplicate() {
    int nodups[] = {0, 10, 20, 30, 40};
    int dups[]   = {10, 10, 20, 30, 40, 10};

    assert(has_duplicate(nodups, 4) == false);
    assert(has_duplicate(dups, 4) == true);
    return EXIT_SUCCESS;
}

int test_06_reverse_array() {
    int numbers[] = {0, 10, 20, 30, 40};

    reverse_array(numbers, 0, 4);
    assert(*numbers == 40);
    reverse_array(numbers, 0, 4);
    assert(*numbers == 0);
    return EXIT_SUCCESS;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is one of the following:\n");
        fprintf(stderr, "    0  Test cumulative_sum\n");
        fprintf(stderr, "    1  Test factorial\n");
        fprintf(stderr, "    2  Test print_string\n");
        fprintf(stderr, "    3  Test linear_search\n");
        fprintf(stderr, "    4  Test binary_search\n");
        fprintf(stderr, "    5  Test has_duplicate\n");
        fprintf(stderr, "    6  Test reverse_array\n");
        return EXIT_FAILURE;
    }

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        case 0: status = test_00_cumulative_sum(); break;
        case 1: status = test_01_factorial(); break;
        case 2: status = test_02_print_string(); break;
        case 3: status = test_03_linear_search(); break;
        case 4: status = test_04_binary_search(); break;
        case 5: status = test_05_has_duplicate(); break;
        case 6: status = test_06_reverse_array(); break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }

    if (status == EXIT_SUCCESS)
        printf("Unit test passed\n");
    return status;
}