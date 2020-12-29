# -*- coding: utf-8 -*-

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
import heapq
from Graph import Graph
from Graph import Node
import json

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
        
        
        
        
    def __dfs(self, node : Node , way : str, visited : dict) -> None:
        node.set_tag(node.get_tag() + 1)
        visited.update({node.get_key() : node})
        
        if(way == 'front'):
            for nei in node.get_neighbors().values():
                if(nei.get_key() not in visited.keys()):
                    self.__dfs(nei , way , visited)
        if(way == 'back'):
            for nei in node.get_connect_to_him().values():
                if(nei.get_key() not in visited.keys()):
                    self.__dfs(nei , way , visited)
    
    
    def __find_component(self , node : Node):
        for n in self.graph.get_all_v().values():
            n.set_tag(0)
            
        self.__dfs(node, 'front', {})
        self.__dfs(node, 'back', {})
        
        component = []
        for n in self.graph.get_all_v().values():
            if(n.get_tag() == 2):
                component.append(n.get_key())
                n.set_info("in component")
        
        return component
                
    
    def connected_components(self) -> list:
       
        for node in self.graph.get_all_v().values():
            node.set_info("")
        
        components = []
        
        for node in self.graph.get_all_v().values():
            if(node.get_info() == ""):
                components.append(self.__find_component(node))

        return components

    def connected_component(self, id1: int) -> list:
        if(id1 not in self.graph.get_all_v().keys()):
            return None
        
        components = self.connected_components()
        for component in components:
            if id1 in component:
                return component


    def save_to_json(self, file_name: str) -> bool:
        nodes = []
        for node in self.graph.get_all_v().values():
            nodes.append({'id' : node.get_key() , 
                          'pos' : str(node.get_pos()[0]) + ',' 
                          + str(node.get_pos()[1]) 
                          + ',' + str(node.get_pos()[2])})
        edges = []
        for node in self.graph.get_all_v().values():
            for  nei in node.get_neighbors().values():
                edges.append({'src' : node.get_key() , 
                              'dest' : nei.get_key(), 
                              'w' : node.get_neighbors_weight()[nei.get_key()]})
        json_dict = {'Nodes' : nodes , 'Edges' : edges}
        try:
            with open(file_name , 'w') as file:
                json.dump(json_dict,file)
        except:
            return False
        
        return True

    def load_from_json(self, file_name: str) -> bool:
       
        try:
            with open(file_name, 'r') as file:
                json_dict = json.load(file)
        except:
            return False
        
        new_graph = Graph()
        
        for json_node in json_dict.get('Nodes'):
            if(json_node.get('pos') is not None):
                new_graph.add_node(json_node['id'] , 
                                   tuple([float(x) for x in json_node['pos'].split(',')]))   
            else:
                new_graph.add_node(json_node['id'])
        
        for json_edge in json_dict.get('Edges'):
            new_graph.add_edge(json_edge['src'] , json_edge['dest'], json_edge['w'])
                
        self.graph = new_graph
        return True
            

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
        
        
        #tuple_ans = ga.shortest_path(3, 2)
        #print(tuple_ans)
        
        #print(ga.connected_components())
        #ga1 = GraphAlgo(Graph())
        #print(ga1.connected_components())
        
        #print(ga.connected_component(1))
        
        #ga.save_to_json("../test1.txt")
        
        print(ga.load_from_json('../data/T0.json'))
        print(ga.get_graph())
    
    
    
    
    