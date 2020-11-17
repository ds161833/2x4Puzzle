    def uniform_cost_search(initial_node, goal_node):
        children = initial_node.get_possible_children()
        current_node = children.pop() # current_node = (1, node)
        current_node.get_possible_children()

    def is_goal_node