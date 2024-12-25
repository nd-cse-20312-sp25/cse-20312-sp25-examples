#!/usr/bin/env python3

''' adjacency_matrix.py

Represent graph as adjacency matrix.
'''

import sys

# Types

AdjacencyMatrix = list[list[int]]

# Functions

def read_graph(stream) -> AdjacencyMatrix:
    # Read number of vertices and number of edges
    num_vertices, num_edges = [int(x) for x in stream.readline().split()]

    # Initialize empty adjacency matrix
    # Use list comprehension to create a 2D list of zeros
    # Note that the * operator is used to repeat the elements in the list
    graph = [[0] * num_vertices for _ in range(num_vertices)]

    # Read each edge and update adjacency matrix
    for _ in range(num_edges):
        source, target = [int(x) for x in stream.readline().split()]

        # Update both directions since graph is undirected
        graph[source][target] = 1
        graph[target][source] = 1

    return graph

# Main Execution

def main(stream=sys.stdin) -> None:
    graph = read_graph(stream)

    for row in graph:
        print(row)

if __name__ == '__main__':
    main()
