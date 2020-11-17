def add_pq_to_pq(q, q2):
    for item in q2.queue:
        q.put(item)


def is_node_in_pq(pq, node):
    nodes_only = []

    for node_tuple in pq.quque:
        nodes_only.append(node_tuple.board)
    return node in nodes_only
