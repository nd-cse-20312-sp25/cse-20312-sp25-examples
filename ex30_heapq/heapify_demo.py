#!/usr/bin/env python3

import heapq

# Using heapify() to convert list into heap
lst = [5, 5, 7, 3, 9, 2, 8]
print(f"Original list: {lst}")

heapq.heapify(lst)
print(f"Heapified:     {lst}")
