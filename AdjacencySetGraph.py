from Base import Graph
import numpy as np 

class AdjancencySetGraph(Graph):
    
    def  __init__(self, numVertices, directed=False):
        super(AdjancencySetGraph,self ). __init__(numVertices, directed)

        self.vertex_list = []
        for i in range(numVertices):
            self.vertex_list.append( Node(i) )

    def add_edge(self, v1, v2, weight = 1):
        if(v1 < 0 or v1 >= self.numVertices  and v2 < 0 and v2 >= self.numVertices):
            raise ValueError("Vertices are outof bound")

        if weight != 1:
            raise ValueError("wieght cannot be greater then 1")
        
        self.vertex_list[v1].add_edge(v2)

        if self.directed == False:
            self.vertex_list[v2].add_edge(v1)
    
    def get_adjacent_vertices(self, v):
        if(v < 0 or v >= self.numVertices):
            raise ValueError("Vertices are outof bound")
        
        return self.vertex_list[v].get_adjacent_vertices()
    
    def get_indegree(self, v):
        if(v < 0 or v >= self.numVertices):
            raise ValueError("Vertices are outof bound")
        
        indegree = 0
        for i in range(self.numVertices):
            if v in self.get_adjacent_vertices(i):
                indegree = indegree + 1
        
        return indegree

    def get_edge_weight(self, v1, v2):
        return 1

    def display(self):
        print(self.numVertices)
        for i in range(self.numVertices):
            for v in self.get_adjacent_vertices(i):
                print(i, "-->", v)


class Node:
    def __init__(self, vertexId):
        self.vertexId = vertexId
        self.adjacency_set = set()

    def add_edge(self, v):
        if self.vertexId == v:
            raise ValueError("The vertex cannot be adjancent to itself")
        self.adjacency_set.add(v)

    def get_adjacent_vertices(self):
        return sorted(self.adjacency_set)


graph = AdjancencySetGraph(4, directed= False)

graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(2,3)

graph.display()