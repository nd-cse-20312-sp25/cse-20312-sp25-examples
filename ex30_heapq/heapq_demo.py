#!/usr/bin/env python3

import heapq

# Create a list
heap = []

# Insert elements into the heap
input_list = [10, 2, 5, 18, 22]
print("Pushing elements into the heap")
for i in input_list:
    print("Push", i, "into the heap")
    heapq.heappush(heap, i)
    print("Heap elements:", heap)

print()
print("Popping elements from the heap")
while heap:
    print("Pop the smallest element:", end=" ")
    print(heapq.heappop(heap))
    print("Heap elements:", heap)
