import time
from queue import PriorityQueue, Queue

from NodeTuple import NodeTuple
from PriorityQueueUtility import increase_cost_uniformly, get_node_tuple_from_pq


def ucs(initial_node, goal_nodes, h):
    start = time.time()
    # set of NodeTuples
    explored = Queue()

    #priority queue of NodeTuples
    frontier = PriorityQueue()
    frontier.put(NodeTuple(0, initial_node, 0, None, 0, 0, 0))
    while not frontier.empty():
        elapsed = time.time() - start
        if elapsed > 3:
            return None, None
        current_node_tuple = frontier.get()

        explored.put(current_node_tuple)

        if is_goal_node(current_node_tuple.node, goal_nodes):
            return current_node_tuple.get_parent_chain(), explored

        current_children_nodes = current_node_tuple.node.get_possible_children(current_node_tuple.cost)
        current_children = PriorityQueue()
        for child_node in current_children_nodes:
            cost = child_node[0]
            node = child_node[1]
            current_children.put(NodeTuple(cost, node, cost, current_node_tuple, 0, cost, 0))

        for child_node_tuple in current_children.queue:
            if (child_node_tuple not in explored.queue) and (child_node_tuple not in frontier.queue):
                frontier.put(child_node_tuple)
            else:
                if child_node_tuple in frontier.queue:
                    replace_if_higher_cost(child_node_tuple, frontier)

    return None, None


def is_goal_node(node, goal_nodes):
    return node in goal_nodes



# potential bug lol with memory:
def replace_if_higher_cost(new_node_tuple, node_tuple_pq):
    for node_tuple in node_tuple_pq.queue:
        if node_tuple == new_node_tuple:
            if node_tuple.cost > new_node_tuple.cost:
                node_tuple = new_node_tuple
