class NodeTuple(object):

    def __init__(self, cost, node, priority):
        self.cost = cost
        self.node = node
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.node == other.node

    def __hash__(self):
        """Overrides the default implementation"""
        return hash(self.node)
