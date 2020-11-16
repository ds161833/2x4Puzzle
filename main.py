import numpy as np

# given a matrix 2x4
from BoardNode import BoardNode
from pretty_print import print_board_node

input_board = np.array([list(range(0, 4)), list(range(4, 8))])

starting_node = BoardNode(input_board)

def uniform_cost_search(initial_node, goal_node):
    children = initial_node.get_possible_children()
    current_node = children.pop() # current_node = (1, node)
    current_node.get_possible_children()

print_board_node(starting_node)

print_board_node(starting_node)
