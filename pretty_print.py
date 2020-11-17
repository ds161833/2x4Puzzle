import numpy as np

cyan = '\033[96m'
red = '\033[91m'


def add_color(string, color, width):
    fixed_width = "{0:>" + str(width) + "}"
    return color + fixed_width.format(str(string)) + color + ' '


def print_board_node(node):
    """

    :type node: BoardNode.BoardNode
    """
    input_board = node.board

    for i in range(len(input_board)):
        row_string = ''
        width = len(str(np.amax(input_board)))
        for j in range(len(input_board[0])):
            current_number = input_board[i][j]

            if current_number == 0:
                row_string += add_color(current_number, red, width)
            else:
                row_string += add_color(current_number, cyan, width)

        print(row_string)


def print_node_tuple(node_tuple):
    string = str(node_tuple.cost) + " " + str(node_tuple.node.num_swapped) + " "
    for number_row in node_tuple.node.board:
        for number in number_row:
            string += add_color(number, cyan, 1) + " "
    print(string)
