#include "map.h"
#include "hash.h"

#include <stdio.h>
#include <string.h>

Map *map_create() {
    Map *m = calloc(1, sizeof(Map));
    m->capacity = MAP_DEFAULT_CAPACITY;
    m->buckets = calloc(m->capacity, sizeof(Pair *));
    return m;
}

void map_delete(Map *m) {
    for (int bucket = 0; bucket < m->capacity; bucket++) {
        pair_delete(m->buckets[bucket]);
    }

    free(m->buckets);
    free(m);
}

int map_lookup(Map *m, char *key) {
    // TODO: Determine the bucket

    // TODO: Look for the key in the bucket's chain of pairs
    // and return value if you find it.

    return -1;
}

void map_insert(Map *m, char *key, int value) {
    // TODO: Return without inserting if the key is found

    int bucket = hash(key) % m->capacity;

    // TODO: Insert a pair at the head of the bucket's chain
    

    // TODO: Increment the size of the hash table

}

void map_print(Map *m) {
    for (int bucket = 0; bucket < m->capacity; bucket++) {
        printf("Bucket %d: ", bucket);
        for (Pair *curr = m->buckets[bucket]; curr; curr = curr->next)
            printf(" {%s: %d}", curr->key, curr->value);
        printf("\n");
    }
}
