#!/usr/bin/env python3

# Represent graph as adjacency list.

import sys
from collections import defaultdict

# Types

AdjacencyList = dict[int, list[int]]

# Functions

def read_graph(stream) -> AdjacencyList:
    # Read number of vertices and number of edges
    num_vertices, num_edges = [int(x) for x in stream.readline().split()]

    # Initialize empty adjacency list
    # Use defaultdict to automatically create empty neighbor
    # lists for vertices that have not been encountered yet
    # prior to appending neighbors
    graph = defaultdict(list)

    # Read each edge and update adjacency list
    for _ in range(num_edges):
        source, target = [int(x) for x in stream.readline().split()]

        # Update both directions since graph is undirected
        graph[source].append(target)
        graph[target].append(source)

    return graph

# Main Execution

def main(stream=sys.stdin) -> None:
    # read a single graph
    graph = read_graph(stream)

    # print the adjacency list with vertices in sorted order
    for vertex, neighbors in sorted(graph.items()):
        print(f'{vertex}: {sorted(neighbors)}')

if __name__ == '__main__':
    main()
