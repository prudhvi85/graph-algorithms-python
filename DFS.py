from queue import Queue
from Base import Graph
from AdjancencyMatrixGraph import AdjancencyMatrixGraph
import numpy as np


def DFS(graph, visited, current = 0):
    if visited[current] == 1:
        return
    
    visited[current] = 1
    print(current)

    for v in graph.get_adjacent_vertices(current):
        DFS(graph, visited, v)

graph = AdjancencyMatrixGraph(9)
visited = np.zeros(graph.numVertices)