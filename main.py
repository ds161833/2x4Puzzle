import copy

import numpy as np
from BoardNode import BoardNode
from NodeTuple import NodeTuple
from PriorityQueueUtility import merge_queues, get_node_tuple_from_set
from UCS import uniform_cost_search
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
    return BoardNode(goal_1), BoardNode(goal_2)


# result = uniform_cost_search(BoardNode(generate_sample(height, width)), generate_goal_nodes(height, width))
result = uniform_cost_search(generate_goal_nodes(height, width)[0], generate_goal_nodes(height, width))


for node_tuple in result:
    print_board_node(node_tuple.node)
