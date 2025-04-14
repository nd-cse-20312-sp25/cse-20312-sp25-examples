#!/usr/bin/env python3

''' 
mst_prim.py

Example of Prim's algorithm for computing the 
Minimum Spanning Tree (MST) of a graph.
'''

from collections import defaultdict
from heapq import heappop, heappush
import sys

# Types

Graph = dict[str, dict[str, int]]

# Build Graph

def read_graph(stream) -> Graph:
    graph: Graph = defaultdict(dict)
    for line in stream:
        source, target, weight = line.split()
        # Graph is undirected, so we add edges in both directions
        graph[source][target] = int(weight)
        graph[target][source] = int(weight)
    return graph

# Compute MST

def compute_mst(graph: Graph, origin: str) -> tuple[int, dict[str, str]]:
    '''
    Compute the Minimum Spanning Tree (MST) from the origin vertex.
    Return the total weight of the MST and a dict of {vertex:source, }
    where source is the predecessor of the vertex.
    '''

    # frontier is priority queue of tuples (distance, vertex, source),
    # where source is the predecessor of the current vertex
    frontier = [(0, origin, origin)]

    # visited is a dict of {vertex:source, }
    visited  = {}
    total_weight = 0

    while frontier:
        weight, vertex, source = heappop(frontier)

        if vertex in visited:
            continue

        # add vertex:source to the visited list and update total weight
        # TODO:
        pass

        for neighbor, weight in graph[vertex].items():
            if not neighbor in visited:
                # Push the neighbor to the frontier as a tuple
                # (weight from predecessor, vertex, predecessor)
                # TODO:
                pass

    # Delete origin vertex from visited list to be returned
    del visited[origin]
    return total_weight, visited

# Main Execution

def main(args=None) -> None:
    if args is None:
        args = sys.argv[1:]
    if len(args) != 2:
        print('Usage:  mst_prim.py graph_file origin')
        sys.exit(1)

    with open(args[0], 'r') as stream:
        graph = read_graph(stream)
    
    origin = args[1]

    # MST
    mst_length, mst_edges = compute_mst(graph, origin)
    edges = sorted(sorted(t) for t in mst_edges.items())

    print(f'MST length = {mst_length}')
    print('MST edges: '+' '.join(f'{source}{target}' for source, target in edges))

if __name__ == '__main__':
    main()
