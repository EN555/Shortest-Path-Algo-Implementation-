from src.GraphInterface import GraphInterface
import random as rnd
"""
This graph represent directed weighted graph
"""


class Graph(GraphInterface):

    """
    constructor
    @param nodes dictionary of <key, node object>
    @param number of edges - count the number of the edges in the graph
    @param number of nodes - count the number of the nodes in the graph
    @param number of modes - count the numebr of changes in nodes or edges in the graph
    """
    def __init__(self):
        self.nodes = {}
        self.Number_Of_edges = 0
        self.Number_Of_nodes = 0
        self.Number_Of_modes = 0

    """
    Returns the number of vertices in this graph
    @return: The number of vertices in this graph
    """
    def v_size(self) -> int:
        return self.Number_Of_nodes

    """
    Returns the number of edges in this graph
    @return: The number of edges in this graph
    """
    def e_size(self) -> int:
        return self.Number_Of_edges

    """
    return a dictionary of all the nodes in the Graph, each node is represented using pair (key, node_data)
    """
    def get_all_v(self) -> dict:
        return self.nodes

    """
    return a dictionary of all the nodes connected to (into) node_id ,
    each node is represented using a pair (key, weight)
    """
    def all_in_edges_of_node(self, id1: int) -> dict:
        l1 = self.nodes.get(id1)
        if l1 != None:      # check if have node like him
            return l1.get_connect_to_him()

    """
    return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key,
    weight)
    """
    def all_out_edges_of_node(self, id1: int) -> dict:
        l1 = self.nodes.get(id1)    # check if have node like him
        if l1 != None:
            return self.nodes.get(id1).get_neighbors_weight()

    """
    Adds an edge to the graph.
    @param id1: The start node of the edge
    @param id2: The end node of the edge
    @param weight: The weight of the edge
    @return: True if the edge was added successfully, False o.w.
    If the edge already exists or one of the nodes dose not exists the functions will do nothing
    """
    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        l1, l2 = self.nodes.get(id1), self.nodes.get(id2)
        if l1 == None or l2 == None or weight < 0 or id1 == id2:     # check if the node exist
            return False                                                        # and the edge not exist
        else:       # if they already have not edge
            l1.add_neighbor(l2, weight)  # add to his neighbor edge
            l2.get_connect_to_him().update({id1: l1})   # update at who the he direct to him
            self.Number_Of_edges += 1
            self.Number_Of_modes += 1
            return True

    """
    Adds a node to the graph.
    @param node_id: The node ID
    @param pos: The position of the node
    @return: True if the node was added successfully, False o.w.
    if the node id already exists the node will not be added
    """
    def add_node(self, node_id: int, pos: tuple = (0, 0, 0)) -> bool:
        l1 = self.nodes.get(node_id)
        if l1 != None or node_id < 0:      # check if the node already exist
            return False
        else:       # the node didn't exist yet
            node = Node(node_id, 0, "")    # create new node
            self.nodes.update({node_id: node})  # update the dictionary of all the nodes above
            node.set_pos(pos)   # update the position
            self.Number_Of_nodes += 1      # update the number of nodes
            self.Number_Of_modes += 1      # update the number of modes
            return True

    """
    Returns the current version of this graph,
    on every change in the graph state - the MC should be increased
    @return: The current version of this graph.
    """
    def get_mc(self) -> int:
        return self.Number_Of_modes

    """
    Removes a node from the graph.
    @param node_id: The node ID
    @return: True if the node was removed successfully, False o.w.
    if the node id does not exists the function will do nothing
    """
    def remove_node(self, node_id: int) -> bool:
        l1 = self.nodes.get(node_id)
        if l1 == None:            # no such node
            return False
        else:              # if this node exist
            for to_him in l1.get_connect_to_him().values():    # remove all the edges that direct to this node
                to_him.get_neighbors().pop(node_id)
                to_him.get_neighbors_weight().pop(node_id)
                self.Number_Of_edges -= 1              # update the number of edges
                self.Number_Of_modes += 1              # update the number of modes
            self.Number_Of_edges -= len(l1.get_neighbors())     # update the number of edge that start from him
            self.Number_Of_modes += len(l1.get_neighbors())
            self.nodes.pop(node_id)         # remove the current node
            self.Number_Of_modes += 1
            self.Number_Of_nodes -= 1
        return True

    """
        Removes an edge from the graph.
            @param node_id1: The start node of the edge
            @param node_id2: The end node of the edge
            @return: True if the edge was removed successfully, False o.w.
            If such an edge does not exists the function will do nothing
    """
    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        l1, l2 = self.nodes.get(node_id1), self.nodes.get(node_id2)
        if l1 != None and l2 != None:       # check if the node exist
            l3 = l1.get_neighbors().get(node_id2)
            if l3 != None:              # check if the edge exist
                l1.get_neighbors().pop(node_id2)  # remove the the edge from he start
                l1.get_neighbors_weight().pop(node_id2)   # remove the weight of the edge from the graph
                l2.get_connect_to_him().pop(node_id1)  # remove the edge from he point on
                self.Number_Of_edges -= 1   # update the number of edges
                self.Number_Of_modes += 1   # update the number of modes
                return True
        else:       # if have nothing to be remove
            return False
        
    def __str__(self):
        return(str([node for node in self.get_all_v().values()]))

    def __repr__(self):
        return(str([node for node in self.get_all_v().values()]))    


