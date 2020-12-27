
class Node:

    def __init__(self, key, tag, info):
        self.key = key
        self.tag = tag
        self.info = info
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

