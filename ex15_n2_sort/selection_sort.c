void SelectionSort(int *numbers, int numbersSize) {
    int i = 0;
    int j = 0;
    int indexSmallest = 0;
    int temp = 0;  // Temporary variable for swap

    for (i = 0; i < numbersSize - 1; ++i) {
        // Find index of smallest remaining element
        indexSmallest = i;
        for (j = i + 1; j < numbersSize; ++j) {
            if (numbers[j] < numbers[indexSmallest]) {
                indexSmallest = j;
            }
        }

        // Swap numbers[i] and numbers[indexSmallest]
        temp = numbers[i];
        numbers[i] = numbers[indexSmallest];
        numbers[indexSmallest] = temp;
    }
}