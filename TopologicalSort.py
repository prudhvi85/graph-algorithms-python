from queue import Queue
from Base import Graph
from AdjancencyMatrixGraph import AdjancencyMatrixGraph
import numpy as np

def topological_sort(graph):

    queue = Queue()
    indegreeMap = {}

    for i in range(graph.numVertices):
        indegreeMap[i] = graph.get_indegree(i)

        if(indegreeMap[i]  == 0):
            queue.put(i)
    
    sortedList = []

    while not queue.empty():
        vertex = queue.get()

        sortedList.append(vertex)
        
        for v in graph.get_adjacent_vertices(i):
            indegreeMap[v] = indegreeMap[v] - 1

            if(indegreeMap[v] == 0):
                queue.put(indegreeMap[v])