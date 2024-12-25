#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void chomp(char *str) {
    // Iterate through str until you get to a null 
    // character.  If you encounter a newline '\n',
    // replace it with '\0' and break out of the loop
    for (char *p = str; *p; p++) {
        if (*p == '\n') {
            *p = '\0';
            break;
        }
    }
}

char  **read_user_data(FILE *stream, int nstrings) {
    // Up to 80 characters per string
    char buffer[80];

    // Allocate a string array for up to nstrings strings
    // that is initialized to all zeros
    char **sarray = calloc(nstrings, sizeof(char *));

    int i = 0;
    while (fgets(buffer, 80, stream)) {
        chomp(buffer);

        // Duplicate the string in the buffer and insert it in sarray
        // Increment the array index
        sarray[i++] = strdup(buffer);
    }
    return sarray;
}

void free_string_array(char **sarray) {
    for (int i = 0; sarray[i]; i++) {
        // free each individual string
        free(sarray[i]);
    }
    // free the array of string pointers
    free(sarray);
}

void print_string_array(char **sarray) {
    for (int i = 0; sarray[i]; i++) {
        puts(sarray[i]);
    }
}

int main() {
    char **string_array = read_user_data(stdin, 100);
    print_string_array(string_array);
    free_string_array(string_array);
}