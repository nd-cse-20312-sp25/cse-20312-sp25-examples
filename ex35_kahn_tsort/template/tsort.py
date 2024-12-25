#!/usr/bin/env python3

''' tsort.py

Use Kahn's algorithm to perform a topological sort on a Makefile.
'''

from collections import defaultdict
import sys

# Types

Graph = dict[str, set[str]]

# Functions

def read_edgefile(stream) -> Graph:
    graph: Graph = defaultdict(set)

    for line in stream:
        source, target = line.split()
        graph[source].add(target)

    return graph

def read_makefile(stream) -> Graph:
    graph: Graph = defaultdict(set)

    for line in stream:
        if ':' not in line:
            continue

        targets_string, sources_string = line.split(':')
        targets = targets_string.split()
        sources = sources_string.split()

        for source in sources:
            graph[source].update(targets)

    return graph

def compute_degrees(graph: Graph) -> dict[str, int]:
    # degrees is a dictionary {vertex:incoming_edges}
    # defaultdict is used to create a default value of 0
    degrees: dict[str, int] = defaultdict(int)

    for source, targets in graph.items():
        # If the source hasn't been seen yet,
        # include it in the dictionary with a value of 0
        # TODO:
        pass
        # For each target, increment the number of incoming edges
        for target in targets:
            # Creates an entry with value 0 before incrementing
            # TODO:
            pass

    return degrees

def topological_sort(graph: Graph) -> list[str]:
    visited  = []
    degrees  = compute_degrees(graph)

    # Initialize the frontier with vertices that have no incoming edges
    # Use a list comprehension to get the vertices with degree 0
    # TODO:
    frontier = None

    while frontier:
        vertex = frontier.pop()
        visited.append(vertex)

        for neighbor in graph[vertex]:
            degrees[neighbor] -= 1
            if degrees[neighbor] == 0:
                frontier.append(neighbor)

    return visited

# Main Execution

def main(args=None) -> None:
    if args is None:
        args = sys.argv[1:]

    # Set the name of the function to be called to read the graph
    # depending on whether the first argument is '-m' for a makefile
    # or otherwise for an edgefile
    if args[0] == '-m':
        args = args[1:]
        read_graph = read_makefile
    else:
        read_graph = read_edgefile

    with open(args[0], 'r') as stream:
        graph = read_graph(stream)

    vertices = topological_sort(graph)

    if len(vertices) == len(graph):
        print(' '.join(vertices))
    else:
        print('There is a cycle!')

if __name__ == '__main__':
    main()
