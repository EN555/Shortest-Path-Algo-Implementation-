
class Graph:

    def __init__(self):
        self.nodes = {}
        self.Number_Of_edges = 0
        self.Number_Of_nodes = 0
        self.Number_Of_modes = 0

    def v_size(self):
     if self.nodes == {}:
        return 0
     return len(self.nodes)

    def e_size(self):
     if self.nodes == {}:
         return 0
     num = 0
     for key, value in self.nodes.items():
      print("The num: ", num)
      num += int(value.nei_size())
     return num

    def get_all_v(self):
        return self.nodes.items()

    # def all_in_edges_of_node(self, id1: int):
    #     dict= {}
    #     for key, value in self.nodes.items():
    #         for val in value.get_neighbors_weight.items():
    #             if val == id1:
    #              dict.update()

    def all_out_edges_of_node(self, id1: int):
        return self.nodes.get(id1).get_neighbors

    def add_node(self, node_id: int, pos: tuple = None):
        node = Node(node_id)
        self.nodes.update({node_id: node})
        node.set_pos(pos)




class Node:

    def __init__(self, key=0, tag=0, info=None):
        self.key = key
        self.tag = tag
        self.info = info
        self.pos = ()
        self.neighbor_objects = {}
        self.neighbor_weight = {}

    def get_key(self):
        return self.key

    def get_tag(self):
        return self.tag

    def getinfo(self):
        return self.info

    def get_neighbors(self):
        return self.neighbor_objects.items()

    def nei_size(self):
        if self.neighbor_objects == {}:
            return 0
        return len(self.neighbor_objects)

    def get_pos(self):
        return self.pos

    def get_neighbors_weight(self):
        return self.neighbor_weight.items()

    def add_neighbor(self, other, weight):
        self.neighbor_objects.update({other.get_key(): other})
        self.neighbor_weight.update({other.get_key(): weight})

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
        node1 = Node(1, 0, 0)
        node2 = Node(2, 0, 0)
        node2.set_pos((1,5,6))
        node3 = Node(3, 0, 0)
        node4 = Node(4, 0, 0)
        node1.set_pos((1, 2, 3))
        # print(node1.get_pos())
        node1.add_neighbor(node2, 2)
        node1.add_neighbor(node3, 2)
        node1.add_neighbor(node4, 6)
        node2.add_neighbor(node1,2)
        node2.add_neighbor(node3,3)

        # print(node1.get_neighbors())
        # print(node1.get_neighbors_weight())
        # print(node1.get_neighbors())

        for key, value in node1.get_neighbors():
            print(key ,"The val: ", value.get_pos())

        print("The len is: ", len({"bl":"bl", "cds" : "dcsa"}))

        graph = Graph()
        graph.add_node(node1)
        graph.add_node(node2)
        graph.add_node(node3)
        graph.add_node(node4)

        print(graph.v_size())
        print("The edge size is: " ,graph.e_size())

        print("The nei_size", node1.nei_size())