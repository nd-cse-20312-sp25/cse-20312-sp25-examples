#!/usr/bin/env python3

'''
Breadth-first search for a weighted graph
'''

from collections import defaultdict, deque
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

# Functions

def read_graph(stream=sys.stdin) -> Graph:
    graph = defaultdict(list)

    for line in stream:
        source, target, weight = line.split()
        graph[source].append(target)

    return graph

def bfs(graph: Graph, vertex: int) -> None:
    frontier = deque([vertex])   # Vertices to be visited
    visited  = set()             # Vertices already visited

    while frontier:
        vertex = frontier.popleft()

        if vertex in visited:
            continue

        visited.add(vertex)
        
        print(vertex, end=' ')

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                frontier.append(neighbor)
    print()

# Main Execution

def main(stream=sys.stdin):
    graph = read_graph(stream)

    bfs(graph, min(graph.keys()))

if __name__ == '__main__':
    main()
