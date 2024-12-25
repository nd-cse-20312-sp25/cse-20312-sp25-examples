#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

bool has_duplicates_fast(int *a, int n) {
    bool *seen = malloc(n * sizeof(bool));
    // bool *seen = calloc(n, sizeof(bool));
    for (int i = 0;  i < n;  i++) {
        if (seen[a[i]] == true) {
            free(seen);
            return true;
        }
        seen[a[i]] = true;
    }
    // free(seen);
    return false;
}

int main()
{
    int nodups[4] = {3, 1, 0, 2};

    bool status = has_duplicates_fast(nodups, 4);

    if (status) {
        printf("has duplicates\n");
    }
    else {
        printf("no duplicates\n");
    }
}