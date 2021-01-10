# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 20:15:22 2020

@author: nir son
"""
import heapq
import copy
import math
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import time
import queue
from Graph import Graph
from Graph import Node
from GraphAlgo import GraphAlgo
import random as rnd
import sys
from networkx.algorithms.shortest_paths.weighted import *
from os import listdir
from networkx.readwrite import json_graph
import json


if __name__ == '__main__':
   
     
# =============================================================================
#     #files = [f for f in listdir("C:/Users/nir son/Desktop/תכנות מונחה עצמים/מטלה 3/Graphs_no_pos")]
#     #print(files)
#     resolts = []
#     ga = GraphAlgo()
# 
#     files = ['G_10_80_0.json' , 'G_100_800_0.json' , 'G_1000_8000_0.json',
#              'G_10000_80000_0.json','G_20000_160000_0.json' ,
#              'G_30000_240000_0.json']
# 
#     #print(sorted(files))
#     
#     #files = ["../Graphs_no_pos/G_10_80_0.json"]
#     
#     for file in files:
#         
# # =============================================================================
# #         print(
# #         ga.load_from_json( "../Graphs_no_pos/" + file)
# #          
# #         )
# # =============================================================================
#         
#         with open("../Graphs_no_pos/" + file , 'r') as file:
#             g_json = json.load(file)
#             graph = json_graph.node_link_graph(g_json , attrs=dict(source='src', target='dest', name='id',key='key', link='Edges') , directed=True)
#         
#         ST = time.time()
#          
#         
#         #nx.algorithms.shortest_paths.weighted.single_source_dijkstra(graph , 
#          #                   rnd.choice(list(graph.nodes().keys())), 
#           #                  rnd.choice(list(graph.nodes().keys())))
#         
#         scc = nx.algorithms.components.strongly_connected_components(graph)
#         for c in scc:
#             if(rnd.choice(list(graph.nodes().keys())) in c):
#                 break
#         
#         #ga.connected_components()
#         
#         #ga.connected_component(rnd.choice(list(ga.get_graph().get_all_v().keys())))
#         
#         #ga.shortest_path(rnd.choice(list(ga.get_graph().get_all_v().keys())), 
#                          #rnd.choice(list(ga.get_graph().get_all_v().keys())))
#         
#         FT = time.time()
#         
#         resolts.append(FT - ST)
#     
#     print(resolts)
# =============================================================================

# =============================================================================
#     a1 = A(1)
#     a2 = A(2)
# 
#     Q = [a1,a2]
#     heapq.heapify(Q)
#     
#     a1.value = 3
#     
#     heapq.heappush(Q,a1)
#     
#     print(Q)
# =============================================================================
    
# =============================================================================
#     title = 'G_10_80_0'
# 
#     plt.bar([1,6,11] , [0.001,0.001,0.001] , color = 'orange' , label = 'python' , width=0.3)
#     plt.bar([2,7,12] , [0.002,0.002,0.003] , color = 'lightblue' , label = 'java' , width=0.3)
#     plt.bar([3,13] , [0.0001,0.0001] , color = 'green' , label = 'networkx' , width=0.3)
#     plt.title(title)
#     plt.xticks([2,6.5,12],['shortest path' , 'SCC' ,"SCC's"])
#     
#     plt.legend()
#     plt.savefig('C:/Users/nir son/Desktop/תכנות מונחה עצמים/מטלה 3/graphs/' + title + '.png')
#     plt.show()
# =============================================================================
    
# =============================================================================
#     ga = GraphAlgo()
#     print(ga.load_from_json("../Graphs_no_pos/G_100_800_0.json"))
#     #print(sorted(ga.connected_components()))
#     re = [sorted(c) for c in ga.connected_components()]
#     print(re)
# =============================================================================
     graph = nx.DiGraph()
     ga = GraphAlgo()
     print(ga.load_from_json("../Graphs_no_pos/G_100_800_0.json"))
     for node in ga.get_graph().get_all_v().keys():
         graph.add_node(node)
     for node in ga.get_graph().get_all_v().values():
         for nei , w in node.get_neighbors_weight().items():
             graph.add_edge(node.get_key() , nei , weight = w)
     
        
     #re = nx.algorithms.shortest_paths.weighted.single_source_dijkstra(graph , 50 , 71)
     re = [sorted(c) for c in nx.algorithms.components.strongly_connected_components(graph)]
     print(re)
    