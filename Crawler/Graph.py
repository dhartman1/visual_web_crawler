import pprint

class Graph:
    def __init__(self, nodes=[], edges=[]):
        self.nodes = nodes
        self.edges = edges

    def add_node(self, node, node_id):
        node.id = node_id
        self.nodes.append(node)

    def add_edge(self, parent_id, target_id):
        edge = Edge(parent_id, target_id)
        self.edges.append(edge)

class Page_Node:
    __slots__ =('url', 'parents_list', 'title', 'parent_node', 'id', 'node_depth')
    def __init__(self, url, parents_list, title, node_depth, id = None, parent_node=None):
        self.url = url
        self.parents_list = parents_list
        self.title = title
        self.node_depth = int(node_depth)
        self.id = id
        self.parent_node = parent_node
        
        
    def printdict(self):
       pprint.pprint(dict({'id': self.id,
                            'parent': self.parent_node,
                            'node depth': self.node_depth,
                            'title': self.title,
                            'url': self.url}))

        
class Edge:
    __slots__ = ['parent', 'target']
    def __init__(self, parent, target):
        self.parent = parent
        self.target = target
        
      