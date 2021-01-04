# -*- coding: utf-8 -*-

from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from typing import List
from Graph import Graph
from Graph import Node
import math
import heapq
import json
import time
import numpy as np
import matplotlib.pyplot as plt
import random as rnd
from enum import Enum
import queue
from sympy.geometry import Point , Circle, Line , intersection


class GraphAlgo(GraphAlgoInterface):
    """ this class is a set of algorithms on an directed weighted graph, 
    including findind the shortest path beetwen two nodes, 
    finding storngly connected components, saving and loading a graph from a json file
    """

    def __init__(self , graph : GraphInterface = None) -> None:
        """ constructor , set the graph for the algorighms to work on"""
        self.graph = graph
        self.time_out =0
        self.dict_help = {}
    
    def get_graph(self) -> GraphInterface:
        """return: the directed graph on which the algorithm works on"""
        return self.graph
    
    def __Dijkstra(self , src : int) -> dict:
        """ an implementation of dijkstra algorightm, 
        psodu-code from https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm"""
        
        for node in self.graph.get_all_v().values(): #initiate all the nodes 'weights' to infinity
            node.set_tag(float('inf'))
        
        src_O = self.graph.get_all_v()[src] #get the src node as a Node object
        src_O.set_tag(0)                     #set the src 'weight' to 0
    
        Q = list(self.graph.get_all_v().values()).copy()    #initiate a prority queue with all the nodes
        heapq.heapify(Q)
        parents = {}    #initiate the 'parenthood' map
        
        
        while(Q):   #go thourgh all the nodes
            current = heapq.heappop(Q)  #get the 'closest' node
            for nei,weight in self.graph.all_out_edges_of_node(current.get_key()).items(): #go though the neighbors of the current node
                nei_O = self.graph.get_all_v()[nei] #get the neighbor as a Node object
                if(current.get_tag() + weight < nei_O.get_tag()):   #if the path though the current node is better,
                    nei_O.set_tag(current.get_tag() + weight)   # set the new 'weight'
                    parents.update({nei: current.get_key()})    #update the 'parenthood' map
            heapq.heapify(Q)    #re-order the heap
       
        return parents
    
    
    
    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """ find the shortest path beetwen the two given nodes. 
        return the path distance and a list representing the path"""
        
        #make sure the nodes exist in the graph
        if(self.graph.get_all_v().get(id1) == None or self.graph.get_all_v().get(id2) == None):
            return None
        
        parents = self.__Dijkstra(id1)  #run dijkstra algorighm
       
        if(self.graph.get_all_v()[id2].get_tag() == float('inf')): #check if there is a path
            return ((float('inf') , []))
        
        path = []
        current = id2
        while(current != None): #re-trace the path backwards, using the 'parenthood'  map
            path.insert(0 , current) #insert the node at the start of the path
            current = parents.get(current) #go to the 'parent'
        
        return ((self.graph.get_all_v()[id2].get_tag() , path)) #return the distance and thee path


    def __dfs_alg(self, arr: list =[], way : str = 'front')-> List[list]:  # tag- d[v], weight- f[v], info- visited, graph - curr graph
        """ param arr: the order of the move on all the nodes
        param graph: get graph at the first time get original graph and after that get transpose graph
        return: list of all ths scc in the graph
        """
        for node in self.graph.get_all_v().values():  # move on all the nodes in the graph and initial their parameter
            node.set_tag(0), node.set_info(Color.WHITE.name), self.dict_help.update({node.get_key(): 0})
        self.time_out =0    # init the time of the dfs algorithm in the graph
        scc = []  # init the list of all the scc of the graph
        for node_key in arr:    # move on all the nodes of the graph according to the order
            node = self.graph.get_all_v().get(node_key)
            if node.get_info() == Color.WHITE.name: # check if the color is white it's represent the never visit there
                node.set_tag(self.time_out)
                scc.append(self.__dfs_rec(node, [] , way))    # keep th scc in the list
        return scc


    def __dfs_rec(self, node: Node = None, ls_nei: list = [] , way: str = 'front'):   # run dfs from specific node
            if node.get_info() == Color.WHITE.name:  # if the color is white first need to update the color
                node.set_info(Color.GREY.name)
                node.set_tag(self.time_out)
                ls_nei.append(node.get_key())
                self.time_out += 1
           
            if(way == 'front'):
                for nei in node.get_neighbors().values():   # if it's was grey or white need to check his neighbors
                   if nei.get_info() == Color.WHITE.name:
                       self.__dfs_rec(nei, ls_nei , way)   # the function will stop when that won't fount white node
            else:
                for nei in node.get_connect_to_him().values():   # if it's was grey or white need to check his neighbors
                   if nei.get_info() == Color.WHITE.name:
                       self.__dfs_rec(nei, ls_nei , way)   # the function will stop when that won't fount white node
            
            node.set_info(Color.BLACK.name)
            self.dict_help.update({node.get_key(): self.time_out})  # <key, finish time>
            self.time_out += 1
            return ls_nei


    def connected_components(self) -> List[list]:
        """  Finds all the Strongly Connected Component(SCC) in the graph , represented by list of lists"""
        self.__dfs_alg(self.graph.get_all_v().keys(), 'front')     # first call dfs on the original graph

        sort_list = list(self.graph.get_all_v().keys()).copy()  #get list of nodes
       
        sort_list.sort(key = lambda x : self.dict_help.get(x) , reverse=True)   #sort list by desending finishing times
            
        scc = self.__dfs_alg(sort_list, 'back')  # second call dfs
        return scc  # return all the scc of the graph


    def connected_component(self, id1: int) -> list:
        """ find and return the strongly connected component of the 
        given node (the component is represented by a list)"""
        if id1 not in self.get_graph().get_all_v().keys():     # check if the id1 contain in the graph nodes
            return None
        comp_list = self.connected_components()   # list of list of all SCC
        for arr in comp_list:   # search at which scc id1 is in
            if id1 in arr:
                    return arr  # return the specific component in the graph

    def save_to_json(self, file_name: str) -> bool:
        """ save the graph into a json file. return if the graph was saved successfuly"""

        nodes = []  #the list of nodes
        for node in self.graph.get_all_v().values():    #for each node in the graph
            nodes.append({'id' : node.get_key() ,               #save the data in json format
                          'pos' : str(node.get_pos()[0]) + ','
                          + str(node.get_pos()[1]) 
                          + ',' + str(node.get_pos()[2])})
        
        edges = []  #the list of edges
        for node in self.graph.get_all_v().values():     #for each edge in the graph
            for  nei in node.get_neighbors().values():
                edges.append({'src' : node.get_key() ,   #save the data in json format
                              'dest' : nei.get_key(), 
                              'w' : node.get_neighbors_weight()[nei.get_key()]})
        
        json_dict = {'Nodes' : nodes , 'Edges' : edges} #make a dict representing the graph
        try:
            with open(file_name , 'w') as file: #try to save the graph into the file
                json.dump(json_dict,file)
        except:
            return False    #if the saving faild, return false
        
        return True

    def load_from_json(self, file_name: str) -> bool:
        """ loads a graph from a json file. return if a grapg was successfuly loaded"""
       
        try:    #try to read the json from the file
            with open(file_name, 'r') as file:
                json_dict = json.load(file)
        except: #if could'nt read from the file, return false
            return False
        
        new_graph = Graph() #make a new graph
        
        for json_node in json_dict.get('Nodes'):    #get the list of nodes from the json
            if(json_node.get('pos') is not None):   #check if a position was give
                new_graph.add_node(json_node['id'] , #add a node with the given data
                                   tuple([float(x) for x in json_node['pos'].split(',')]))   
            else:   #if a position was not given
                new_graph.add_node(json_node['id']) #add a node with default position
        
        for json_edge in json_dict.get('Edges'):    #get the list of edges from the json
            new_graph.add_edge(json_edge['src'] , json_edge['dest'], json_edge['w'])    #add an edge with the given data
                
        self.graph = new_graph  #set the new grah
        return True

    def plot_graph(self) -> None:
        x,y = [],[]
        
        
        for node in self.graph.get_all_v().values():
            if node.get_pos() == (0,0,0):
                node.set_pos((rnd.random(),rnd.random(),0))
        
        x_max , x_min  ,y_max , y_min = float('-inf'),  float('inf'), float('-inf'),  float('inf')
        
        for node in self.graph.get_all_v().values():
            if node.get_pos()[0] < x_min:
                x_min = node.get_pos()[0]
            if node.get_pos()[0] > x_max:
                x_max = node.get_pos()[0]
            if node.get_pos()[1] < y_min:
                y_min = node.get_pos()[1]
            if node.get_pos()[1] > y_max:
                y_max = node.get_pos()[1]
            
            x.append(node.get_pos()[0])
            y.append(node.get_pos()[1])
        
        normal_x = lambda i : (i - x_min)/(x_max - x_min)
        normal_y = lambda i : (i - y_min)/(y_max - y_min)
        x = [normal_x(i) for i in x]
        y = [normal_y(i) for i in y]
        
        fig, ax = plt.subplots(figsize=(100,100))
        
        ax.scatter(x,y,color = 'lightgreen', linewidths = 1 , edgecolors='green' , s = 150)
        ax.set_xticks([])
        ax.set_yticks([])
        

        
        
        for node in self.graph.get_all_v().values():
            x1,y1 = normal_x(node.get_pos()[0]) , normal_y(node.get_pos()[1])
            ax.annotate(node.get_key(),(x1,y1 + 0.012) , size = 15)
            for nei in node.get_neighbors().values():
                x2,y2 = normal_x(nei.get_pos()[0]) , normal_y(nei.get_pos()[1])
                
                ax.arrow(x1 ,y1 ,x2-x1 ,y2-y1 ,length_includes_head=True , color = '#A6D800' , head_width=0.01)  
       
        plt.show()

