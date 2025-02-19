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
    int bucket = hash(key) % t->capacity;

    // TODO: Look for the key in the bucket's chain of pairs
    // and return value if you find it.
    for (Pair *curr = t->buckets[bucket]; curr; curr = curr->next) {
        if (strcmp(curr->key, key) == 0) {
            return curr->value;
        }
    }

    return -1;
}

void table_insert(Table *t, char *key, int value) {
    // TODO: Return without inserting if the key is found
    if (table_lookup(t, key) >= 0) {
        return;
    }
    
    // TODO: Insert a pair at the head of the bucket's chain
    int bucket = hash(key) % t->capacity;
    t->buckets[bucket] = pair_create(key, value, t->buckets[bucket]);

    // TODO: Increment the size of the hash table
    t->size++;
}

void table_print(Table *t) {
    for (int bucket = 0; bucket < t->capacity; bucket++) {
        printf("Bucket %d: ", bucket);
        for (Pair *curr = t->buckets[bucket]; curr; curr = curr->next)
            printf(" {%s: %d}", curr->key, curr->value);
        printf("\n");
    }
}
