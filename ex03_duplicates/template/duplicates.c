#include <stdbool.h>
#include <stdlib.h>

#include "duplicates.h"

bool has_duplicates_slow(int *a, int n) 
{
    for (int i = 0;  i < n;  i++) {
        for (int j = i+1;  j < n;  j++) {
            // TODO: Replace 'true' with a proper test for a duplicate
            if (true) {
                return true;
            }
        }
    }
    return false;
}


bool has_duplicates_fast(int *a, int n) {
    bool *seen = calloc(n, sizeof(bool));
    for (int i = 0;  i < n;  i++) {
        // TODO: Replace 'true' with a test to determine if the
        // current element has been seen before
        if (true) {
            free(seen);
            return true;
        }
        // TODO: Update the seen array 
        // (for the case where element is seen for the first time)
    }
    free(seen);
    return false;
}
