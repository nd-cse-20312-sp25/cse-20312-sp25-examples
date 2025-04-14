#!/usr/bin/env python3

''' sssp.py

Example of Dijkstra's algorithm for single source shortest path.
'''

import collections
from heapq import heappush, heappop
import sys

# Types

'''
The graph is represented as an adjacency list using
a dictionary, where the key is the source node and
the value is another dictionary, where the keys
are neigbor vertices and the values are the edge weights
to each vertex, e.g.

{
    source_vertex1 : {neighbor1: weight1, neighbor2: weight2}
    source_vertex2 : . . .
    . . .
}

'''
Graph = dict[str, dict[str, int]]

# Build Graph

def read_graph(stream) -> Graph:
    ''' 
    Read in directed graph 
    Each line is an edge: source, target, weight
    '''
    graph = collections.defaultdict(dict)
    for line in stream:
        source, target, weight = line.split()
        graph[source][target] = int(weight)
    return graph

# Compute SSSP

def compute_sssp(graph: Graph, start: str) -> dict[str, int]:
    ''' Use Dijkstra's Algorithm to compute the single-source shortest path '''
    
    # frontier is a priority queue of tuples (distance, vertex)
    frontier: list[tuple[int, str]] = []

    # visited is a dict of vertex:distance
    visited: dict[str, int] = {}

    # use heap to implement frontier priority queue
    heappush(frontier, (0, start))

    while frontier:
        # pop total_distance, vertex from frontier
        # TODO
        pass

        # if vertex in visited, continue to next iteration
        # TODO
        pass
        
        # add vertex:total_distance to visited
        # TODO
        pass

        # push each unvisited neighbor with its total_distance to frontier
        # TODO
        pass

    return visited

# Main Execution

def main(stream=sys.stdin) -> None:
    # Read Graph
    graph   = read_graph(stream)

    # Compute SSSP
    start   = min(graph.keys())
    visited = compute_sssp(graph, start)

    # Display Distances
    for target in sorted(graph.keys())[1:]:
        print(f'{start} -> {target} = {visited[target]}')

if __name__ == '__main__':
    main()
