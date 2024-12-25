#pragma once

typedef struct Pair Pair;
struct Pair {
    char *key;
    int   value;
    Pair *next;
};

Pair *	pair_create(const char *key, int value, Pair *next);
void	pair_delete(Pair *p);
