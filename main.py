import copy

import numpy as np
from BoardNode import BoardNode
from NodeTuple import NodeTuple
from PriorityQueueUtility import merge_queues, get_node_tuple_from_set
from UCS import uniform_cost_search
from pretty_print import print_board_node, print_node_tuple

height = 2
width = 4


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
    return BoardNode(goal_1, 0), BoardNode(goal_2, 0)


result = uniform_cost_search(BoardNode(generate_sample(height, width)), generate_goal_nodes(height, width))


for node_tuple in result.queue:
    print_node_tuple(node_tuple)
