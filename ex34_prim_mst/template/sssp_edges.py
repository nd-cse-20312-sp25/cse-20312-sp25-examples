#!/usr/bin/env python3

''' 
sssp_edges.py

Revised version of Dijkstra's algorithm that returns the list of edges in the shortest path.
'''

from collections import defaultdict
from heapq import heappop, heappush
import sys

# Types

# Graph is a dict of {vertex: {neighbor: weight, }}
Graph = dict[str, dict[str, int]]

# Build Graph

def read_graph(stream) -> Graph:
    graph: Graph = defaultdict(dict)
    for line in stream:
        source, target, weight = line.split()
        graph[source][target] = int(weight)
        graph[target][source] = int(weight)
    return graph

# Compute SSSP

def compute_sssp(graph: Graph, origin: str) -> dict[str, str]:
    '''
    Compute the Single Source Shortest Path (SSSP) from the origin vertex.
    Return a dict of {vertex:source, } where source is the predecessor of the vertex.
    '''
    
    # frontier is priority queue of tuples (distance, vertex, source),
    # where source is the predecessor of the current vertex
    frontier = [(0, origin, origin), ]

    # visited is a dict of {vertex:source, }
    visited  = {}

    while frontier:
        # Pop the vertex with the smallest distance
        distance, vertex, source = heappop(frontier)

        if vertex in visited:
            continue

        # add vertex:source to the visited list
        visited[vertex] = source

        for neighbor, weight in graph[vertex].items():
            if not neighbor in visited:
                # Push the neighbor to the frontier as a tuple 
                # (total distance from origin, vertex, predecessor)
                # TODO:
                pass

    # Delete origin vertex from visited list to be returned
    del visited[origin]
    return visited

def reconstruct_path(visited: dict[str, str], origin: str, destination: str) -> list[str]:
    path = []

    # Reconstruct path from destination to origin
    curr = destination
    while curr != origin:
        # Append the current vertex to the end of the path
        # and update the current vertex to its predecessor.
        # Note that the order of the path in the list is reversed,
        # so the path will be reversed before returning.
        # TODO:
        pass

    path.append(origin)
    return reversed(path)


# Main Execution

def main(args=None) -> None:
    if args is None:
        args = sys.argv[1:]
    if len(args) != 2:
        print('Usage: sssp_edges.py <graph> <origin>')
        sys.exit(1)
    
    # Read graph from file as the first command line argument
    with open(args[0], 'r') as stream:
        graph  = read_graph(stream)
    
    # Origin vertex is the second command line argument
    origin = args[1]

    # SSSP
    sssp  = compute_sssp(graph, origin)
    print('SSSP')
    for target in sorted(graph):
        path = reconstruct_path(sssp, origin, target)
        print(f'{origin} -> {target} = {" ".join(path)}')

if __name__ == '__main__':
    main()
