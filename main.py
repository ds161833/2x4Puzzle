import copy
import time

import numpy as np

from Astar import astar
from BoardNode import BoardNode
from GBFS import gbfs
from NodeTuple import NodeTuple
from PriorityQueueUtility import merge_queues, get_node_tuple_from_set
from UCS import uniform_cost_search
from pretty_print import print_board_node, print_node_tuple

height = 2
width = 4


def generate_sample(height, width):
    sample = np.arange(height * width)
    # np.random.shuffle(sample)
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

# naive
def h1(node, goal_nodes):
    h1 = 0
    h2 = 0
    goal_node = goal_nodes[0]
    for i in range(height):
        for j in range(width):
            if node.board[i][j] != goal_node.board[i][j]:
                h1 += 1

    goal_node = goal_nodes[1]
    for i in range(height):
        for j in range(width):
            if node.board[i][j] != goal_node.board[i][j]:
                h2 += 1

    return min(h1, h2)

# manhatten
def h2(node, goal_nodes):
    h1 = 0
    h2 = 0
    goal_node = goal_nodes[0]
    for i in range(height):
        for j in range(width):
            if node.board[i][j] != goal_node.board[i][j]:
                h1 += 1

    goal_node = goal_nodes[1]
    for i in range(height):
        for j in range(width):
            if node.board[i][j] != goal_node.board[i][j]:
                h2 += 1

    return min(h1, h2)



def f1(node, goal_nodes, cost):
    return h1(node, goal_nodes) + cost


def f2(node, goal_nodes, cost):
    return h2(node, goal_nodes) + cost


start = time.process_time()
# result = uniform_cost_search(BoardNode(generate_sample(height, width)), generate_goal_nodes(height, width))

# result = gbfs(BoardNode(generate_sample(height, width)), generate_goal_nodes(height, width),
              # lambda node, goal: h1(node, goal))

result = astar(BoardNode(generate_sample(height, width)), generate_goal_nodes(height, width),
              lambda node, goal, cost: f2(node, goal, cost))

finish = time.process_time() - start

for node_tuple in result.queue:
    print_node_tuple(node_tuple)

print()
print("took this ms to run: " + str(finish))
