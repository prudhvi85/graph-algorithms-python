from Base import Graph
import numpy as np

class AdjancencyMatrixGraph(Graph):

    def __init__(self, numVertices, directed=False):
        super(AdjancencyMatrixGraph, self).__init__(numVertices, directed)

        self.matrix = np.zeros((numVertices, numVertices))

    def add_edge(self, v1, v2, weight=1):

        if(v1 < 0 or v1 >= self.numVertices  and v2 < 0 and v2 >= self.numVertices):
            raise ValueError("Vertices are outof bound")
        
        if(weight < 1):
            raise ValueError("An Edge Weight Cannot Have < 1")
        
        self.matrix[v1][v2] = weight

        if self.directed == False:
            self.matrix[v2][v1] = weight

    def get_adjacent_vertices(self , v):
        if(v < 0 or v >= self.numVertices):
            raise ValueError("Vertices are outof bound")
        
        adjacent_vertices = []
        for i in range(self.numVertices):
            if self.matrix[v][i] > 0:
                adjacent_vertices.append(i)
        
        return adjacent_vertices

    def get_indegree(self, v):
        if(v < 0 or v >= self.numVertices):
            raise ValueError("Vertices are outof bound")
        
        indegree = 0
        for i in range(self.numVertices):
            if self.matrix[i][v] > 0:
                indegree = indegree + 1
        return indegree

    def get_edge_weight(self, v1, v2):
        return self.matrix[v1][v2]
    
    def display(self):
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->" ,v)

graph = AdjancencyMatrixGraph(4)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(2,3)

graph.display()

