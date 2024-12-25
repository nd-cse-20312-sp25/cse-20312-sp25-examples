#include "map.h"
#include "hash.h"
#include <stdio.h>
#include <string.h>

void usage() {
    puts("Commands:");
    puts("  (i)nsert key value");
    puts("  (l)ookup key");
    puts("  (h)ash key");
    puts("  (p)rint");
    puts("  (a)lpha");
    puts("  (q)uit");
    puts("");
}

int main() {
    int done = 0;
    char line[80];
    char delim[] = " \n";
    char *command;
    char *key;
    int  value;

    Map *map = map_create();

    usage();
    while (!done) {
        printf("\nhash_demo> ");
        fgets(line, 80, stdin);
        command = strtok(line, delim);
        if (*command == 'q') {
            done = 1;
        }
        else if (*command == 'i') {
            key = strtok(NULL, delim);
            value = atoi(strtok(NULL, delim));
            map_insert(map, key, value);
            map_print(map);
        }
        else if (*command == 'l') {
            key = strtok(NULL, delim);
            value = map_lookup(map, key);
            printf("%s: %d\n", key, value);
        }
        else if (*command == 'h') {
            key = strtok(NULL, delim);
            int h = hash(key);
            printf("hash(%s) = %d   hash(%s) %% %d = %d\n", key, h, key, map->capacity, h % map->capacity);
        }
        else if (*command == 'a') {
            printf("alpha = %f\n", (float) map->size / map->capacity);
        }
        else if (*command == 'p') {
            map_print(map);
        }
        else {
            usage();
        }
    }

    map_delete(map);
}