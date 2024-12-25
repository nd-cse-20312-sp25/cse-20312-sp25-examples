#include <stdio.h>

// Determine the number of bits needed to represent a number
int bit_length(int n) {
    int i = 1;
    while (n > 1) {
        n = n >> 1;
        i++;
    }
    return i;
}

// Create a string with a binary representation of an integer
char* to_binary_string(unsigned int num) {
    static char binary[33];
    binary[32] = '\0';
    for (int i = 31; i >= 0; i--) {
        binary[i] = (num & 1) ? '1' : '0';
        num >>= 1;
    }
    char *p = binary;
    while (*(p+1) && (*p == '0')) {
        p++;
    }
    return p;
}

// Mid-square hash algorithm
//   key: value to be hashed
//   nbits: number of bits of output
int mid_square_hash(int key, int nbits) {
    int squared_key = key * key;
    int low_bits_to_remove = (bit_length(squared_key) - nbits) / 2;
    int extracted_bits = squared_key >> low_bits_to_remove;
    extracted_bits = extracted_bits & (0xFFFFFFFF >> (32 - nbits));
    return extracted_bits;
}

// Knuth multiplicative hash algorithm
//   key: value to be hashed
//   nbits: number of bits of output
unsigned knuth_multiplicative_hash(int key, int nbits) {
    const unsigned A = 2654435769U;
    return (key * A) >> (32 - nbits);
}

int main() {
    int nbits = 4;                // number of bits in table index
    int table_size = 1 << nbits;  // table size is a power of 2
    int collide_bin = 1;          // all keys will collide on this bin

    printf("table index: %d bits\n", nbits);
    printf("table size:  %d buckets\n", table_size);
    printf("all keys collide on bin: %d\n", collide_bin);
    printf(" key  key^2       binary key^2  mid-square  knuth\n");
    for(int i = 0;  i < 10;  i++) {
        // Make all keys collide on the same bin
        int key = i * table_size + collide_bin; 

        // binary representation of key squared
        int key_squared = key * key;
        char* binary_key_squared = to_binary_string(key_squared);

        // hashed keys from mid-square and knuth hash functions
        int mid_square = mid_square_hash(key, nbits);
        int knuth = knuth_multiplicative_hash(key, nbits);

        printf("%4d %6d %18s      %2d        %2d\n", key, key_squared, binary_key_squared, mid_square, knuth);
    }
}