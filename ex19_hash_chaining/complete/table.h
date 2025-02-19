#pragma once

#include "pair.h"

#define TABLE_DEFAULT_CAPACITY (1 << 2)

typedef struct {
    Pair **buckets;
    int capacity;
    int size;
} Table;

Table*  table_create();
void    table_delete(Table *t);
void    table_insert(Table *t, char *key, int value);
int     table_lookup(Table *t, char *key);
void    table_print(Table *t);
