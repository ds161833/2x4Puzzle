class NodeTuple(object):

    def __init__(self, weight, board):
        self.board = board
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight
