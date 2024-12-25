void BubbleSort(int *numbers, int numbersSize) {
   for (int i = 0; i < numbersSize - 1; i++) {
      for (int j = 0; j < numbersSize - i - 1; j++) {
         if (numbers[j] > numbers[j+1]) {
            int temp = numbers[j];
            numbers[j] = numbers[j + 1];
            numbers[j + 1] = temp;
         }
      }
   }
}

// Suggested improvement to remember where the last
// swap occured and only proceed to that point, as
// everything after that is already sorted
// https://anim.ide.sk/sorting_algorithms_1.php
void BubbleSortImproved(int *numbers, int numbersSize) {
   int i = numbersSize - 1;
   while (i >= 1) {
      int last = -1;
      for (int j = 0;  j < i;  j++) {
         if (numbers[j] > numbers[j+1]) {
            int temp = numbers[j];
            numbers[j] = numbers[j + 1];
            numbers[j + 1] = temp;
            last = j;
         }
      }
      i = last;
   }
}