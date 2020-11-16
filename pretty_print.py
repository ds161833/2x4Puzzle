cyan = '\033[96m'
red = '\033[91m'


def add_color(string, color):
    return color + str(string) + color + ' '


def print_board_node(node):
    """

    :type node: BoardNode.BoardNode
    """
    input_board = node.board

    for i in range(len(input_board)):
        row_string = ''
        for j in range(len(input_board[0])):
            current_number = input_board[i][j]

            if current_number == 0:
                row_string += add_color(current_number, red)
            else:
                row_string += add_color(current_number, cyan)

        print(row_string)