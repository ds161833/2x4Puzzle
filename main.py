import copy
import time

import numpy as np

from Astar import astar
from BoardNode import BoardNode
from GBFS import gbfs
from NodeTuple import NodeTuple
from PriorityQueueUtility import merge_queues, get_node_tuple_from_set
from UCS import  ucs
from pretty_print import print_board_node, print_node_tuple, node_tuple_to_solution, \
    node_tuple_to_search

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


# naive
def h1(node, goal_nodes):
    h = [0, 0]
    for z in range(2):
        goal_node = goal_nodes[z]
        for i in range(height):
            for j in range(width):
                if node.board[i][j] != goal_node.board[i][j]:
                    h[z] += 1
    return min(h[0], h[1])


# manhatten
def h2(node, goal_nodes):
    h = [0, 0]
    goal_node = goal_nodes[0]
    for i in range(height):
        for j in range(width):
            current_number = node.board[i][j]
            (i_offset, j_offset) = np.where(goal_node.board == current_number)
            i_offset, j_offset = i_offset[0], j_offset[0]
            h[0] += abs(i - i_offset) + abs(j - j_offset)
    return h[0]


def f1(node, goal_nodes, cost):
    return h1(node, goal_nodes) + cost


def f2(node, goal_nodes, cost):
    return h2(node, goal_nodes) + cost


def naive_h(node, goal_nodes, cost):
    if node.board[width - 1][height - 1] == 0:
        return 0
    return 1


def naive_f(node, goal_nodes, cost):
    return naive_h(node, goal_nodes) + cost


def speed(action):
    start = time.time()
    result1, result2 = action()
    return (result1, result2, time.time() - start)


f = open("c://Code//2x4Puzzle//input.txt", "r")
problem_lines = []
for line in f:
    problem_lines.append(line)
f.close()

f = open("c://Code//2x4Puzzle//50samples.txt", "r")
analysis_lines = []
for line in f:
    analysis_lines.append(line)
f.close()

goal_nodes = generate_goal_nodes(height, width)

def solve(algorithm, h, unique_name, problems):
    for i in range(len(problems)):
        line = problems[i].rstrip()
        starting_node = line.split(" ")
        starting_node = BoardNode(np.array(list(map(int, starting_node))).reshape(height, width), None)

        # solution, searched, elapsed = speed(lambda: gbfs(starting_node, goal_nodes, lambda node, goal: h2(node, goal)))
        solution, searched, elapsed = speed(lambda: algorithm(starting_node, goal_nodes, h))
        if solution is not None: solution.reverse()
        create_solution_file(solution, str(i) + "_" + unique_name, elapsed)
        create_search_file(searched, str(i) + "_" + unique_name)

def analyze(algorithm, h, unique_name, problems):
    problems_amount = len(problems)

    total_paths = [0, 0]
    average_paths = [0, 0]
    elapsed = [0, 0]
    no_solution_counter = 0

    for i in range(problems_amount):
        line = problems[i].rstrip()
        starting_node = line.split(" ")
        starting_node = BoardNode(np.array(list(map(int, starting_node))).reshape(height, width), None)

        # solution, searched, elapsed = speed(lambda: gbfs(starting_node, goal_nodes, lambda node, goal: h2(node, goal)))
        solution, searched, current_elapsed = speed(lambda: algorithm(starting_node, goal_nodes, h))
        elapsed[0] += current_elapsed

        if solution is None:
            no_solution_counter += 1
            continue

        total_paths[0] += len(solution)
        total_paths[1] += len(searched.queue)

    average_paths[0] = total_paths[0]/problems_amount
    average_paths[1] = total_paths[1]/problems_amount
    elapsed[1] = elapsed[0]/problems_amount

    print("Analysis of " + str(problems_amount) + " problems for " + unique_name + " algorithm:")
    print("total/average solution paths: " + str(total_paths[0]) + "/" + str(average_paths[0]))
    print("total/average searched paths: " + str(total_paths[1]) + "/" + str(average_paths[1]))
    print("total/average elapsed: " + str(elapsed[0]) + "/" + str(elapsed[1]) + " seconds")
    print("total no solutions: " + str(no_solution_counter))
    print()


def create_solution_file(solution, unique_name, elapsed):
    f = open("c://Code//2x4Puzzle//output//" + unique_name + "_solution.txt", "w")
    if solution is None:
        f.write("No solution")
        return
    for item in solution:
        f.write(node_tuple_to_solution(item) + "\n")
    f.write("Algorithm took: " + str(elapsed) + " s")

def create_search_file(searched, unique_name):
    f = open("c://Code//2x4Puzzle//output//" + unique_name + "_search.txt", "w")
    if searched is None:
        f.write("No solution")
        return
    for item in searched.queue:
        f.write(node_tuple_to_search(item) + "\n")

def get_random_board_node(height, width):
    sample = generate_sample(height, width)
    return BoardNode(sample)


# solve(ucs, h2, "ucs", problem_lines)
# solve(gbfs, h1, "gbfs-h1", problem_lines)
solve(gbfs, h2, "gbfs-h2", problem_lines)
# solve(astar, f1, "astar-h1", problem_lines)
solve(astar, f2, "astar-h2", problem_lines)

# analyze(ucs, h2, "ucs", analysis_lines)
# analyze(gbfs, h1, "gbfs-h1", analysis_lines)
# analyze(gbfs, h2, "gbfs-h2", analysis_lines)
# analyze(astar, f1, "astar-h1", analysis_lines)
# analyze(astar, f2, "astar-h2", analysis_lines)

def solve_random_with_best(height, width):
    board = get_random_board_node(height, width)
    solution, searched, elapsed = speed(lambda: gbfs(board, goal_nodes, h1))

    if solution is None:
        print("no solution")
    else:
        print("solved puzzle " + str(height) + "x" + str(width) + " in " + str(elapsed) + " seconds")

# solve_random_with_best(height, width)

