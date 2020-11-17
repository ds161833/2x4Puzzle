import numpy as np
from BoardNode import BoardNode
from pretty_print import print_board_node

height = 2
width = 3


def generate_sample(height, width):
    sample = np.arange(height * width)
    np.random.shuffle(sample)
    return sample.reshape((height, width))


def generate_goal_nodes(height, width):
    goal_1 = np.roll(
        np.arange(height * width), -1
    ).reshape(height, width)

    goal_2 = np.transpose(
        np.roll(
            np.arange(height * width), -1
        ).reshape(width, height)
    )
    return goal_1, goal_2


input_board = generate_sample(height, width)
starting_node = BoardNode(input_board)

goal_1, goal_2 = generate_goal_nodes(height, width)

print_board_node(BoardNode(goal_1))
print()
print_board_node(BoardNode(goal_2))
