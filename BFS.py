from queue import Queue
from Base import Graph
from AdjancencyMatrixGraph import AdjancencyMatrixGraph
import numpy as np


def BFS(graph, start=0):
    queue = Queue()
    queue.put(start)

    visited = np.zeros(graph.numVertices)

    while not queue.empty():
        vertex = queue.get()

        if(visited[vertex] == 1):
            continue
        
        for v in graph.get_adjacent_vertices(v):
            if visited[vertex] != 1:
                queue.put(v)
        
        visited[vertex] = 1
        print(vertex)