class Color(Enum):
    WHITE = 1,
    BLACK = 2,
    GREY = 3


if __name__ == '__main__':

# =============================================================================
#     graph = Graph()
#     graph.add_node(0)#, (1, 200))
#     graph.add_node(1)
#     graph.add_node(2)#, (4543, 4455))
#     graph.add_node(3)#, (7544, 5442))
#     graph.add_node(4)#, (155, 266))
#     graph.add_node(5)
#     graph.add_node(6)#, (16670, 711))
#     graph.add_node(7)#, (162, 34))
#     graph.add_node(8)
# 
#     
#     graph.add_edge(0, 1, 1)
#     graph.add_edge(1, 2, 2)
#     graph.add_edge(2, 3, 3)
#     graph.add_edge(0, 2, 10)
#     graph.add_edge(2, 0, 5)
#     graph.add_edge(3, 5, 5)
#     graph.add_edge(5, 3, 5)
#     graph.add_edge(6, 6, 5)
#     graph.add_edge(3,8, 5)
#     graph.add_edge(7, 3, 5)
#     graph.add_edge(8, 2, 5)
#     graph.add_edge(8, 5, 5)
#     graph.add_edge(4,6, 5)
#     graph.add_edge(4,8, 5)
# =============================================================================


    # tuple_ans = ga.shortest_path(0, 3)
    # print(tuple_ans)
