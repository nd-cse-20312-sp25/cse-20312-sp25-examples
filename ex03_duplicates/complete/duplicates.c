#include <stdbool.h>
#include <stdlib.h>

#include "duplicates.h"

bool has_duplicates_slow(int *a, int n) 
{
    for (int i = 0;  i < n;  i++) {
        for (int j = i+1;  j < n;  j++) {
            if (a[i] == a[j]) {
                return true;
            }
        }
    }
    return false;
}


bool has_duplicates_fast(int *a, int n) {
    bool *seen = calloc(n, sizeof(bool));
    for (int i = 0;  i < n;  i++) {
        if (seen[a[i]] == true) {
            free(seen);
            return true;
        }
        seen[a[i]] = true;
    }
    free(seen);
    return false;
}
