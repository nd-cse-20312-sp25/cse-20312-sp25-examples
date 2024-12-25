#!/usr/bin/env python3

import sys

def main():
    # Read input from stdin and chomp the newline at the end
    input = sys.stdin.read().strip()

    # Split the input into a list of strings
    number_str_list = input.split()

    # Convert the list of strings into a list of integers
    # Note: This is a list comprehension
    numbers = [int(num) for num in number_str_list]

    # Increment each number by 1
    incremented_numbers = [num + 1 for num in numbers]

    # Convert the list of integers into a list of strings
    incremented_numbers_str_list = [str(num) for num in incremented_numbers]

    # Join the list of strings into a single string with commas and spaces
    print(', '.join(incremented_numbers_str_list))

if __name__ == "__main__":
    main()