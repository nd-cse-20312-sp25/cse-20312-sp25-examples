#include "table.h"
#include "hash.h"

#include <stdio.h>
#include <string.h>

Table *table_create() {
    Table *t = calloc(1, sizeof(Table));
    t->capacity = TABLE_DEFAULT_CAPACITY;
    t->buckets = calloc(t->capacity, sizeof(Pair *));
    return t;
}

void table_delete(Table *t) {
    for (int bucket = 0; bucket < t->capacity; bucket++) {
        pair_delete(t->buckets[bucket]);
    }

    free(t->buckets);
    free(t);
}

int table_lookup(Table *t, char *key) {
    // TODO: Determine the bucket

    // TODO: Look for the key in the bucket's chain of pairs
    // and return value if you find it.

    return -1;
}

void table_insert(Table *t, char *key, int value) {
    // TODO: Return without inserting if the key is found
    
    // TODO: Insert a pair at the head of the bucket's chain

    // TODO: Increment the size of the hash table
}

void table_print(Table *t) {
    for (int bucket = 0; bucket < t->capacity; bucket++) {
        printf("Bucket %d: ", bucket);
        for (Pair *curr = t->buckets[bucket]; curr; curr = curr->next)
            printf(" {%s: %d}", curr->key, curr->value);
        printf("\n");
    }
}
