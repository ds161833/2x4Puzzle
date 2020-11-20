from queue import PriorityQueue, Queue

from NodeTuple import NodeTuple
from PriorityQueueUtility import increase_cost_uniformly, get_node_tuple_from_pq


def gbfs(initial_node, goal_nodes, h):
    # set of NodeTuples
    explored = Queue()

    # priority queue of NodeTuples
    frontier = PriorityQueue()
    frontier.put(NodeTuple(0, initial_node, 0, None))
    while not frontier.empty():
        current_node_tuple = frontier.get()

        explored.put(current_node_tuple)

        if is_goal_node(current_node_tuple.node, goal_nodes):
            return current_node_tuple.get_parent_chain(), explored

        current_children_nodes = current_node_tuple.node.get_possible_children(current_node_tuple.cost)
        current_children = PriorityQueue()
        for child_node in current_children_nodes:
            cost = child_node[0]
            node = child_node[1]
            h_value = h(node, goal_nodes)
            current_children.put(NodeTuple(cost, node, h_value, current_node_tuple, 0, cost, h_value))

        for child_node_tuple in current_children.queue:
            if (child_node_tuple not in explored.queue) and (child_node_tuple not in frontier.queue):
                frontier.put(child_node_tuple)

    return None, None


def is_goal_node(node, goal_nodes):
    return node in goal_nodes


# potential bug lol with memory:
def replace_if_higher_cost(new_node_tuple, node_tuple_pq):
    for node_tuple in node_tuple_pq.queue:
        if node_tuple == new_node_tuple:
            if node_tuple.cost > new_node_tuple.cost:
                node_tuple = new_node_tuple
