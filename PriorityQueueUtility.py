def merge_queues(q, q2):
    for item in q2.queue:
        q.put(item)


def get_nodes_from_pq(pq):
    nodes_only = []

    for node_tuple in pq.quque:
        nodes_only.append(node_tuple.node)
    return nodes_only


def increase_cost_uniformly(pq, cost):
    for node_tuple in pq.queue:
        node_tuple.cost += cost


def get_node_tuple_from_set(item, set):
    for set_item in set:
        if set_item.node == item:
            return set_item
    return None

def get_node_tuple_from_pq(item, pq):
    for set_item in pq.queue:
        if set_item.node == item:
            return set_item
    return None
