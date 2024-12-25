#include "array.h"
#include <assert.h>
#include <string.h>

Array *array_create() {
    // Allocate Array structure
    Array *array = malloc(sizeof(Array));

    // Initialize capacity and size
    array->capacity = ARRAY_DEFAULT_CAPACITY;
    array->size = 0;

    // Allocate the data array
    array->data = malloc(array->capacity * sizeof(int));

    // return pointer to Array
    return array;
}

void array_delete(Array *array) {
    // Free the data array
    free(array->data);
    
    // Free the Array structure
    free(array);
}

void array_append(Array *array, int value) {
    // If the size is at capacity, double the capacity
    if (array->size == array->capacity) {
        array->capacity *= 2;  // Double the capacity
        array->data = realloc(array->data, array->capacity * sizeof(int));
    }

    // Store value at end of array and increment size
    array->data[array->size] = value;
    array->size++;
}

int array_at(Array *array, int index) {
    // Return the value at the index
    return array->data[index];
}

int array_index(Array *array, int value) {
    // Scan internal array for first element 
    // that matches value and return its index         
    for (int index = 0; index < array->size; index++)
        if (array->data[index] == value) {
            return index;
        }
    
    // Return -1 if no match found
    return -1;
}

void array_insert(Array *array, int index, int value) {
    // If the size is at capacity, double the capacity
    if (array->size == array->capacity) {
        array->capacity *= 2;  // Double the capacity
        array->data = realloc(array->data, array->capacity * sizeof(int));
    }

    // Shift the values from index to the end of the array one element ahead
    for (int i = array->size; i > index; i--) {
        array->data[i] = array->data[i-1];
    }

    // Store new value and increment size
    array->data[index] = value;
    array->size++;
}
