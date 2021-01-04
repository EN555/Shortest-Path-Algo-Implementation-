# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:23:31 2021

@author: nir son
"""

from Graph import Graph
from Graph import Node
from GraphAlgo import GraphAlgo
import math
import time
import random

import unittest

def simpleGraphGenerator() -> Graph:
    """ generate a ssimple graph with 4 nodes """
    
    graph = Graph()
    
    graph.add_node(0 , (1,2,0))
    graph.add_node(1 , (2,2,0))
    graph.add_node(2 , (2,1,0))
    graph.add_node(3 , (1,1,0))
    
    graph.add_edge(0,1,1)
    graph.add_edge(1,2,2)
    graph.add_edge(2,3,0.5)
    graph.add_edge(2,0,5)
    graph.add_edge(0,2,2.3)
    
    return graph
    

class GraphAlgoTest(unittest.TestCase):
    
    def test_shortest_path(self):
        ga = GraphAlgo(simpleGraphGenerator())
        
        self.assertEqual(ga.shortest_path(0,3) , (2.8, [0,2,3]), "the shortest path from 0 to 3 is (2.8, [0,2,3])")
        self.assertEqual(ga.shortest_path(3,2), (math.inf , []) , "no path from 3 to 2")
        self.assertEqual(ga.shortest_path(1,1) , (0,[1]), "path from node to itself is 0")
        
        self.assertIsNone(ga.shortest_path(5,6) , "nodes 5 and 6 are not in the graph")
        self.assertIsNone(ga.shortest_path(0,7) , "node 7 is not in the graph")
        
    
    def test_connected_components(self):
        ga = GraphAlgo(simpleGraphGenerator())
        
        self.assertEqual(ga.connected_components().sort() , [[3],[0,1,2]].sort(), "connected components dont math")
        
        ga.get_graph().remove_edge(2,0)
        self.assertEqual(ga.connected_components().sort() , [[0],[1],[2],[3]].sort(), "connected components dont math")
        
        ga = GraphAlgo(Graph())
        self.assertEqual(ga.connected_components() , [], "emtpy graph have no SCC")
        
    def test_connected_component(self):
        ga = GraphAlgo(simpleGraphGenerator())
        
        self.assertEqual(ga.connected_component(1).sort() , [0,1,2].sort(), "worng SCC")
        self.assertEqual(ga.connected_component(3) , [3], "worng SCC")
        
        self.assertIsNone(ga.connected_component(7), "node 7 is not in the graph")
        
    def test_save_load_from_json(self):
        graph = simpleGraphGenerator()
        ga = GraphAlgo(graph)
        
        self.assertTrue(ga.save_to_json("test1.json"),  "graph should be saved")
        self.assertTrue(ga.save_to_json("test1.json"),  "can't override existing file")
        
        self.assertTrue(ga.load_from_json("test1.json") , "graph should be loaded")
        
        self.assertEqual(ga.get_graph() , graph, "loaded wrong graph")
        
        self.assertFalse(ga.load_from_json("no_file") , "there is not such file")
        
        ga = GraphAlgo(Graph())
        self.assertTrue(ga.save_to_json("test3.json"), "empty graph should be saved")
        self.assertTrue(ga.load_from_json("test3.json"), "empty graph should be loaded")
        self.assertEqual(ga.get_graph() , Graph() , "not loaded empty graph")
        
        
        graph = simpleGraphGenerator()
        ga = GraphAlgo(graph)
        ga.save_to_json("test2.json")
        graph.remove_edge(1,2)
        ga.load_from_json("test2.json")
        self.assertNotEqual(graph , ga.get_graph() , "chenges to graph should not effect json")


if __name__ == '__main__':
    unittest.main()
        
    
        
        
        
        
        
        
        
        
        
        
    
    