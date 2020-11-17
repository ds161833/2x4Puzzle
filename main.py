import numpy as np
from BoardNode import BoardNode
from pretty_print import print_board_node


input_board = np.array([list(range(0, 4)), list(range(4, 8))])
starting_node = BoardNode(input_board)

print_board_node(starting_node)

starting_node.swap_elements((0,0), (0,1))

print_board_node(starting_node)

starting_node.swap_elements((0,1), (0,2))

print_board_node(starting_node)
