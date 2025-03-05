#include "table.h"
#include "hash.h"
#include <stdio.h>
#include <string.h>

void usage() {
    puts("Commands:");
    puts("  (i)nsert key value");
    puts("  (l)ookup key");
    puts("  (h)ash key");
    puts("  (p)rint");
    puts("  load (f)actor");
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

    Table *table = table_create();

    usage();
    while (!done) {
        printf("\nhash_table_demo> ");
        fgets(line, 80, stdin);
        command = strtok(line, delim);
        if (!command) continue;
        if (*command == 'q') {
            done = 1;
        }
        else if (*command == 'i') {
            key = strtok(NULL, delim);
            value = atoi(strtok(NULL, delim));
            table_insert(table, key, value);
            table_print(table);
        }
        else if (*command == 'l') {
            key = strtok(NULL, delim);
            value = table_lookup(table, key);
            printf("%s: %d\n", key, value);
        }
        else if (*command == 'h') {
            key = strtok(NULL, delim);
            int h = hash(key);
            printf("hash(%s) = %d   hash(%s) %% %d = %d\n", key, h, key, table->capacity, h % table->capacity);
        }
        else if (*command == 'f') {
            printf("load factor = %f\n", (float) table->size / table->capacity);
        }
        else if (*command == 'p') {
            table_print(table);
        }
        else {
            usage();
        }
    }

    table_delete(table);
}