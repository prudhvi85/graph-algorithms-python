import abc
import numpy

class Graph(abc.ABC):

    def __init__(self, numVertices, directed=False):
        self.numVertices = numVertices
        self.directed = directed

    @abc.abstractclassmethod
    def add_edge(self, v1, v2, weight):
        pass
    
    @abc.abstractclassmethod
    def get_adjacent_vertices(self, v):
        pass
    
    @abc.abstractclassmethod
    def get_indegree(self, v):
        pass
    
    @abc.abstractclassmethod
    def get_edge_weight(self, v1, v2):
        pass

    @abc.abstractclassmethod
    def display(self):
        pass