"""
This class represent single node in directed weighted graph
"""


class Node:

    """
    constructor
    @param key - the ID of the node
    @param tag - the tag use for algorithm
    @param info - the info use for algorithm
    """
    def __init__(self, key: int = 0, tag: float = 0, info: str = None):
        self.key = key
        self.tag = tag
        self.info = info
        self.pos = (0, 0, 0)
        self.neighbor_objects = {}     # represents all the edges that start from him <ID , node>
        self.neighbor_weight = {}      # represents all the weight of the edges <ID , weight>
        self.connect_to_him = {}       # represents all the ndoes that connect to him <ID , node>

    """
    return the key of the node
    """
    def get_key(self) -> int:
        return self.key

    """
    return the tag of the node
    """
    def get_tag(self) -> float:
        return self.tag

    """
    return the info the tag
    """
    def get_info(self) -> str:
        return self.info

    """
    return dictionary of the neighbors
    """
    def get_neighbors(self) -> dict:
        return self.neighbor_objects

    """
    return the number of neighbors
    """
    def nei_size(self) -> int:
        return len(self.neighbor_objects)

    """
    return tuple of the location of the ndoe
    """
    def get_pos(self) -> tuple:
        return self.pos

    """
    return dictionary of all the the weight of the nodes
    """
    def get_neighbors_weight(self) -> dict:
        return self.neighbor_weight

    """
    return all the nodes that direct to him
    """
    def get_connect_to_him(self) -> dict:
        return self.connect_to_him

    """
    @param node object 
    @param weight of the edge
    the function add node to the dictionary of the edge
    """
    def add_neighbor(self, other, weight) -> None:
        self.neighbor_objects.update({other.get_key(): other})
        self.neighbor_weight.update({other.get_key(): weight})

    """
    @param id1 - ID of the node that need to update the weight
    @param weight - weight of the edge 
    """
    def set_weight(self, id1, weight) -> None:
        self.neighbor_weight.update({id1: weight})

    """
    @param id1 - ID of the node that need to update the weight
    @param weight - weight of the edge 
    """
    def set_pos(self, pos) -> None:
        self.pos = pos
    """
    @param other - node neighbor 
    return the weight if the node
    """
    def get_weight(self, other) -> float:
        return self.get_neighbors_weight().get(other.get_key)

    """
    @param info
    the function update the info of the node
    """
    def set_info(self, info) -> None:
        self.info = info

    """
    @param tag
    the function update the tag of the node
    """
    def set_tag(self, tag) -> None:
        self.tag = tag

    """
    @param pos- tuple 
    update the pos of node in graph
    """
    def set_pos(self, pos) -> None:
        self.pos = pos

    """
    @return the key of node and all his neighbors
    """
    def __str__(self):
        s = []
        for key in self.get_neighbors().keys():
            s.append(key)
        return ("The key is: "  + str(self.key) +  " ,The neighbors are: " +  str(s))
    
    def __repr__(self):
        s = []
        for key in self.get_neighbors().keys():
            s.append(key)
        return ("The key is: "  + str(self.key) +  " ,The neighbors are: " +  str(s))

    def __lt__(self , other) -> bool:
        return self.tag < other.tag
    
    def __gt__(self , other) -> bool:
        return self.tag > other.tag
    

if __name__ == '__main__':

    graph = Graph()
    graph.add_node(1, (1, 2, 3))
    graph.add_node(2, (2,3,4))
    graph.add_node(3, (5,4,6))
    graph.add_node(4, (3,4,6))

    # print("The number of nodes is: ", graph.v_size())

    graph.add_edge(1, 2, 3)
    graph.add_edge(2, 3, 3)
    graph.add_edge(3, 4, 3)
    graph.add_edge(4, 1, 3)

    print("The number of edges is: ", graph.e_size())

    # print(graph.get_all_v())

    graph.remove_node(3)
    
    node = Node(1)
    
    print(graph)

    # print("The number of nodes is: ", graph.v_size())

    # print("The number of edges ", graph.e_size())
    #
    # print("the edge is " , graph.all_out_edges_of_node(4))
    #
    # graph.remove_edge(4,1)
    #
    # print("The number of edges is: ", graph.e_size())
