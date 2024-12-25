#!/usr/bin/env python3

# Demonstration of a doubly linked list with an interface similar to Python's list

import doubly_linked_list as dll

# Create a doubly linked list
lst = dll.DoublyLinkedList()

# Append some data
lst.append(1)
lst.append(2)
lst.append(3)

# Insert some data
lst.insert(1, 10)

# Pop some data
d = lst.pop(1)

# Find the index of some data
i = lst.index(3)

# Get the string representation of the list
s = str(lst)
print(lst)

# Test if the list is empty
if lst:
    print("List is not empty")

# Test if the list contains some data
if 3 in lst:
    print("List contains 3")
if not 4 in lst:
    print("List does not contain 4")

# Iterate over the list
for data in lst:
    print(data)

# Clear the list
lst.clear()

# Test if the list is empty
if not lst:
    print("List is empty")



