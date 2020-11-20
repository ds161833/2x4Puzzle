class NodeTuple(object):

    def __init__(self, cost, node, priority, parent, f=0, g=0, h=0):
        self.cost = cost
        self.node = node
        self.priority = priority
        self.parent = parent
        self.f = f
        self.g = g
        self.h = h

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.node == other.node

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(self.node)

    def get_parent_chain(self):
        parents = []
        current_node = self

        while current_node is not None:
            parents.append(current_node)
            current_node = current_node.parent

        return parents
