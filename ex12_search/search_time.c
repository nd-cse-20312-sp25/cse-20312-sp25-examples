#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Linear congruential random number generator
// Constants from Kernighan & Ritchie, C Programming Language
int lcrng(int nbits, int reset) {
    static int rnd = 1;
    if (reset) {
        rnd = 1;
    } else {
        rnd = (rnd * 1103515245 + 12345) & ((1U << nbits) - 1);
    }
    return rnd;
}

// Linear search, verbatim from zyBook
int LinearSearch(int numbers[], int numbersSize, int key) {
    int i;

    for (i = 0; i < numbersSize; ++i) {
        if (numbers[i] == key) {
            return i;
        }
    }

    return -1; /* not found */
}

// Binary search, verbatim from zyBook
int BinarySearch(int numbers[], int numbersSize, int key) {
    int mid;
    int low;
    int high;

    low = 0;
    high = numbersSize - 1;

    while (high >= low) {
        mid = (high + low) / 2;
        if (numbers[mid] < key) {
            low = mid + 1;
        } else if (numbers[mid] > key) {
            high = mid - 1;
        } else {
            return mid;
        }
    }

    return -1;  // not found
}

int main() {
    const int NBITS = 20;  // default 2^20 = 1M
    const int SIZE = 1 << NBITS;
    const int TRIALS = 10000;

    clock_t start, end;
    double elapsed;
    int key;
    int found_count;

    // Allocate an array of SIZE integers and fill it with
    // values 0 through SIZE-1 in order

    int *data = malloc(SIZE * sizeof(int));
    for (int i = 0; i < SIZE; i++) {
        data[i] = i;
    }

    // Run TRIALS Linear Searches for random key values in the data array.
    // Print the elapsed time and number of values found
    // Generate random keys in the range 2*SIZE, so that approximately
    // half will be found

    lcrng(NBITS+1, 1);
    found_count = 0;
    printf("\nStarting %d trials of LinearSearch . . .\n", TRIALS);
    start = clock();
    for (int i = 0;  i < TRIALS;  i++) {
        key = lcrng(NBITS+1, 0);
        if (LinearSearch(data, SIZE, key) > 0) {
            ++found_count;
        }
    }
    end = clock();
    elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time: %f seconds.\n", elapsed);
    printf("found_count: %d\n", found_count);

    
    // Run TRIALS Binary Searches for random key values in the data array.
    // Print the elapsed time and number of values found
    // Generate random keys in the range 2*SIZE, so that approximately
    // half will be found

    lcrng(NBITS+1, 1);
    found_count = 0;
    printf("\nStarting %d trials of BinarySearch . . .\n", TRIALS);
    start = clock();
    for (int i = 0;  i < TRIALS;  i++) {
        key = lcrng(NBITS+1, 0);
        if (BinarySearch(data, SIZE, key) > 0) {
            ++found_count;
        }
    }
    end = clock();
    elapsed = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Time: %f seconds.\n", elapsed);
    printf("found_count: %d\n", found_count);

    free(data);
}