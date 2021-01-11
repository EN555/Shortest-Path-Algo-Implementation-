import unittest
from src.DiGraph import DiGraph
from src.DiGraph import Node
import time

class GraphTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:    # it's happen only at the start of the program def setUp before every test
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_single_node(self):  # check single node function
        node = Node(1, 2, "black")
        self.assertEqual(node.get_key(), 1, "The key is one!!")
        self.assertEqual(node.get_tag(), 2)
        self.assertEqual(node.get_info(), "black")
        self.assertEqual(node.nei_size(), 0, "The node havn't neighbors")
        self.assertEqual(node.get_neighbors(), {}, "The node havn't neighbors")
        self.assertEqual(node.get_neighbors_weight(), {}, "The node havn't neighbors!")
        self.assertEqual(node.get_connect_to_him(), {}, "No one directed to him")

    def test_init_node(self):  # check advanced function in Node class
        node1 = Node(1, 0, "white")
        node2 = Node(2, 0, "black")
        node3 = Node(3, 0, "black")
        node4 = Node(4, 0, "black")
        node1.add_neighbor(node2, 1)
        node1.add_neighbor(node3, 2)
        node1.add_neighbor(node4, 3)
        self.assertEqual(node1.nei_size(), 3, "have 3 neighbors!!")
        self.assertEqual(len(node1.get_neighbors_weight()), 3)
        self.assertEqual(len(node1.get_neighbors()), 3)

    def test_set(self):  # check set operation
        node1 = Node(1, 0, "white")
        node2 = Node(2, 0, "black")
        node3 = Node(3, 0, "black")
        node4 = Node(4, 0, "black")
        node1.add_neighbor(node2, 1)
        node1.add_neighbor(node3, 2)
        node1.add_neighbor(node4, 3)
        node1.set_pos((1, 2, 4))
        node2.set_pos((1, 3, 4))
        node3.set_pos((2, 4, 3))
        node4.set_pos((7, 6, 4))
        self.assertEqual(node1.get_pos(), (1, 2, 4))
        self.assertEqual(node1.get_info(), "white")
        node1.set_info("black")
        self.assertEqual(node1.get_info(), "black")

    def test_time_creator(self):  # check time create nodes
        start = time.time()
        for i in range(100000):
            Node(i, 0, "")
        end = time.time()
        self.assertTrue((end - start) < 10, "it's need to be under 10 seconds!")

    def test_empty_graph(self):
        graph = DiGraph()
        self.assertTrue(graph.get_mc() == 0)
        self.assertTrue(graph.e_size() == 0)
        self.assertTrue(graph.v_size() == 0)
        self.assertFalse(graph.remove_node(1), "The node does not exist!")
        self.assertFalse(graph.remove_edge(1, 2), "The edge already exist!")

    def test_add(self): # chek add node and add edge
        graph = DiGraph()
        graph.add_node(1, (1, 2, 3))    #add node check
        graph.add_node(2, (2, 3, 4))
        graph.add_node(3, (5, 4, 6))
        graph.add_node(4, (3, 4, 6))
        self.assertTrue(4 == graph.v_size())
        self.assertTrue(0 == graph.e_size())
        graph.add_node(1, (2, 3, 4))
        self.assertTrue(4 == graph.v_size())
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 4, 3)
        graph.add_edge(4, 1, 3)
        self.assertTrue(4 == graph.e_size())
        self.assertTrue(8 == graph.get_mc())
        graph.add_edge(1, 2, 4)
        self.assertTrue(8 == graph.get_mc(), "you add exist edge!")
        self.assertTrue(4 == graph.e_size(), "you add exist edge!")
        graph.add_edge(1, 2, -5)
        self.assertTrue(8 == graph.get_mc(), "you add exist edge!")
        self.assertTrue(4 == graph.e_size(), "you add exist edge!")

    def test_remove(self):
        graph = DiGraph()
        graph.add_node(1, (1, 2, 3))  # add node check
        graph.add_node(2, (2, 3, 4))
        graph.add_node(3, (5, 4, 6))
        graph.add_node(4, (3, 4, 6))
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 4, 3)
        graph.add_edge(4, 1, 3)
        self.assertEqual(graph.v_size(), 4, "have only 4 nodes!!")
        self.assertEqual(graph.e_size(), 4, "have only 4 nodes!!")
        graph.remove_node(1)
        self.assertTrue(graph.v_size() == 3)
        self.assertTrue(graph.e_size() == 2)
        graph.remove_node(1)
        self.assertTrue(graph.get_mc() == 11, "add - 8 times, remove 1- node 2- edges")

    def test_get(self):
        graph = DiGraph()
        graph.add_node(1, (1, 2, 3))  # add node check
        graph.add_node(2, (2, 3, 4))
        graph.add_node(3, (5, 4, 6))
        graph.add_node(4, (3, 4, 6))
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 4, 3)
        graph.add_edge(4, 1, 3)
        self.assertTrue(len(graph.get_all_v()) == 4)

    def test_time_bigGraph(self):
        start = time.time()
        graph = DiGraph()
        for i in range(10000):
            graph.add_node(i, (i, i+1, i+2))
            for j in range(100):
                graph.add_edge(j, j+1, 3)
        end = time.time()
        self.assertTrue((end - start) < 10, "it's too much time!!")

if __name__ == '__main__':
    unittest.main()
