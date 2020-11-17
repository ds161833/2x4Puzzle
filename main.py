import numpy as np
from BoardNode import BoardNode
from pretty_print import print_board_node

def generate_sample(height, width):
    sample = np.arange(height*width)
    np.random.shuffle(sample)
    return sample.reshape((height, width))



input_board = generate_sample(3, 4)
starting_node = BoardNode(input_board)


print_board_node(starting_node)
children = starting_node.get_regular_move_states()
print()
for child in children:
    print_board_node(child)
    print()
