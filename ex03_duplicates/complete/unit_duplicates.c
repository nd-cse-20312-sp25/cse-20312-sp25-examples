#include "duplicates.h"
#include "unit_assert.h"
#include <stdio.h>

int array_nodup[4] = {0, 1, 2, 3};
int array_dup[4]   = {0, 1, 2, 2};

int test_00_has_duplicates_slow() {
    unit_assert(has_duplicates_slow(array_dup, 4) == true);
    unit_assert(has_duplicates_slow(array_nodup, 4) == false);
    return EXIT_SUCCESS;
}

int test_01_has_duplicates_fast() {
    unit_assert(has_duplicates_fast(array_dup, 4) == true);
    unit_assert(has_duplicates_fast(array_nodup, 4) == false);
    return EXIT_SUCCESS;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s NUMBER\n\n", argv[0]);
        fprintf(stderr, "Where NUMBER is one of the following:\n");
        fprintf(stderr, "    0  Test has_duplicates_slow\n");
        fprintf(stderr, "    1  Test has_duplicates_fast\n");
        return EXIT_FAILURE;
    }

    int number = atoi(argv[1]);
    int status = EXIT_FAILURE;

    switch (number) {
        case 0: status = test_00_has_duplicates_slow(); break;
        case 1: status = test_01_has_duplicates_fast(); break;
        default: fprintf(stderr, "Unknown NUMBER: %d\n", number); break;
    }
    if (status == EXIT_SUCCESS)
        printf("Unit test passed\n");
    return status;
}