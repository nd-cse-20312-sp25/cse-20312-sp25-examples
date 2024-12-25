#!/usr/bin/env python3

from collections import defaultdict, deque
import sys

# Types

Graph = dict[int, list[int]]

# Functions

def read_graph(stream=sys.stdin) -> Graph:
    graph = defaultdict(list)

    for line in stream:
        source, target = [int(x) for x in line.split()]
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
