from queue import PriorityQueue

from NodeTuple import NodeTuple
from PriorityQueueUtility import increase_cost_uniformly, get_node_tuple_from_pq


def uniform_cost_search(initial_node, goal_nodes):

    # set of NodeTuples
    explored = set()

    #priority queue of NodeTuples
    frontier = PriorityQueue()
    frontier.put(NodeTuple(0, initial_node))

    while not frontier.empty():
        current_node_tuple = frontier.get()

        explored.add(current_node_tuple)

        if is_goal_node(current_node_tuple.node, goal_nodes):
            return explored

        current_children = current_node_tuple.node.get_possible_children()
        increase_cost_uniformly(current_children, current_node_tuple.cost)

        for child_node_tuple in current_children:
            if (child_node_tuple not in explored) and (child_node_tuple not in frontier):
                frontier.put(child_node_tuple)
            else:
                if child_node_tuple in frontier:
                    replace_if_higher_cost(child_node_tuple, frontier)

    return None


def is_goal_node(node, goal_nodes):
    return node in goal_nodes

# potential bug lol with memory:
def replace_if_higher_cost(new_node_tuple, node_tuple_pq):
    for node_tuple in node_tuple_pq.queue:
        if node_tuple == new_node_tuple:
            if node_tuple.cost > new_node_tuple.cost:
                node_tuple.cost = new_node_tuple.cost
