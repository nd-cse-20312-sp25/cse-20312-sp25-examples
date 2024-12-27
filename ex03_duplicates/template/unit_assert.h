#pragma once

#include <stdio.h>
#include <stdlib.h>

#define unit_assert(expr) \
    do { \
        if (!(expr)) { \
            fprintf(stderr, "Assertion failed: (%s), file %s, line %d\n", #expr, __FILE__, __LINE__); \
            exit(EXIT_FAILURE); \
        } \
    } while (0)
    