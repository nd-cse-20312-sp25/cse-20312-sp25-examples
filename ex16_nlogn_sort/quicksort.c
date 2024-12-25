#include <stdbool.h>

int Partition(int *numbers, int lowIndex, int highIndex) {
    // Pick middle element as pivot
    // int midpoint = lowIndex + (highIndex - lowIndex) / 2;
    int midpoint = (highIndex + lowIndex) / 2;
    int pivot = numbers[midpoint];

    bool done = false;
    while (!done) {
        // Increment lowIndex while numbers[lowIndex] < pivot
        while (numbers[lowIndex] < pivot) {
            lowIndex += 1;
        }

        // Decrement highIndex while pivot < numbers[highIndex]
        while (pivot < numbers[highIndex]) {
            highIndex -= 1;
        }

        // If zero or one elements remain, then all numbers are
        // partitioned. Return highIndex.
        if (lowIndex >= highIndex) {
            done = true;
        } else {
            // Swap numbers[lowIndex] and numbers[highIndex]
            int temp = numbers[lowIndex];
            numbers[lowIndex] = numbers[highIndex];
            numbers[highIndex] = temp;

            // Update lowIndex and highIndex
            lowIndex += 1;
            highIndex -= 1;
        }
    }

    // this will be the top of the low end for the next call
    return highIndex;
}

void Quicksort(int *numbers, int lowIndex, int highIndex) {
    // Base case: If the partition size is 1 or zero
    // elements, then the partition is already sorted
    if (lowIndex >= highIndex) {
        return;
    }

    // Partition the data within the array. Value lowEndIndex
    // returned from partitioning is the index of the low
    // partition's last element.
    int lowEndIndex = Partition(numbers, lowIndex, highIndex);

    // Recursively sort low partition (lowIndex to lowEndIndex)
    // and high partition (lowEndIndex + 1 to highIndex)
    Quicksort(numbers, lowIndex, lowEndIndex);
    Quicksort(numbers, lowEndIndex + 1, highIndex);
}

// from https://anim.ide.sk/sorting_algorithms_2.php
// Basically the same thing, may do one extra swap with itself
// void Quicksort(int *a, int beg, int end) {
//     int i = beg;
//     int j = end;
//     int pivot = a[(i + j) / 2];
//     while (i <= j) {  // i, j need to cross for next call
//         while (a[i] < pivot) 
//             i++;
//         while (a[j] > pivot) 
//             j--;
//         if (i <= j) {
//             // one last swap with yourself--no harm
//             int temp = a[i];
//             a[i] = a[j];
//             a[j] = temp;
//             i++;
//             j--;
//         }
//     }
//     if (beg < j) 
//         Quicksort(a, beg, j);
//     if (i < end) 
//         Quicksort(a, i, end);
// }