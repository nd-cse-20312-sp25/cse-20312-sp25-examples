#pragma once

#include "pair.h"

#define MAP_DEFAULT_CAPACITY (1 << 2)

typedef struct {
    Pair **buckets;
    int capacity;
    int size;
} Map;

Map*    map_create();
void    map_delete(Map *m);
void    map_insert(Map *m, char *key, int value);
int     map_lookup(Map *m, char *key);
void    map_print(Map *m);
