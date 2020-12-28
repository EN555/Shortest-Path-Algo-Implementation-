import unittest
import time
from src.Graph import Node


class NodeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_single_node(self):     # check single node function
        node = Node(1, 2, "black")
        self.assertEqual(node.get_key(), 1, "The key is one!!")
        self.assertEqual(node.get_tag(), 2)
        self.assertEqual(node.get_info(), "black")
        self.assertEqual(node.nei_size(), 0, "The node havn't neighbors")
        self.assertEqual(node.get_neighbors(), {}, "The node havn't neighbors")
        self.assertEqual(node.get_neighbors_weight(), {}, "The node havn't neighbors!")
        self.assertEqual(node.get_connect_to_him(), {}, "No one directed to him")

    def test_init_node(self):       # check advanced function in Node class
        node1 = Node(1, 0, "white")
        node2 = Node(2, 0, "black")
        node3 = Node(3, 0, "black")
        node4 = Node(4, 0, "black")
        node1.add_neighbor(node2, 1)
        node1.add_neighbor(node3, 2)
        node1.add_neighbor(node4, 3)
        self.assertEqual(node1.nei_size(), 3, "have 3 neighbors!!")
        self.assertEqual(len(node1.get_neighbors_weight()),3)
        self.assertEqual(len(node1.get_neighbors()), 3)

    def test_set(self):     # check set operation
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

if __name__ == '__main__':
    unittest.main()