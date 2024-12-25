void InsertionSort(int *numbers, int numbersSize) {
    for (int i = 1; i < numbersSize; ++i) {
        int j = i;
            // Insert numbers[i] into sorted part
            // stopping once numbers[i] in correct position
            while (j > 0 && numbers[j] < numbers[j - 1]) {
            // Swap numbers[j] and numbers[j - 1]
            int temp = numbers[j]; 
            numbers[j] = numbers[j - 1];
            numbers[j - 1] = temp;
            --j;
        }
    }
}

// An improved version that does fewer swaps by holding
// the current value to be inserted in a temp variable to
// be inserted when the proper location is found, rather
// than "bubbling" it into place.
// See https://anim.ide.sk/sorting_algorithms_1.php
void InsertionSortImproved(int *numbers, int numbersSize) {
    for (int i = 1;  i < numbersSize;  i++) {
        int j = i - 1;
        int tmp = numbers[i];
        while ((j >= 0) && (numbers[j] > tmp)) {
            numbers[j+1] = numbers[j];
            j = j - 1;
        }
        numbers[j+1] = tmp;
    }
}