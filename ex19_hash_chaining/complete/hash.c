#include "hash.h"

int	hash(char *str) {    
    int value = 0;
    for (int i = 0; str[i] != '\0'; i++) {
    	value += str[i];
    }

    return value;
}