# =============================================================================
#     graph = Graph()
#    
#     graph.add_node(0 ,(1,2,0))
#     graph.add_node(1,(2,2,0))
#     graph.add_node(2,(2,1,0))
#     graph.add_node(3,(1,1,0))
#     graph.add_node(4,(1,1,0))
#     graph.add_node(5,(1,1,0))
#     graph.add_node(6,(1,1,0))
#     graph.add_node(7,(1,1,0))
# 
#     graph.add_edge(0, 1, 1)
#     graph.add_edge(1, 2, 2)
#     graph.add_edge(2, 3, 3)
#     graph.add_edge(0, 2, 10)
#     graph.add_edge(3, 0, 5)
#     graph.add_edge(2, 4, 5)
#     graph.add_edge(5, 3, 5)
#     graph.add_edge(5, 6, 5)
#     graph.add_edge(6, 7, 5)
#     graph.add_edge(7, 5, 5)
# =============================================================================



    # graph.add_edge(3, 5, 5)
    # graph.add_edge(5, 3, 5)
    # graph.add_edge(6, 6, 5)
    # graph.add_edge(3,8, 5)
    # graph.add_edge(7, 3, 5)
    # graph.add_edge(8, 2, 5)
    # graph.add_edge(8, 5, 5)
    # graph.add_edge(4,6, 5)
    # graph.add_edge(4,8, 5)

    graph = Graph()

    graph.add_node(0, (1, 2, 0))
    graph.add_node(1, (2, 2, 0))
    graph.add_node(2, (2, 1, 0))
    graph.add_node(3, (1, 1, 0))

    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 3, 0.5)
    graph.add_edge(2, 0, 5)
    graph.add_edge(0, 2, 2.3)
    ga = GraphAlgo(graph)
    print(ga.connected_components())
    #print(ga.connected_component(1))


    # tuple_ans = ga.shortest_path(0, 3)
    # print(tuple_ans)
    # graph = Graph()
    #
    # graph.add_node(0)
    # graph.add_node(1)
    # graph.add_node(2)
    # graph.add_node(3)
    #
    # graph.add_edge(0, 1, 1)
    # graph.add_edge(1, 2, 2)
    # graph.add_edge(2, 3, 3)
    # graph.add_edge(0, 2, 10)
    # graph.add_edge(2, 0, 5)
        
    # ga = GraphAlgo(graph)

    # ST = time.time()
    # ga = GraphAlgo(graph)
    # ga.load_from_json('../data/A3')
    # ga.plot_graph()
    # print(time.time() - ST)

        #tuple_ans = ga.shortest_path(3, 2)
        #print(tuple_ans)
        
        #print(ga.connected_components())
        #ga1 = GraphAlgo(Graph())
        #print(ga1.connected_components())
        
        #print(ga.connected_component(2))
        
        #ga.save_to_json("../test1.txt")
        
        #print(ga.load_from_json('../data/T0.json'))
        #print(ga.get_graph())




    
    