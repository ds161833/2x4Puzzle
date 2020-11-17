class NodeTuple(object):

    def __init__(self, cost, node):
        self.node = node
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.node == other.node

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(self.node)
