
class Graph:

    def __init__(self):
        self.nodes = {}
        self.Number_Of_edges = 0
        self.Number_Of_nodes = 0
        self.Number_Of_modes = 0

    def v_size(self):
        return self.Number_Of_nodes

    def e_size(self):
        return self.Number_Of_edges

    def get_all_v(self):
        return self.nodes.items()

    def all_in_edges_of_node(self, id1: int):
        l1 = self.nodes.get(id1)
        if l1 != None:
            Node(l1).get_connect_to_him().items()

    def all_out_edges_of_node(self, id1: int):
        return self.nodes.get(id1).get_neighbors

    def add_edge(self, id1: int, id2: int, weight: float):
        l1 , l2 = self.nodes.get(id1), self.nodes.get(id2)
        if self.nodes != {} and l1 != None and l2 != None:
            Node(l1).add_neighbor(l2, weight)
            Node(l2).get_connect_to_him().update({id1: l1})
            self.Number_Of_edges += 1
            self.Number_Of_modes += 1

    def add_node(self, node_id: int, pos: tuple = None):
        l1 = self.nodes.get(node_id)
        if l1 == None:
         node = Node(node_id, 0, 0)
         self.nodes.update({node_id: node})
         node.set_pos(pos)
         self.Number_Of_nodes += 1

    def get_mc(self):
        return self.Number_Of_modes

    def remove_node(self, node_id: int):
        l1 = self.nodes.get(node_id)
        if l1 != None:
            for to_him in Node(self.nodes.get(node_id)).get_connect_to_him().values():
               Node(to_him).get_neighbors().pop(node_id)
            self.nodes.pop(node_id)
            self.Number_Of_modes += 1
            self.Number_Of_nodes -= 1

    def remove_edge(self, node_id1: int, node_id2: int):
        l1, l2 = self.nodes.get(node_id1), self.nodes.get(node_id2)
        if l1 != None and l2 != None:
            print("hello")
            l3 = Node(l1).get_neighbors().get(node_id2)
            print("the edge is: " ,l3)
            if l3 != None:
                print("hello")
                Node(l1).get_neighbors().pop(node_id1)
                Node(l2).get_connect_to_him().pop(node_id1)
                self.Number_Of_edges -= 1

class Node:

    def __init__(self, key=0, tag=0, info=None):
        self.key = key
        self.tag = tag
        self.info = info
        self.pos = ()
        self.neighbor_objects = {}
        self.neighbor_weight = {}
        self.connect_to_him = {}

    def get_key(self):
        return self.key

    def get_tag(self):
        return self.tag

    def getinfo(self):
        return self.info

    def get_neighbors(self):
        return self.neighbor_objects

    def nei_size(self):
        if self.neighbor_objects == {}:
            return 0
        return len(self.neighbor_objects)

    def get_pos(self):
        return self.pos

    def get_neighbors_weight(self):
        return self.neighbor_weight.items()

    def get_connect_to_him(self):
        return self.connect_to_him

    def add_neighbor(self, other, weight):
        self.neighbor_objects.update({other.get_key(): other})
        self.neighbor_weight.update({other.get_key(): weight})

    def set_weight(self, id1, weight):
        self.neighbor_weight.update({id1: weight})

    def get_weight(self, other):
        return self.get_neighbors_weight().get(other.get_key)

    def set_key(self, key):
        self.key= key

    def set_info(self, info):
        self.info = info

    def set_tag(self, tag):
        self.tag=tag

    def set_pos(self, pos):
        self.pos= pos

    def str(self):
        return "The key is", self.key, "The neighbor is: ", self.get_neighbors()

if __name__ == '__main__':

        graph = Graph()
        graph.add_node(1, (1,2,3))
        graph.add_node(2, (2,3,4))
        graph.add_node(3, (5,4,6))
        graph.add_node(4, (3,4,6))

        print("The number of nodes is: ", graph.v_size())

        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 3, 3)
        graph.add_edge(3, 4, 3)
        graph.add_edge(4, 1, 3)

        print("The number of edges is: " , graph.e_size())

        print(graph.get_all_v())

        graph.remove_node(1)

        print(graph.get_all_v())

        print("The number of nodes is: ", graph.v_size())

        graph.remove_edge(3,4)

        print("The number of edges is: ", graph.e_size())
