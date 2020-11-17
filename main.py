import numpy as np
from BoardNode import BoardNode
from pretty_print import print_board_node

def generate_sample(height, width):
    sample = np.arange(height*width)
    np.random.shuffle(sample)
    return sample.reshape((height, width))



input_board = generate_sample(2, 4)
starting_node = BoardNode(input_board)

copied_array = np.copy(input_board)

print(BoardNode(input_board) == BoardNode(copied_array))


#
# print_board_node(starting_node)
# children = starting_node.get_possible_children()
# print()
# while not children.empty():
#     child = children.get()
#     print_board_node(child.board)
#     print()
