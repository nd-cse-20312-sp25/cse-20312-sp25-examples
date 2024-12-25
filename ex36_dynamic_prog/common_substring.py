#!/usr/bin/env python3

def longest_common_substring(str1, str2):
    # Create the matrix as a list of lists.
    matrix = []
    for i in range(len(str1)):
        # Each row is started as a list of zeros.
        matrix.append([0] * len(str2))

    # Variables to remember the largest value, and the row it
    # occurred at.
    max_value = 0
    max_value_row = 0
    for row in range(len(str1)):
        for col in range(len(str2)):
        
            # Check if the characters match
            if str1[row] == str2[col]:
                # Get the value in the cell that's up and to the 
                # left, or 0 if no such cell
                up_left = 0
                if row > 0 and col > 0:
                    up_left = matrix[row - 1][col - 1]
                
                # Set the value for this cell
                matrix[row][col] = 1 + up_left

                # Update the saved maximum value and row,
                # if appropriate.
                if matrix[row][col] > max_value:
                    max_value = matrix[row][col]
                    max_value_row = row
            else:
                matrix[row][col] = 0

    # The longest common substring is the substring
    # in str1 from index max_value_row - max_value + 1, 
    # up to and including max_value_row.
    start_index = max_value_row - max_value + 1
    return str1[start_index : max_value_row + 1]
    
def longest_common_substring_optimized(str1, str2):
    # Create one row of the matrix.
    matrix_row = [0] * len(str2)

    # Variables to remember the largest value, and the row it
    # occurred at.
    max_value = 0
    max_value_row = 0
    for row in range(len(str1)):
        # Variable to hold the upper-left value from the
        # current matrix position.
        up_left = 0
        for col in range(len(str2)):
            # Save the current cell's value; this will be up_left
            # for the next iteration.
            saved_current = matrix_row[col]
        
            # Check if the characters match
            if str1[row] == str2[col]:
                matrix_row[col] = 1 + up_left
                
                # Update the saved maximum value and row,
                # if appropriate.
                if matrix_row[col] > max_value:
                    max_value = matrix_row[col]
                    max_value_row = row
            else:
                matrix_row[col] = 0
                
            # Update the up_left variable
            up_left = saved_current

    # The longest common substring is the substring
    # in str1 from index max_value_row - max_value + 1, 
    # up to and including max_value_row.
    start_index = max_value_row - max_value + 1
    return str1[start_index : max_value_row + 1]

# Main program to test the longest common substring algorithms.
first_string = input('Enter the first string: ')
print()

second_string = input('Enter the second string: ')
print()

unoptimized = longest_common_substring(first_string, second_string)
optimized = longest_common_substring_optimized(first_string, second_string)
print()
print('Unoptimized solution: %s' % unoptimized)
print('Optimized solution: %s' % optimized)
