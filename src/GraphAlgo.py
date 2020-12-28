# -*- coding: utf-8 -*-

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import heapq
from Graph import Graph

class GraphAlgo(GraphAlgoInterface):
    
    
    def __init__(self , graph : GraphInterface = None) -> None:
        self.graph = graph
    
    def get_graph(self) -> GraphInterface:
        return self.graph
    
    def __Dijkstra(self , src : int) -> dict:
        for node in self.graph.get_all_v().values():
            node.set_tag(float('inf'))
        
        src_O = self.graph.get_all_v()[src]
        src_O.set_tag(0)
    
        Q = list(self.graph.get_all_v().values()).copy()
        heapq.heapify(Q)
        parents = {}
        
        
        while(Q):
            current = heapq.heappop(Q)
            for nei,weight in self.graph.all_out_edges_of_node(current.get_key()).items():
                nei_O = self.graph.get_all_v()[nei]
                if(current.get_tag() + weight < nei_O.get_tag()):
                    nei_O.set_tag(current.get_tag() + weight)
                    parents.update({nei: current.get_key()})
            heapq.heapify(Q)
        return parents
    
    
    
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if(self.graph.get_all_v()[id1] == None or self.graph.get_all_v()[id2] == None):
            return
        
        parents = self.__Dijkstra(id1)
       
        if(self.graph.get_all_v()[id2].get_tag() == float('inf')):
            return ((float('inf') , []))
        
        path = []
        current = id2
        while(current != None):
            path.insert(0 , current)
            current = parents.get(current)
        return ((self.graph.get_all_v()[id2].get_tag() , path))
        
        
    
   









if __name__ == '__main__':
    graph = Graph()
    
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 3, 3)
    graph.add_edge(0, 2, 10)
    graph.add_edge(2, 0, 5)
    
    ga = GraphAlgo(graph)
    
    tuple_ans = ga.shortest_path(3, 2)
    print(tuple_ans)
    
    
    
    
    